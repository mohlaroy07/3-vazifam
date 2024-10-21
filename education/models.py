from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    

class Lesson(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title