import re

from django.contrib.auth import get_user_model
from django.db import connections

from custom_db_logger.utils import LogLevels


test_superuser = {
    'username': 'Super User',
    'email': 'superuser@email.com',
    'password': 'Admin!123',
}


def create_superuser(data=test_superuser):
    return get_user_model().objects.create_superuser(**data)


def force_drop_test_databases():
    test_dbs = [
        {
            'db_alias': 'default',
            'db_name': 'test_simpleproxies_logger_db',
        },
    ]

    for test_db in test_dbs:
        db_alias = test_db['db_alias']
        with connections[db_alias].cursor() as cursor:
            db_name = test_db['db_name']
            cursor.execute(
                f'ALTER DATABASE {db_name} CONNECTION LIMIT 0')
            cursor.execute("""
                SELECT pg_terminate_backend(pid)
                FROM pg_stat_activity
                WHERE datname = %s;
            """, [db_name,])
            cursor.execute(f'DROP DATABASE {db_name}')


def log_msg_regex(msg, log_level=None):
    if log_level:
        level_regex = re.escape(LogLevels(log_level).name)
    else:
        level_regex = r'(NOTSET|DEBUG|INFO|WARNING|ERROR|CRITICAL)'
    return (
        r'^' + level_regex +
        r' [\d]{4}-[\d]{2}-[\d]{2} [\d]{2}:[\d]{2}:[\d]{2},[\d]{3} .* line [\d]{0,6} in [\w-]*: ' +
        re.escape(msg) + r'$')


def ip_address_regex():
    ip_field = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'

    return (
        r'^' + ip_field + r'\.' + ip_field + r'\.' + ip_field + r'\.' +
        ip_field + r':[\d]{2,5}$')
