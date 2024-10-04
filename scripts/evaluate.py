# evaluate.py
import pandas as pd
import mlflow
import argparse
from sklearn.metrics import ndcg_score
import joblib
from file_manager import FileManager

# Функция для оценки модели
def evaluate_model(input_path, model_path):
    # Логирование в MLflow
    with mlflow.start_run():
        print(f"Reading data from {input_path}")
        # Чтение данных и модели
        df = pd.read_parquet(input_path)
        
        print(f"Loading model from {model_path}")
        model = joblib.load(model_path)
        
        print("Splitting data into features and target...")
        # Выделение признаков и целевой переменной
        X = df.drop(columns=['user_id', 'products'])
        y = df['products']
        
        print("Making predictions...")
        # Оценка качества модели
        y_pred = model.predict(X)
        if len(y_pred.shape) != 1 or len(y) != len(y_pred):
            raise ValueError("The model output does not align with the expected ranking. Verify the output format of the predict method.")
        score = ndcg_score([y], [y_pred])
        
        print(f"NDCG Score: {score}")
        # Логирование метрик
        mlflow.log_metric("ndcg_score", score)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str, required=True, help="Path to the preprocessed data file")
    parser.add_argument("--model_path", type=str, required=True, help="Path to the saved model file")
    args = parser.parse_args()
    print(f"Starting evaluation with input: {args.input_path} and model: {args.model_path}")
    evaluate_model(args.input_path, args.model_path)