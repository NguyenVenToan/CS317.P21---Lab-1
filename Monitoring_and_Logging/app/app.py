from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exception_handlers import http_exception_handler
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List
import numpy as np
import joblib
import logging
import time
import sys
import os
from logging.handlers import SysLogHandler
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Summary, Counter

# ============ CONFIG ============ #
MODEL_PATH = "model_rf.pkl"
EXPECTED_NUM_FEATURES = 30

# Tạo thư mục logs nếu chưa có
LOG_DIR = "/app/logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "app_log.log")
# ================================ #

# ============ Logging Setup ============ #
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Clear existing handlers
logger.handlers.clear()

# Ghi vào logfile
file_handler = logging.FileHandler(LOG_FILE, mode='a')
file_handler.setLevel(logging.INFO)

# Ghi stdout
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)

# Ghi stderr (thường dùng để log lỗi và traceback)
stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setLevel(logging.ERROR)

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)

# Gửi tới syslog (nếu có)
try:
    syslog_handler = SysLogHandler(address="/dev/log")
    syslog_handler.setLevel(logging.INFO)
    logger.addHandler(syslog_handler)
except Exception as e:
    logger.warning(f"Không thể kết nối syslog: {e}")

# Format chung cho tất cả handler
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
for handler in logger.handlers:
    handler.setFormatter(formatter)

# Log startup message
logger.info("=== APPLICATION STARTING ===")
logger.info(f"Log file: {LOG_FILE}")
# ========================================= #

# Load model
model = joblib.load(MODEL_PATH)
logger.info("Model loaded successfully")

# Prometheus metrics
INFERENCE_TIME = Summary("inference_time_seconds", "Time taken for inference")
CONFIDENCE_SCORE_SUM = Counter("confidence_score_sum", "Sum of confidence scores")
CONFIDENCE_SCORE_COUNT = Counter("confidence_score_count", "Count of confidence scores")

# FastAPI app
app = FastAPI()
Instrumentator().instrument(app).expose(app)

# Input schema
class InputData(BaseModel):
    data: List[float]

@app.post("/predict")
def predict(input_data: InputData):
    try:
        if len(input_data.data) != EXPECTED_NUM_FEATURES:
            msg = f"Expected {EXPECTED_NUM_FEATURES} features, but got {len(input_data.data)}"
            logger.warning(msg)
            raise HTTPException(status_code=400, detail=msg)

        X = np.array([input_data.data])
        start = time.time()
        with INFERENCE_TIME.time():
            y_pred = model.predict(X)
            proba = model.predict_proba(X)  # <-- lấy xác suất dự đoán
        end = time.time()

        confidence = float(np.max(proba))  # <-- xác suất cao nhất

        CONFIDENCE_SCORE_SUM.inc(confidence)
        CONFIDENCE_SCORE_COUNT.inc()

        logger.info(f"Prediction done. Output={y_pred[0]}, Confidence={confidence:.2f}, Time={end - start:.4f}s")

        return {
            "prediction": int(y_pred[0]),
            "confidence": round(confidence, 2),
            "inference_time": round(end - start, 4)
        }

    except Exception as e:
        logger.exception("Prediction error")
        raise HTTPException(status_code=500, detail=f"Lỗi khi xử lý dữ liệu: {str(e)}")

@app.get("/health")
def health_check():
    logger.info("Health check accessed")
    return {"status": "ok"}

@app.get("/error500")
def error_500():
    logger.error("Error 500 endpoint accessed")
    raise HTTPException(status_code=500, detail="Internal Server Error for testing")

# ============ Global Exception Handlers ============ #

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTPException: status_code={exc.status_code}, detail={exc.detail}")
    return await http_exception_handler(request, exc)

@app.exception_handler(Exception)
async def all_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=5000)