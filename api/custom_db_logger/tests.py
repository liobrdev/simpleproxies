import logging

from django.conf import settings
from django.core import mail
from django_redis import get_redis_connection

from rest_framework.test import APITestCase

from custom_db_logger.models import StatusLog
from custom_db_logger.serializers import StatusLogSerializer
from custom_db_logger.utils import LogLevels
from proxies.utils import ProxyCommands
from utils.testing import create_superuser, log_msg_regex


class DatabaseLoggerTest(APITestCase):
    databases = '__all__'

    def setUp(self):
        self.superuser = create_superuser()
        self.logger = logging.getLogger('proxies')

    def tearDown(self):
        get_redis_connection('default').flushall()

    def test_exception(self):
        exc_message = 'Exception Message!'

        try:
            raise Exception(exc_message)
        except Exception as e:
            self.logger.exception(exc_message, exc_info=e, extra={
                'command': ProxyCommands.GET_PROXIES,
            })

        self.assertEqual(StatusLog.objects.count(), 1)
        instance = StatusLog.objects.latest('created_at')
        log = StatusLogSerializer(instance).data
        self.assertRegex(log['msg'], log_msg_regex(exc_message, LogLevels.ERROR))
        self.assertEqual(log['level'], LogLevels.ERROR)
        self.assertEqual(log['command'], ProxyCommands.GET_PROXIES)
        self.assertIsNotNone(log['trace'])
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject,
            f'{settings.EMAIL_SUBJECT_PREFIX}ERROR: Exception Message!')
        self.assertListEqual(mail.outbox[0].to, ['contact@simpleproxies.app'])
