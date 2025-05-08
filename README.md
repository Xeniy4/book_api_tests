## Простые тесты для сайта Restful-booker

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
 <img src="media/icons/python.svg" width="50">  <img src="media/icons/pytest.png" width="50"> <img src="media/icons/pydantic.png" width="50">  <img src="media/icons/allure_report.png" width="50"> <img src="media/icons/allure_testops.png" width="50"> <img src="media/icons/tg.png" width="50">  


- Язык программирования `Python`
- Фреймворк для создания моделей тестирования `Pydantic`
- Фреймворк модульного тестирования `Pytest`
- Фреймворки для сбора отчетности и хранения файлов тестирования `Allure Report`
- Инструмент для сбора и хранения статистики тестов `Allure TestOps`
- Краткие отчеты в `Telegram` отправляет `Telegram Bot`

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

<img src="media/images/allure1.png">

Детальная информация с шагами и аттачментами отображается в разделе `Suites`

<img src="media/images/allure2.png">

---
### Статистика отчета хранится в Allure TestOps
Последний отчет можно посмотреть на сайте [Allure TestOps](https://allure.autotests.cloud/launch/45643/?treeId=0)  
Для просмотра статистики после запуска в Jenkins в шаге 4 необходимо нажать на кнопку `Allure TestOps` <img src="media/icons/allure_testops.png" width="15">

<img src="media/images/testops1.png">

Детальная информация по тест-кейсам

<img src="media/images/testops2.png">


---
### Отчет о результатах тестирования в Telegram
Отчеты приходят в канал [Allure_channel](https://t.me/Allure_channel_autotests)

<img src="media/images/tg.png">








