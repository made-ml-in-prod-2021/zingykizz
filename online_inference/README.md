## Проект online_inference

Сборка докер-образа:
~~~
docker build -t zingykizz/online_inference:v1 .
~~~

Запуск докер-контейнера:
~~~
docker run --name online_inference_container -p 8000:8000 zingykizz/online_inference:v1
~~~

Пуш в докер-хаб:
~~~
docker push zingykizz/online_inference:v1
~~~

Пулл из докер-хаба:
~~~
docker pull zingykizz/online_inference:v1
~~~
