import unittest

from rest_framework.test import APITestCase
from rest_framework import status
from blog_new.models import Note
from django.contrib.auth.models import User


class TestNoteListCreateAPIView(APITestCase):
    @classmethod
    def setUpTestData(cls):                            # тест данные один раз на все тесты
        User.objects.create(username='test@test.ru')   # создаем пользователя по умолчанию, он будет
                                                       # сидеть в нашей БД для всех тестов, у него author_id=1

    def test_empty_list_objects(self):
        url = '/notes/'                 # путь куда стучаться от корня
        resp = self.client.get(url)     # клиент типа браузера, с которого мы делаем запросы и получаем ответ
        # ожидаем от сервера ответ "status.HTTP_200_OK" и сравниваем с полученными
        self.assertEqual(status.HTTP_200_OK, resp.status_code)

        # если база пустая, там пустой список т.к. listcomp во view
        response_data = resp.data       # полученные данные
        exp_data = []                   # ожидаемые данные
        self.assertEqual(exp_data, response_data)

    def test_list_objects(self):
        # Выше setUpTestData создали пользователя
        # Далее помещаем 2 записи с созданным пользователем

        # имитация помещения данных в базу по ключу
        Note.objects.create(title='Заголовок из тестов 1', author_id=1)   # создание 1 запись, польз достаем по id
        # аналогично по пользователю
        test_user = User.objects.get(username="test@test.ru")          # достаем пользователя созд в setUpTestData
        Note.objects.create(title='Заголовок из тестов 1', author=test_user)  # создаем 2 запись

        url = '/notes/'
        resp = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, resp.status_code)

        response_data = resp.data               # достаем 2
        self.assertEqual(2, len(response_data)) # поместили 2 (выше 2 create) достать должны тоже 2


    # ОБЕЩАЛ на 3 лекции показать на 3 практике как создавать
    #@unittest.skip("ЕЩЕ НЕ РЕАЛИЗОВАН")
    def test_create_objects(self):

        Note.objects.create(
            id=1,
            title='Тест создание объекта Note',
            message='Создан Note',
            public=True,
            author_id=1)

        new_title = "TEST from title"
        new_data = {
            "id": 2,
            "title": new_title,
            "message": "Тестируем создание объекта",
            "public": True,
            "author_id": 1
        }
        url = "/notes/"
        # отправили пост запрос и создался объект в таблице
        resp = self.client.post(url, new_data)
        self.assertEqual(status.HTTP_201_CREATED, resp.status_code)

        # забираем объект из базы, если оюъект не найден, вернет ошибку does not exist
        # Note.objects.get(title=new_title)  # exists assertTrue()


class TestNoteDetailAPIView(APITestCase):
    """Класс тестов для отдельных объектов базы"""

    @classmethod
    def setUpTestData(cls):  # создаем тест данные один раз на все тесты внутри данного класса
        User.objects.create(username='test@test.ru')                        # создаем пользователя
        Note.objects.create(title='Заголовок из тестов 1', author_id=1)     # создаем 1 запись
        Note.objects.create(title='Заголовок из тестов 2', author_id=1)     # создаем 2 запись

    # обновление существующей записи
    def test_retrieve_object(self):
        note_pk = 2                     # id записи
        url = f"/notes/{note_pk}"       #

        resp = self.client.get(url)    # запрос
        self.assertEqual(status.HTTP_200_OK, resp.status_code)

        # нам прилетел resp с data
        expected_data = {
            "id": 2,
            "title": 'Заголовок из тестов 2',
            "message": '',
            "public": False
            #"create_at": ''   # не работает если раскоментить с ней из-за serializer.py
        }

        self.assertDictEqual(expected_data, resp.data)

    def test_does_not_exists_object(self):
        does_not_exist_pk = '123123123123'
        url = f"/notes/{does_not_exist_pk}"

        resp = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, resp.status_code)

    def test_update_object(self):
        # создаем запись
        Note.objects.create(
            title='Заголовок на изменение',
            message="Тут есть данные для изменения",
            public=False,
            author_id=1)

        # Делаем запрос на извлечение
        note_pk = 3
        url = f"/notes/{note_pk}"
        resp = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, resp.status_code)

        # проверяем извлеченную запись
        expected_data = {
            "id": 3,
            "title": 'Заголовок на изменение',
            "message": 'Тут есть данные для изменения',
            "public": False
        }

        self.assertDictEqual(expected_data, resp.data)

        # формируем обновление
        expected_update_data = {
            "id": 3,
            "title": 'Обновленный заголовок',
            "message": 'Обновленное сообщение',
            "public": False
        }

        # проверка успешности создания обновления
        resp_update = self.client.put(url, expected_update_data)
        self.assertEqual(status.HTTP_201_CREATED, resp_update.status_code)

        # считывание измененных данных и проверка обновленных полей
        resp2 = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, resp2.status_code)
        self.assertDictEqual(expected_update_data, resp2.data)

    def test_partial_update_object(self):
        pass