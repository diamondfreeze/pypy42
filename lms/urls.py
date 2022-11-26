from rest_framework.routers import DefaultRouter
from lms.views import StudentViewSet, CuratorViewSet, GroupViewSet, DisciplineViewSet, DirectionViewSet

lms_router = DefaultRouter()
lms_router.register(r'student',
                    StudentViewSet,
                    basename = 'student')
lms_router.register(r'curator',
                    CuratorViewSet,
                    basename = 'student')
lms_router.register(r'group',
                    GroupViewSet,
                    basename = 'student')
lms_router.register(r'discipline',
                    DisciplineViewSet,
                    basename = 'student')
lms_router.register(r'direction',
                    DirectionViewSet,
                    basename = 'student')
