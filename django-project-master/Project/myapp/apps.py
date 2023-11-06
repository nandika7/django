from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    # {% if {{outcome}} == 0 %}
    # Your diabetes results came back positive
    # {% else %}
    # Your diabetes results came back negative