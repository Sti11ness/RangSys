import subprocess
import os

def run_command(command):
    print(f"Running command: {command}")
    process = subprocess.Popen(command, shell=True)
    process.communicate()
    if process.returncode != 0:
        raise Exception(f"Command failed: {command}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    preprocess_script = os.path.join(base_dir, "scripts", "preprocess.py")
    train_script = os.path.join(base_dir, "scripts", "train.py")
    evaluate_script = os.path.join(base_dir, "scripts", "evaluate.py")

    input_data = os.path.join(base_dir, "data", "train_actions.pq")
    preprocessed_data = os.path.join(base_dir, "data", "preprocessed_data.pq")
    trained_model = os.path.join(base_dir, "models", "trained_model.pkl")

    run_command(f"python {preprocess_script} --input_path {input_data} --output_path {preprocessed_data}")
    run_command(f"python {train_script} --input_path {preprocessed_data} --model_output_path {trained_model}")
    run_command(f"python {evaluate_script} --input_path {preprocessed_data} --model_path {trained_model}")