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
