
# Practical task for Nerdysoft

В ходе выполнения задания были использовано: 
- Flask
- Swagger 
- SQLAlchemy
- PostgreSQL

Помимо этого, из стандартной библиотеки были использованы модули
 - json 
 - collections.Counter
 
 Приложение было запущено на облачной платформе Heroku и 
доступно по адрессу https://still-cove-38481.herokuapp.com/apidocs/
(может долго загружаться при первом подключении)

## Пункты задания
1) Замена словара новым происходит по endpoint-у
```PUT /vocabulary/words  ```
2) Добавление нового словаря к уже существующему 
```POST /vocabulary/words  ```
3) Добавление отдельного слова к словарю 
```POST /vocabulary/word  ```
4) Подсчет количества слов, которые содержат указанные буквы
```GET /vocabulary/word/count  ```
5) Получение всех слов, которые содержат указанные буквы, списком
```GET /vocabulary/wordі  ```
## Для запуска локально

Скопировать проект 

```bash
  git clone https://github.com/dolho/practical_task_nerdysoft
```

Зайти в директорию проекта

```bash
  cd practical_task_nerdysoft
```

Установить зависимости

```bash
  pip install -r requirements.txt

```

Выполнить

```bash
  export FLASK_APP=server
  export FLASK_ENV=development
```
Создать и заполнить .env файл в формате
```bash
USER_PROD=your_user
PASSWORD=your_password
DB=your_db
HOST=your_db_host
```

Выполнить 
```bash
   flask setup
```


Запустить сервер

```bash
  gunicorn server:app --preload
```

