{% extends "app/base.rs" %}
{% load convert %}
{% block content %}
{% autoescape off %}
pub mod connections {
    {% for database in app_data.databases %}
        {% include "app/database_mod.rs" with database=database %}    
    {% endfor %} 
}

pub mod django_apps {
    {% for app in app_data.apps %}
    pub mod {{ app.name|name4rust }} {
        
        pub mod schema {

            {% for model in app.models %}
                {{ model.render }}
            {% endfor %}
        }
    }
    {% endfor %}
}
{% endautoescape %}
{% endblock %}
