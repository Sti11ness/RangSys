# file_manager.py
import os
import shutil

class FileManager:
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def ensure_directory(self, relative_path):
        path = os.path.join(self.base_dir, relative_path)
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def copy_file(self, src, dest):
        shutil.copy2(src, dest)

    def delete_file(self, file_path):
        if os.path.exists(file_path):
            os.remove(file_path)

    def list_files(self, relative_path):
        path = os.path.join(self.base_dir, relative_path)
        return os.listdir(path) if os.path.exists(path) else []
