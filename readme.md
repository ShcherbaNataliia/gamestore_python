Для створення нових шаблонів (templates) використовуйте базовий шаблон base.html.
Це автоматично додасть навігаційну панель та підключить стилі. Приклад використання:

<!-- example.html -->
{% extends 'base.html' %}

{% block title %} Example title {% endblock %}

{% block content %}
<h2>Додайте контент в цей блок</h2>
<!-- page content -->
{% endblock %}

