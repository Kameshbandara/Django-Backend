from django.contrib import admin

from .models import (Answers, AssessmentArea, Award, Class, School, Student,
                     Subject, Summary)

admin.site.register(School)
admin.site.register(Class)
admin.site.register(AssessmentArea)
admin.site.register(Student)
admin.site.register(Answers)
admin.site.register(Award)
admin.site.register(Subject)
admin.site.register(Summary)

