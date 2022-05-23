# # сериализуем объект из БД в json
#
# # сериалайзер для выходной схемы
# def note_to_json(note) -> dict:
#     return {
#         "id": note.id,
#         "title": note.title,
#         "message": note.message,
#         "public": note.public,
#         "create_at": note.create_at,   # нужно комментить в тестах  TestNoteDetailAPIView(APITestCase):
#     }
#
#
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

from rest_framework import serializers
from blog_new.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:  # хранит внутри конфигурации, имя именно это
        model = Note        # accept model
        fields = "__all__"  # show all fields
        read_only_fields = ("author", )  # только для чтения, что бы в post не отображался что итипа обязат поле
        #read only fields

    # вариант когда урезаем выдачу полей
class MiniNoteSerializer(serializers.ModelSerializer):
    class Meta:  # хранит внутри конфигурации, имя именно это
        model = Note        # accept model
        fields = ('id', "author", "message")  # show all fields # аналог можно просто исключить какое-то поле exclude = ("id", )

        read_only_fields = ("author", )  # только для чтения, что бы в post не отображался что итипа обязат поле
        #read only fields