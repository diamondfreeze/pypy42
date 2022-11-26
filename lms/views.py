from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from lms.models import Student, Curator
from lms.serialisers import StudentSerializer
from lms.serialisers import CuratorSerializer
from lms.serialisers import GroupSerializer
from lms.serialisers import DisciplineSerializer
from lms.serialisers import DirectionSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class CuratortViewSet(viewsets.ModelViewSet):
    queryset = Curator.objects.all()
    serializer_class = CuratorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CuratorViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = CuratorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class DirectionViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]