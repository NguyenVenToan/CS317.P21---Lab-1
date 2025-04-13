import os
from metaflow import FlowSpec, step, Parameter
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import mlflow
import mlflow.sklearn
import json

class BreastCancerPipeline(FlowSpec):

    test_size = Parameter("test_size", default=0.2)
    random_state = Parameter("random_state", default=42)
    n_estimators = Parameter("n_estimators", default=100)
    max_depth = Parameter("max_depth", default=5)
    svc_kernel = Parameter("svc_kernel", default="rbf")
    c_logreg = Parameter("c_logreg", default=1.0)
    hyperparameter_tuning = Parameter("hyperparameter_tuning", default=True)

    @step
    def start(self):
        self.data_path = "breast-cancer.csv"
        assert os.path.exists(self.data_path), f"{self.data_path} not found!"
        self.df = pd.read_csv(self.data_path)
        self.next(self.preprocessing)

    @step
    def preprocessing(self):
        df = self.df
        df = df.drop(columns=["id", "Unnamed: 32"], errors="ignore")
        df["diagnosis"] = df["diagnosis"].map({"M": 1, "B": 0})
        self.X = df.drop("diagnosis", axis=1)
        self.y = df["diagnosis"]
        print(f"X shape: {self.X.shape}")
        print(f"y shape: {self.y.shape}")
        print(f"y value counts:\n{self.y.value_counts()}")
        self.next(self.split)

    @step
    def split(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=self.test_size, random_state=self.random_state
        )
        self.next(self.train_model)

    @step
    def train_model(self):
        mlflow.set_experiment("breast_cancer_experiment")

        with mlflow.start_run() as run:
            mlflow.log_param("n_estimators", self.n_estimators)
            mlflow.log_param("max_depth", self.max_depth)
            mlflow.log_param("test_size", self.test_size)
            mlflow.log_param("random_state", self.random_state)
            mlflow.log_param("dataset_link", "https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data")
            mlflow.log_param("dataset_version", "v2")

            # Log dataset CSV as artifact
            dataset_json = {
                "dataset_link": "https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data",
                "dataset_version": "v2"
            }
            dataset_json_path = "dataset_info.json"
            with open(dataset_json_path, "w") as f:
                json.dump(dataset_json, f)
            
            mlflow.log_artifact(self.data_path)  # Log the CSV dataset
            mlflow.log_artifact(dataset_json_path)  # Log the dataset_info.json file

            # Tuning RandomForestClassifier (GridSearchCV)
            if self.hyperparameter_tuning:
                rf_param_grid = {
                    "n_estimators": [50, 100, 200],
                    "max_depth": [5, 10, None]
                }
                grid_search_rf = GridSearchCV(RandomForestClassifier(random_state=self.random_state), rf_param_grid, cv=5)
                grid_search_rf.fit(self.X_train, self.y_train)
                self.rf_model = grid_search_rf.best_estimator_
                mlflow.sklearn.log_model(self.rf_model, "random_forest_model")
                mlflow.log_param("best_rf_params", grid_search_rf.best_params_)
            else:
                self.rf_model = RandomForestClassifier(
                    n_estimators=self.n_estimators, max_depth=self.max_depth, random_state=self.random_state
                )
                self.rf_model.fit(self.X_train, self.y_train)
                mlflow.sklearn.log_model(self.rf_model, "random_forest_model")
                mlflow.log_param("model", "RandomForest")

            # Tuning SVM (GridSearchCV)
            if self.hyperparameter_tuning:
                svc_param_grid = {
                    "C": [0.1, 1, 10],
                    "kernel": [self.svc_kernel, "linear", "poly"]
                }
                grid_search_svc = GridSearchCV(SVC(), svc_param_grid, cv=5)
                grid_search_svc.fit(self.X_train, self.y_train)
                self.svc_model = grid_search_svc.best_estimator_
                mlflow.sklearn.log_model(self.svc_model, "svc_model")
                mlflow.log_param("best_svc_params", grid_search_svc.best_params_)
            else:
                self.svc_model = SVC(kernel=self.svc_kernel, random_state=self.random_state)
                self.svc_model.fit(self.X_train, self.y_train)
                mlflow.sklearn.log_model(self.svc_model, "svc_model")
                mlflow.log_param("model", "SVM")

            # Tuning Logistic Regression (GridSearchCV)
            if self.hyperparameter_tuning:
                logreg_param_grid = {
                    "C": [0.1, 1, 10]
                }
                grid_search_logreg = GridSearchCV(LogisticRegression(random_state=self.random_state), logreg_param_grid, cv=5)
                grid_search_logreg.fit(self.X_train, self.y_train)
                self.logreg_model = grid_search_logreg.best_estimator_
                mlflow.sklearn.log_model(self.logreg_model, "logreg_model")
                mlflow.log_param("best_logreg_params", grid_search_logreg.best_params_)
            else:
                self.logreg_model = LogisticRegression(C=self.c_logreg, random_state=self.random_state)
                self.logreg_model.fit(self.X_train, self.y_train)
                mlflow.sklearn.log_model(self.logreg_model, "logreg_model")
                mlflow.log_param("model", "LogisticRegression")

            self.run_id = run.info.run_id
        self.next(self.evaluate)

    @step
    def evaluate(self):
        # Prediction and evaluation for all models
        y_pred_rf = self.rf_model.predict(self.X_test)
        y_pred_svc = self.svc_model.predict(self.X_test)
        y_pred_logreg = self.logreg_model.predict(self.X_test)

        # Metrics for Random Forest
        acc_rf = accuracy_score(self.y_test, y_pred_rf)
        precision_rf = precision_score(self.y_test, y_pred_rf)
        recall_rf = recall_score(self.y_test, y_pred_rf)
        f1_rf = f1_score(self.y_test, y_pred_rf)

        # Metrics for SVM
        acc_svc = accuracy_score(self.y_test, y_pred_svc)
        precision_svc = precision_score(self.y_test, y_pred_svc)
        recall_svc = recall_score(self.y_test, y_pred_svc)
        f1_svc = f1_score(self.y_test, y_pred_svc)

        # Metrics for Logistic Regression
        acc_logreg = accuracy_score(self.y_test, y_pred_logreg)
        precision_logreg = precision_score(self.y_test, y_pred_logreg)
        recall_logreg = recall_score(self.y_test, y_pred_logreg)
        f1_logreg = f1_score(self.y_test, y_pred_logreg)

        # Confusion matrices
        cm_rf = confusion_matrix(self.y_test, y_pred_rf)
        cm_svc = confusion_matrix(self.y_test, y_pred_svc)
        cm_logreg = confusion_matrix(self.y_test, y_pred_logreg)

        # Classification Reports for all models
        report_rf = classification_report(self.y_test, y_pred_rf, output_dict=True)
        report_svc = classification_report(self.y_test, y_pred_svc, output_dict=True)
        report_logreg = classification_report(self.y_test, y_pred_logreg, output_dict=True)

        # Save classification reports as JSON
        with open("classification_report_rf.json", "w") as f:
            json.dump(report_rf, f)
        with open("classification_report_svc.json", "w") as f:
            json.dump(report_svc, f)
        with open("classification_report_logreg.json", "w") as f:
            json.dump(report_logreg, f)

        # Plot confusion matrix
        plt.figure(figsize=(12, 8))
        for i, cm in enumerate([cm_rf, cm_svc, cm_logreg]):
            plt.subplot(1, 3, i + 1)
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=[0, 1], yticklabels=[0, 1])
            plt.xlabel('Predicted')
            plt.ylabel('Actual')
            plt.title(f"Confusion Matrix {['RF', 'SVM', 'LogReg'][i]}")
            plt.tight_layout()

        plt.savefig("confusion_matrices.png")
        plt.close()

        with mlflow.start_run(run_id=self.run_id):
            # Log accuracy, precision, recall, and F1-score for each model
            mlflow.log_metric("accuracy_rf", acc_rf)
            mlflow.log_metric("precision_rf", precision_rf)
            mlflow.log_metric("recall_rf", recall_rf)
            mlflow.log_metric("f1_rf", f1_rf)

            mlflow.log_metric("accuracy_svc", acc_svc)
            mlflow.log_metric("precision_svc", precision_svc)
            mlflow.log_metric("recall_svc", recall_svc)
            mlflow.log_metric("f1_svc", f1_svc)

            mlflow.log_metric("accuracy_logreg", acc_logreg)
            mlflow.log_metric("precision_logreg", precision_logreg)
            mlflow.log_metric("recall_logreg", recall_logreg)
            mlflow.log_metric("f1_logreg", f1_logreg)

            mlflow.log_artifact("confusion_matrices.png")
            mlflow.log_artifact("classification_report_rf.json")
            mlflow.log_artifact("classification_report_svc.json")
            mlflow.log_artifact("classification_report_logreg.json")

        print(f"Random Forest Accuracy: {acc_rf}, Precision: {precision_rf}, Recall: {recall_rf}, F1: {f1_rf}")
        print(f"SVM Accuracy: {acc_svc}, Precision: {precision_svc}, Recall: {recall_svc}, F1: {f1_svc}")
        print(f"Logistic Regression Accuracy: {acc_logreg}, Precision: {precision_logreg}, Recall: {recall_logreg}, F1: {f1_logreg}")

        self.next(self.end)

    @step
    def end(self):
        print("Pipeline complete.")

if __name__ == "__main__":
    BreastCancerPipeline()
