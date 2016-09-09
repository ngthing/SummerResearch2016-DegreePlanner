from django.contrib import admin
from .models import Student,Enroll,csbs_course, gmu_cs_course_topic_association,Topic, gmu_cs_courses, ResultSet, AllGmuCourses
# Register your models here.

admin.site.register(Student)
admin.site.register(Enroll)
admin.site.register(csbs_course)
admin.site.register(Topic)
admin.site.register(ResultSet)
admin.site.register(gmu_cs_courses)
admin.site.register(gmu_cs_course_topic_association)
admin.site.register(AllGmuCourses)