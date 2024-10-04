@echo off

:: Создание структуры проекта recommender_system_project
set BASE_DIR=recommender_system_project

:: Создание основных директорий
mkdir %BASE_DIR%
mkdir %BASE_DIR%\data
mkdir %BASE_DIR%\scripts
mkdir %BASE_DIR%\models
mkdir %BASE_DIR%\workflow

:: Создание файлов
cd %BASE_DIR%
copy NUL README.md
copy NUL requirements.txt
copy NUL Dockerfile

cd scripts
copy NUL file_manager.py
copy NUL preprocess.py
copy NUL train.py
copy NUL evaluate.py
copy NUL run_pipeline.py

cd ..\workflow
copy NUL run_pipeline.sh
copy NUL Snakefile

:: Возврат в базовую директорию
cd ..

:: Сообщение об успешном создании структуры проекта
echo Project structure created successfully.