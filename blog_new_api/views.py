from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from blog_new.models import Note  # подтягиваем модель, из др приложения
from . import serializers

class NoteListCreateAPIView(APIView):
    """Read all list"""
    def get(self, request:Request):
        objects = Note.objects.all()
        return Response([serializers.note_to_json(elem) for elem in objects])
        #return Response({"test":"test"})

    def post(self, request: Request):
        data = request.data # считываем отправленный кнопкой POST json по http
        note = Note(**data)  # формируем объект python для базы
        note.save(force_insert=True) # сохраняем в базе сформированный объект

        return Response(
            serializers.note_created(note),
            status=status.HTTP_201_CREATED
        ) #


class NoteDetailAPIView(APIView):
    def get(self, request, pk):
        # note = Note.objects.get(pk=pk)
        # return Response(serializers.note_to_json(note))
        note = get_object_or_404(Note, pk=pk)   # обработка ошибок если нет такого номера
        return Response(serializers.note_to_json(note))


    def put(self, request):
        ...
