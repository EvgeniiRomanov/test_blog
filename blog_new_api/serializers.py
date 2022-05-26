"""Сериализуем объекты из БД в json и обратно разными способами"""

# Сериализация с помощью фунций
# сериалайзер из бд в json


def note_to_json(note) -> dict:
    return {
        "id": note.id,
        "title": note.title,
        "message": note.message,
        "public": note.public,          # в методе put - false или true (регистр важен)
        "create_at": note.create_at,   # нужно комментить в тестах  TestNoteDetailAPIView(APITestCase):
    }


# сериалайзер для входной схемы
def note_created(note) -> dict:
    return {
        "id": note.id,
        "title": note.title,
        "message": note.message,
        "public": note.public,
        "create_at": note.create_at,
        "update_at": note.update_at,
        "author": note.author_id
    }


# Сериализация классами
from rest_framework import serializers
from blog_new.models import Note


# выдача всех полей - определяет как выглядят выходные данные пользователю
class NoteSerializer(serializers.ModelSerializer):
    class Meta:             # хранит внутри конфигурации, имя именно это
        model = Note        # accept model
        fields = "__all__"  # show all fields (либо exclude = ('public', ))
        read_only_fields = ("author", )  # только для чтения, что бы в post не отображался что итипа обязат поле


# вариант когда урезаем выдачу полей
class MiniNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', "author", "message")  # show all fields, как аналог можно просто исключить -
                                              # какое-то поле exclude = ("id", )
        read_only_fields = ("author", )
