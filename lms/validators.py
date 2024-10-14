from rest_framework.serializers import ValidationError


def validate_description_links(value):
    """Проверяет на содержание ссылок на запрещенные сайты"""
    value = value.split()
    for word in value:
        if word.startswith("https://www.youtube.com/") or word.startswith("www.youtube.com"):
            raise ValidationError("Нельзя включать ссылки на запрещённые сайты")
