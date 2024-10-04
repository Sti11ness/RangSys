# Dockerfile для контейнеризации проекта
FROM python:3.8-slim

# Установка зависимостей
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копирование всех файлов проекта в контейнер
COPY . .

# Команда по умолчанию для запуска пайплайна
CMD ["bash", "workflow/run_pipeline.sh"]