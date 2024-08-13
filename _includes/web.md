| Description | Site |
| ---- | ---- |
{% assign skills = site.data.skills.web | "title" -%}
{% for skill in skills -%}
| [{{skill.title}}] | ({{skill.level}}) |
{% endfor %}