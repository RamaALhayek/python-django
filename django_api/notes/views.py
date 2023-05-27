from rest_framework import viewsets
from .models import Author, Note
from .serializers import AuthorSerializer, NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
