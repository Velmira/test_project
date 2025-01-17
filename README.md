# test_project

Проект по тестированию API сервиса Gectaro(https://gectaro.com/) и UI сайта https://cryptoexchange.com/
```
## Для локального запуска тестов необходимо:
```
Клонировать репозиторий и перейти в него в командной строке:
```
https://github.com/Velmira/test_project.git
```
Создать и активировать виртуальное окружение:
```
python3 -m venv venv
```
- Для Linux/macOS:
    ```
    source venv/bin/activate
    ```
- Для Windows:
    ```
    source venv/scripts/activate
    ```
Обновить pip:
```
pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Запуск всех тестов:
```
pytest .
```
Запуск API тестов:
```
pytest API/tests
```
Запуск UI тестов (настройка conftest.py предусмотрена для удаленного запуска
через Selenoid - Selenoid должен быть предварительно настроен и запущен):
```
pytest UI/tests
```
Запуск в многопоточном режиме:
```
pytest . -n {n}
```
Для удаленного запуска из Jenkins в проекте присутствует Jenkinsfile
