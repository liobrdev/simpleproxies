from django.test import override_settings
from django_redis import get_redis_connection

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from custom_db_logger.models import StatusLog
from utils.testing import ip_address_regex


@override_settings(DJANGO_ENV='test')
class AuthenticationTest(APITestCase):
    databases = '__all__'

    def tearDown(self):
        get_redis_connection('default').flushall()

    def test_successful_get_proxies(self):
        response = self.client.get(reverse('proxies'))
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        for proxy in response.data:
            self.assertIsInstance(proxy, str)
            self.assertRegex(proxy, ip_address_regex())
        self.assertEqual(StatusLog.objects.count(), 0)
