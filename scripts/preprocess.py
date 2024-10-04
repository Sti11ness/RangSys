# preprocess.py
import pandas as pd
import numpy as np
import mlflow
import argparse
from file_manager import FileManager

# Функция для предобработки данных
def preprocess_data(input_path, output_path):
    # Логирование в MLflow
    with mlflow.start_run():
        print(f"Reading data from {input_path}")
        # Чтение данных
        df = pd.read_parquet(input_path)
        mlflow.log_param("input_path", input_path)
        
        print("Converting date column...")
        # Преобразование даты
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df.dropna(subset=['date'], inplace=True)
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        df['day'] = df['date'].dt.day
        df['hour'] = df['date'].dt.hour
        df.drop(columns=['date'], inplace=True)
        print("Handling missing values...")
        # Обработка пропущенных значений
        df.fillna({'action': 0, 'sub_action': 0, 'url': 'no_information'}, inplace=True)
        df['products'] = df['products'].apply(lambda x: [] if pd.isna(x) else x)
        
        print(f"Saving preprocessed data to {output_path}")
        # Логирование артефактов предобработки
        mlflow.log_artifact(output_path)
        
        # Сохранение предобработанных данных
        df.to_parquet(output_path, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str, required=True, help="Path to the input data file")
    parser.add_argument("--output_path", type=str, required=True, help="Path to save the preprocessed data")
    args = parser.parse_args()
    print(f"Starting preprocessing with input: {args.input_path} and output: {args.output_path}")
    file_manager = FileManager(base_dir=os.path.dirname(os.path.abspath(__file__)))
    file_manager.ensure_directory(os.path.dirname(args.output_path))
    preprocess_data(args.input_path, args.output_path)