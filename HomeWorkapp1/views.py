from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    code = """
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Главная</title>
</head>
<body>
  <h1>Главная страница!</h1>
</body>
</html>
 """
    return HttpResponse(code)


def about(request):
    code = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>О нас</title>
    </head>
    <body>
      <h1>Страница о нас!</h1>
    </body>
    </html>
     """
    return HttpResponse(code)