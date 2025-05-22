## Автотесты для сайта Restful-booker

[Restful-booker](https://restful-booker.herokuapp.com/)

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
<img src="media/icons/python.svg" width="50">  <img src="media/icons/pytest.png" width="50"> <img src="media/icons/pydantic.png" width="50"> <img src="media/icons/jenkins.png" width="50"> <img src="media/icons/test_ops.png" width="50"> <img src="media/icons/allure_report.png" width="50"> <img src="media/icons/tg.png" width="50">

- Язык программирования `Python`
- Фреймворк модульного тестирования `Pytest`
- Фреймворк для создания моделей тестирования `Pydantic`
- Выполнение удаленного запуска тестов с помощью `Jenkins`
- Инструмент для сбора и хранения статистики тестов `Allure TestOps`
- Фреймворки для сбора отчетности и хранения файлов тестирования `Allure Report`
- - Краткие отчеты в `Telegram` отправляет `Telegram Bot`

---

### Локальный запуск

Перед запуском в корне проекта создать файл .env с содержимым:

```
BOOKER_USERNAME="your_username"
BOOKER_PASSWORD="your_password"
```

Для локального запуска необходимо выполнить:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```

Для локального получения отчета необходимо выполнить:

```
allure.bat serve tests/allure-results
```

## Пример локального отчета о прохождении api-тестов

<img src="media/images/allure_2.png">

Детальная информация с шагами отображается в разделе `Suites`

<img src="media/images/allure_1.png">

---
### Удаленный запуск тестов выполняется в Jenkins
Посмотреть и запустить можно на странице проекта в [Jenkins](https://jenkins.autotests.cloud/job/api_tests_booking/).

Для запуска тестов необходимо:
1. Перейти на [проект](https://jenkins.autotests.cloud/job/api_tests_booking/)
2. Нажать на кнопку `Build now`
3. Дождаться окончания тестирования
4. Нажать на кнопку `Allure Report` <img src="media/icons/allure_report.png" width="15">

Откроется страница отчета

<img src="media/images/allure_report1.png">

Детальная информация с шагами и аттачментами отображается в разделе `Suites`

<img src="media/images/allure_report2.png">

### Статистика отчета хранится в Allure TestOps
Последний отчет можно посмотреть по [ссылке](https://allure.autotests.cloud/launch/46489)  
Для просмотра статистики после запуска в Jenkins в шаге 4 необходимо нажать на кнопку `Allure TestOps` <img src="media/icons/test_ops.png" width="15">

<img src="media/images/testops1.png">

Детальная информация по тест-кейсам

<img src="media/images/testops2.png">

Дашборд со статистикой и графиками запусков

<img src="media/images/testops3.png">


### Отчет о результатах тестирования в Telegram
Отчеты приходят в канал [Allure_channel](https://t.me/Allure_channel_autotests)

<img src="media/images/allure_tg.png">









