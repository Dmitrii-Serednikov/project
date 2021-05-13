{% extends 'flatpages/default.html' %}
{% block title %} TITLE 2 (Contacts) {% endblock title %}
{% block content %}
<h1>Contact us</h1>
{{ flatpage.content }}
<br>
{{ flatpage.content }}
{% endblock content %}
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %} {% endblock title %}</title>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Django flatpages — {% block title %} {% endblock title %}</title>

  <!-- Bootstrap core CSS -->
  <link href="{% static 'vendor/bootstrap/css/bootstrap.min.css' %}" rel="stylesheet">

</head>

<body>
    <a href="/contacts">Contacts</a>
    <a href="/about">About</a>
    <hr>

    {% block content %}
    {{ flatpage.content }}
    {% endblock content %}

  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
    <div class="container">
      <a class="navbar-brand" href="#">Django flatpages</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home
              <span class="sr-only">(current)</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/about/">About</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/contacts/">Contact</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/hidden/">Hidden</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Content -->
  <div class="container">
    <div class="row">
      <div class="col-lg-12 text-center">
       {% block content %}
       {{ flatpage.content }}
       {% endblock content %}
      </div>
    </div>
  </div>

  <!-- Bootstrap core JavaScript -->
  <script src="{% static 'vendor/jquery/jquery.slim.min.js' %}"></script>
  <script src="{% static 'vendor/bootstrap/js/bootstrap.bundle.min.js' %}"></script>

</body>

</html>