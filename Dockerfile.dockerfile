# Базовый образ Python
FROM python:3.12
# Устанавливаем django и bootstrap
RUN pip install django && pip install django-bootstrap4
# Копируем файлы сайта
COPY . /Site/
# Рабочая директория
WORKDIR /Site/
# Открываем порт
EXPOSE 8000
# Команда для запуска
CMD ["python","manage.py","runserver","0.0.0.0:8000"]

