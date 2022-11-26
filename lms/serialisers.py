from rest_framework import serializers

from lms.models import Student
from lms.models import Curator
from lms.models import Group
from lms.models import Discipline
from lms.models import Direction

class StudentSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Student
        fields = '__all__'


class CuratorSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Curator
        fields = '__all__'

class GroupSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Group
        fields = '__all__'

class DisciplineSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Discipline
        fields = '__all__'

class DirectionSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Direction
        fields = '__all__'