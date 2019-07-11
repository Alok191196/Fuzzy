from django.db import models


class Branch(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Student(models.Model):
    name = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Fuzzy(models.Model):
    internal_s = models.IntegerField()
    external_s = models.IntegerField()
    attendance_s = models.IntegerField()
    res_s = models.IntegerField()


class Semester(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Subjects(models.Model):
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    sem_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Marks(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    sem_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subj_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    internal = models.IntegerField()
    external = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Attendance(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    sem_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    attendance = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Technical(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    sem_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    technical = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Aptitude(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    sem_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    aptitude = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)



class FinalEvaluaton(models.Model):
    internal = models.TextField()
    external = models.TextField()
    attendance = models.TextField()
    output = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
