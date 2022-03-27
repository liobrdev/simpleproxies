from django.db.models.enums import TextChoices


class ProxyCommands(TextChoices):
    GET_PROXIES = 'get_proxies'
    NO_COMMAND = 'no_command'
