"""Сериализуем объекты из БД в json и обратно разными способами"""
from datetime import datetime

# Сериализация классами
from rest_framework import serializers
from blog_new.models import Note, Comment


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


# выдача всех полей - определяет как выглядят выходные данные пользователю
class NoteSerializer(serializers.ModelSerializer):
    class Meta:             # хранит внутри конфигурации, имя именно это
        model = Note        # accept model
        fields = "__all__"  # show all fields (либо exclude = ('public', ))
        read_only_fields = ("author", )  # только для чтения, что бы в post не отображался как обязат поле


# # вариант когда урезаем выдачу полей
# class MiniNoteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Note
#         fields = ('id', "author", "message")  # show all fields, как аналог можно просто исключить -
#                                               # какое-то поле exclude = ("id", )
#         read_only_fields = ("author", )


class CommentSerializer(serializers.ModelSerializer):
    """Для замены поля rating из Comment, перезаписываем его сериалайзером"""
    rating = serializers.SerializerMethodField('get_rating')

    def get_rating(self, obj: Comment):
        return {
            'value': obj.rating,
            'display': obj.get_rating_display()  # из models Comment
        }

    class Meta:
        model = Comment
        fields = "__all__"
        # exclude = ("id", "note", )


class NoteDetailSerializer(serializers.ModelSerializer):
    """/notes/pk"""
    author = serializers.SlugRelatedField(
        # author в models есть FK на табл auth_user, для красивого отображения
        # подменяем поле по умолчанию id (или pk) из табл auth_user
        # на slug_field из той же табл. SlugRelatedField работает только на FK
        slug_field="username",  # new field to show
        read_only=True
    )
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = (
            'title', 'message', 'public', 'create_at', 'update_at',  # from model
            'author', 'comments'                        # from serializer
        )

    def to_representation(self, instance):
        """Меняем формат вывода даты в ответе"""
        ret = super().to_representation(instance)
        create_at = datetime.strptime(ret['create_at'], '%Y-%m-%dT%H:%M:%S.%f')
        update_at = datetime.strptime(ret['update_at'], '%Y-%m-%dT%H:%M:%S.%f')
        ret['create_at'] = create_at.strftime('%d %B %Y %H:%M:%S')
        ret['update_at'] = update_at.strftime('%d %B %Y %H:%M:%S')
        return ret