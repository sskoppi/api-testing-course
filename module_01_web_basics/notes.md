# Занятие 1. Ответы Web3–Web12

## Web3
- Статус: 200
- Content-Type: application/json; charset=utf-8
- Пользователей в теле: 10
- Запрос со статусом ≠ 200: нет

## Web4
- Комментариев вернулось: 5
- У скольких postId = 5: у всех 5

  ## Web5
- Запрос: GET /albums/1/photos?limit=3
- Объектов в ответе: 50 (ожидалось 3, но сервер вернул весь альбом)
- id объектов: 1–50
- Вывод: параметр limit на этом эндпоинте не ограничил выдачу

  ## Web6
- GET /comments?postId=3 → 5 комментариев
- GET /comments?postId=4 → 5 комментариев
- Вывод: параметр postId фильтрует комментарии по номеру записи, к которой они относятся.

   ## Web7
- Гипотеза: параметр _limit ограничивает количество объектов в ответе до указанного числа.
- GET /posts?_limit=2 → 2 объекта
- GET /posts?_limit=7 → 7 объектов
- Вывод: гипотеза подтвердилась.

  ## Web9
- /users/2/posts → 10 объектов, id первого: 11
- /posts?userId=2 → 10 объектов, id первого: 11
- Вывод: это одни и те же данные, полученные двумя дорогами (через путь и через query).

  ## Web10
- GET /users/1 → 200
- GET /users/11 → 404
- GET /users/1?foo=bar → 200
- Вывод: ресурс ломает путь (несуществующий id → 404), а лишний query-параметр (foo=bar) на ресурс не влияет.

## Web11
- GET /users (Postman):
  - Content-Type: application/json; charset=utf-8
  - Content-Length: не указан (Transfer-Encoding: chunked)
- HTML-страница (любая в браузере):
  - Content-Type: text/html; charset=utf-8
- Вывод: у JSON и HTML разные Content-Type — браузер по нему понимает, как отображать данные.
  
## Web12
- GET /todos?limit=5&page=1 → 5 объектов, id первого: 1
- GET /todos?limit=5&page=2 → 5 объектов, id первого: 6
- Вывод: _page задаёт номер страницы: page=1 — первые 5 записей, page=2 — следующие 5.
