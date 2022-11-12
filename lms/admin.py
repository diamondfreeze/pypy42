from django.contrib import admin
from lms.models import Curator
from lms.models import Direction
from lms.models import Discipline
from lms.models import Group

admin.site.register(Curator)
admin.site.register(Direction)
admin.site.register(Discipline)
admin.site.register(Group)