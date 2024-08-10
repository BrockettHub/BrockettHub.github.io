| Skill | Level |
| ---- | ---- |
{% assign skills = site.data.skills.technical | "title" -%}
{% for skill in skills -%}
| {{skill.title}} | {{skill.level}} |
{% endfor %}