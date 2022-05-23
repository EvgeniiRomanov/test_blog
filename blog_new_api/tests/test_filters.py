from django.test import TestCase
from django.contrib.auth.models import User
from blog_new.models import Note
from blog_new_api import filters

# тестируем список записей конкретного автора
# генерируем список разных авторов и записей (пример 2 автора, 2 записи)
# фильтруем по конкретному

class TestBlogAPINoteFilters(TestCase):
    def test_note_filter_by_author_id(self):
        # создаем 2 users
        test_user1 = User(
            username="test_user1",
            password="fake1"
        )
        test_user2 = User(
            username="test_user2",
            password="fake2"
        )
        # test_user1.save()
        # test_user2.save()

        test_user1, test_user2 = User.objects.bulk_create([test_user1, test_user2])
        # наполняем базу 3 записями
        Note(title="title_1", author=test_user1).save()
        Note(title="title_2", author=test_user1).save()
        Note(title="title_2", author_id=test_user2.id).save()  # по внешнему соед 2 польз со 2 записью

        queryset = Note.objects.all()
        filter_author_id = test_user1.id
        expected_queryset = queryset.filter(author_id=filter_author_id)
        actual_queryset = filters.note_filter_by_author_id(
            queryset,
            author_id=filter_author_id,
        )
        # проверяем
        self.assertQuerysetEqual(
            actual_queryset, expected_queryset, ordered=False
        )