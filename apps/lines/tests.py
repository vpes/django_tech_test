# coding: utf8
from django.urls import reverse
from rest_framework.test import APITestCase

from apps.users.test import CustomUserTestMixin
from .factories import (LineFactory, RouteFactory)


class LineCreateTest(CustomUserTestMixin, APITestCase):
    """
        Test class for the List and create methods for the Line Model
    """
    url = reverse("lines:v1_list_create_line")

    def test_list(self):
        LineFactory()

        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        response = response.json()

        self.assertEquals(response['body'].get('count'), 1)

    def test_create_successfully(self):
        data = {
            "name": "Urbvan Line 1",
            "color": "$00FF00",
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, 201)


class LineDetailTest(CustomUserTestMixin, APITestCase):
    """
        Test class for the detail methods for Line Model: Retrieve, update, destroy
    """

    def test_retrieve_successfully(self):
        """
            Retrieve test for Line Model API
        """
        st = LineFactory()
        url = reverse("lines:v1_detail_line", kwargs={'pk': st.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['id'], st.id)

    def test_update_successfully(self):
        """
            Update unit test for Line Model API
        """
        st = LineFactory()
        url = reverse("lines:v1_detail_line", kwargs={'pk': st.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['color'], st.color)
        data = {
            "name": st.name,
            "color": "#FFFFFF",
        }
        response = self.client.patch(url, data=data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['id'], st.id)
        self.assertEquals(response.data['color'], "#FFFFFF")

    def test_destroy_successfully(self):
        """
            Update unit test for Line Model API
        """
        st = LineFactory()
        url = reverse("lines:v1_detail_line", kwargs={'pk': st.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        response = self.client.delete(url)
        self.assertEquals(response.status_code, 204)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)


class RouteListCreateTest(CustomUserTestMixin, APITestCase):
    """
        Test class for the List and create methods for the Station Model
    """
    url = reverse("routes:v1_list_create_route")

    def test_list(self):
        RouteFactory()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        response = response.json()
        self.assertEquals(response['body'].get('count'), 1)

    def test_create_successfully(self):
        line = LineFactory()
        data = {
            "line": line.id,
            "stations": [],
            "direction": True,
            "is_active": True
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, 201)


class RouteDetailTest(CustomUserTestMixin, APITestCase):
    """
        Test class for the detail methods for Route Model: Retrieve, update, destroy
    """

    def test_retrieve_successfully(self):
        """
            Retrieve test for Route Model API
        """
        st = RouteFactory()
        url = reverse("routes:v1_detail_route", kwargs={'pk': st.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['id'], st.id)

    def test_update_successfully(self):
        """
            Update unit test for Route Model API
        """
        st = RouteFactory()
        url = reverse("routes:v1_detail_route", kwargs={'pk': st.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['is_active'], st.is_active)
        data = {
            "is_active": not st.is_active,
        }
        response = self.client.patch(url, data=data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['id'], st.id)
        self.assertEquals(response.data['is_active'], not st.is_active)

    def test_destroy_successfully(self):
        """
            Update unit test for Route Model API
        """
        st = RouteFactory()
        url = reverse("routes:v1_detail_route", kwargs={'pk': st.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        response = self.client.delete(url)
        self.assertEquals(response.status_code, 204)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
