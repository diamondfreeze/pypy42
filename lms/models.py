from django.db.models import (Model, CharField, CASCADE, ForeignKey, Discipline)



class Curator(Model):
    first_name = CharField(max_length=20)

    def __str__(self):
        return 'курат. '+self.first_name



class Direction(Model):
    name = CharField(max_length=20)
    curator = ForeignKey(Curator,
                         on_delete=CASCADE,
                         related_name='direction')

    def __str__(self):
        return 'напр. '+self.name


class Discipline(Model):
    dis_name = CharField(max_length=10)
    direction = ForeignKey(Direction,
                         on_delete=CASCADE,
                         related_name='discipline',
                         )


    def __str__(self):
        return "discipline "+self.dis_name

