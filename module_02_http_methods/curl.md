# Занятие 2. Команды curl

## Met2. POST и PATCH

### Команда 1 — POST

```
curl -i -X POST https://jsonplaceholder.typicode.com/posts -H "Content-Type: application/json" -d "{\"title\": \"Мой пост\", \"body\": \"Текст\", \"userId\": 1}"
```

**Вывод:**

```
HTTP/1.1 201 Created
Content-Type: application/json; charset=utf-8
Content-Length: 85

{
  "title": "Мой пост",
  "body": "Текст",
  "userId": 1,
  "id": 101
}
```

### Команда 2 — PATCH

```
curl -i -X PATCH https://jsonplaceholder.typicode.com/users/1 -H "Content-Type: application/json" -d "{\"name\": \"Ada\"}"
```

**Вывод:**

```
HTTP/1.1 200 OK
Date: Thu, 08 Oct 2026 14:02:08 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 499
```


## Met8. curl: POST и GET

### Команда 1 — POST

```
curl -i -X POST https://jsonplaceholder.typicode.com/posts -H "Content-Type: application/json" -d "{\"title\": \"Мой пост\", \"body\": \"Текст\", \"userId\": 1}"
```

**Вывод:**

```
HTTP/1.1 201 Created
Content-Type: application/json; charset=utf-8
Content-Length: 85
...
```

### Команда 2 — GET

```
curl -i https://jsonplaceholder.typicode.com/users/3
```

**Вывод:**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 205
...
```

**Вопрос к себе.** Ключ `-i` показал заголовки ответа. Без него на экране осталось бы только тело JSON — и в багрепорте не было бы видно, какой статус и формат вернул сервер. Одного тела для воспроизведения бага мало: нужны метод, URL, тело запроса и заголовки ответа.


## Met9. Accept

### Команда 1 — с Accept

```
curl -i -H "Accept: application/json" https://jsonplaceholder.typicode.com/users/1
```

**Вывод:**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 509

{ "id": 1, "name": "Leanne Graham", ... }
```

### Команда 2 — без Accept

```
curl -i https://jsonplaceholder.typicode.com/users/1
```

**Вывод:**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 509

{ "id": 1, "name": "Leanne Graham", ... }
```

**Изменилось:** ничего — статус, заголовки и тело одинаковые.

**Вывод, смотрел ли сервер на Accept:** нет, сервер не читает Accept и всегда отдаёт JSON.

**Вопрос к себе.** Если по телу разницу не видно, где ещё в ответе она обязана проявиться: заголовок `Content-Type` объявляет формат тела. У обоих ответов он одинаковый — `application/json`, значит, сервер не переключался на другой формат.
