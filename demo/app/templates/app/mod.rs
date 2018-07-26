{% extends "app/base.rs" %}
{% block content %}
{% autoescape off %}
pub mod connections {
    {% for database in app_data.databases %}
        {% include "app/database_mod.rs" with database=database %}    


    {% endfor %} 
}

pub mod django_apps {

}
{% endautoescape %}
{% endblock %}
