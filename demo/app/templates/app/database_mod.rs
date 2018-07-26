{% load convert %}
pub mod {{ database.name|name4rust }} {
    {{ database.render }}
}
