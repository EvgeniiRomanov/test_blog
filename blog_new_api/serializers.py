# сериализуем объект из БД в json

# сериалайзер для выходной схемы
def note_to_json(note) -> dict:
    return {
        "id": note.id,
        "title": note.title,
        "message": note.message,
        "public": note.public,
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