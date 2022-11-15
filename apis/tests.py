from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from hello.models import Helloer


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.helloer = Helloer(
            name="Parham",
            family="Alvani",
            age=30,
        )
        cls.helloer.save()

    def test_api_listview(self):
        response = self.client.get(reverse("helloer_list"))
        # response code should be 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # there should be only one helloer in the database
        self.assertEqual(Helloer.objects.count(), 1)

        helloers = response.json()
        self.assertEqual(len(helloers), 1)
        self.assertEqual(helloers[0]["name"], self.helloer.name)
        self.assertEqual(helloers[0]["family"], self.helloer.family)
        self.assertEqual(helloers[0]["age"], self.helloer.age)
