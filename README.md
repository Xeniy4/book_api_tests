## Автотесты для сайта Restful-booker

[Arzamas](https://restful-booker.herokuapp.com/)

---
 
<img src="media/images/booker.png">


Список проведенных проверок:
- Авторизация пользователя
- Создания заказа
- Редактирование заказа
- Удаление заказа
- Просмотр информации по заказу

---

Проект реализован с использованием актуальных инструментов:  
 <img src="media/icons/python.svg" width="50">  <img src="media/icons/pytest.png" width="50"> <img src="media/icons/pydantic.png" width="50">  <img src="media/icons/allure_report.png" width="50"> 


- Язык программирования `Python`
- Фреймворк для создания моделей тестирования `Pydantic`
- Фреймворк модульного тестирования `Pytest`
- Фреймворки для сбора отчетности и хранения файлов тестирования `Allure Report`

---

### Локальный запуск
Перед запуском в корне проекта создать файл .env с содержимым:
```
BOOKER_USERNAME="admin"
BOOKER_PASSWORD="password123"
```

Для локального запуска необходимо выполнить:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```
Для получения отчета необходимо выполнить:
```
allure.bat serve tests/allure-results
```

## Пример отчета о прохождении api-тестов

<img src="media/images/allure_2.png">

Детальная информация с шагами и аттачментами отображается в разделе `Suites`

<img src="media/images/allure_1.png">








