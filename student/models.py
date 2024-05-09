from django.db import models


class School(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

class Class(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

class AssessmentArea(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=255)

class Answers(models.Model):
    id = models.IntegerField(primary_key=True)
    answer = models.CharField(max_length=255)

class Award(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

class Subject(models.Model):
    id = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=255)
    subject_score = models.FloatField()

class Summary(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    sydney_participant = models.CharField(max_length=255)
    syndey_percentile = models.CharField(max_length=255)
    assessment_area = models.ForeignKey(AssessmentArea, on_delete=models.CASCADE)
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    correct_answer_percentage_per_class = models.FloatField()
    correct_answer = models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    participant = models.CharField(max_length=255)
    student_score = models.FloatField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    category_id = models.IntegerField()
    year_level_name = models.CharField(max_length=255)
    answer_id = models.ForeignKey(Answers, on_delete=models.CASCADE)
    correct_answer_id = models.IntegerField()
