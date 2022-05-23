from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from blog_new.models import Note  # подтягиваем модель, из др приложения
from . import serializers

# сериализация функциями
# class NoteListCreateAPIView(APIView):
#     """Read all list"""
#     def get(self, request:Request):
#         objects = Note.objects.all()
#         return Response([serializers.note_to_json(elem) for elem in objects])
#         #return Response({"test":"test"})
#
#     def post(self, request: Request):
#         data = request.data # считываем отправленный кнопкой POST json по http
#         note = Note(**data, author=request.user)  # формируем объект python для базы
#         note.save(force_insert=True) # сохраняем в базе сформированный объект
#         # возвращаем результат пользователю
#         return Response(
#             serializers.note_created(note),
#             status=status.HTTP_201_CREATED
#         ) #


# сериализация классами
from blog_new_api import serializers, filters
from rest_framework.generics import ListAPIView    # получаем ключевые действия


class NoteListCreateAPIView(APIView):
    """Read all list"""
    def get(self, request:Request):
        notes = Note.objects.all()
        serializer = serializers.NoteSerializer(
            instance=notes, # передаем экземпляры
            many=True,
        )

        return Response(data = serializer.data)

    def post(self, request: Request):
        serializer = serializers.NoteSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)  # проверка сырых данных и если ошибка, возврат ошибки (типа 404)
        serializer.save(author=request.user)  # сохранияем в базе (в скобках берем автора, которого типа скрыли в модели)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class NoteDetailAPIView(APIView):
    def get(self, request, pk):
        # note = Note.objects.get(pk=pk)
        # return Response(serializers.note_to_json(note))
        note = get_object_or_404(Note, pk=pk)   # обработка ошибок если нет такого номера
        #return Response(serializers.note_to_json(note))     # закомментил на 3 практике


    def put(self, request, pk):
        object = get_object_or_404(Note, pk=pk)
        object.title = request.data['title']
        object.message = request.data['message']
        object.public = request.data['public']

        object.save(force_update=True)

        return Response(
            serializers.note_created(object),
            status = status.HTTP_201_CREATED
        )

    # практика 3 (02:15) распивывали put через классы

    # generics - альтернитива тому что мы писали раньше
    #
class PublicNoteListAPIView(ListAPIView):
    """/notes/public/"""
    queryset = Note.objects.all()   #(public=True) - отображать только пубуличные, но так не правильно ограничивать
    serializer_class = serializers.NoteSerializer

    def get_queryset(self):                         # получем данные с которыми будем работать
        queryset = super().get_queryset()            # получаем полную копию
        return queryset.filter(public=True)           # фильтруем (author=self.request.user, public = True)

    def filter_queryset(self, queryset):
       # queryset = super().filter_queryset(queryset)   #
        #self.request.query_params.get("author_id", None)
        return filters.note_filter_by_author_id(
            queryset,
            author_id=self.request.query_params.get("author_id", None)
        )