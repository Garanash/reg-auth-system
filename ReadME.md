# Система аутентификации пользователей АГБ

## для запуска:
### установить виртуальное окружение
```cmd
python -m venv venv
source venv/bin/activate
# или venv/Scripts/activate на Windows
```
### загрузить систему контроля зависимостей и установить зависимости
```commandline
pip install poetry
poetry install --no-root
```
### Перейти в папку с файлом и запустить бэкенд
```commandline
cd backend
python main.py
```
### бекенд будет доступен на адресе: http://127.0.0.1:8001 
Доступны ручки на весь круд связанный с пользователем, при условии авторизации через пользователя.
тестовый пользователь:
- login: test
- password: test