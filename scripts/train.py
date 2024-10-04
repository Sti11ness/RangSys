# train.py
import pandas as pd
import mlflow
import mlflow.sklearn
import argparse
from sklearn.model_selection import train_test_split
from lightgbm import LGBMRanker
import joblib
from file_manager import FileManager

# Функция для обучения модели
def train_model(input_path, model_output_path):
    # Логирование в MLflow
    with mlflow.start_run():
        print(f"Reading data from {input_path}")
        # Чтение данных
        df = pd.read_parquet(input_path)
        
        print("Splitting data into features and target...")
        # Выделение признаков и целевой переменной
        X = df.drop(columns=['user_id', 'products'])
        y = df['products']  # Здесь предполагаем, что целевой признак - товары, которые пользователь покупает
        
        print("Splitting data into training and testing sets...")
        # Разделение на обучающую и тестовую выборки
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        print("Training the model...")
        # Обучение модели LightGBM Ranker
        model = LGBMRanker()
        model.fit(X_train, y_train, group=[len(X_train)])
        
        # Логирование параметров модели и метрик
        mlflow.log_param("model", "LGBMRanker")
        mlflow.sklearn.log_model(model, "model")
        
        print(f"Saving trained model to {model_output_path}")
        # Сохранение модели
        joblib.dump(model, model_output_path)
        mlflow.log_artifact(model_output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str, required=True, help="Path to the preprocessed data file")
    parser.add_argument("--model_output_path", type=str, required=True, help="Path to save the trained model")
    args = parser.parse_args()
    print(f"Starting training with input: {args.input_path} and output: {args.model_output_path}")
    file_manager = FileManager(base_dir=os.path.dirname(os.path.abspath(__file__)))
    file_manager.ensure_directory(os.path.dirname(args.model_output_path))
    train_model(args.input_path, args.model_output_path)