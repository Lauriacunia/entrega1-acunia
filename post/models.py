from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author) + ' | ' + str(self.date_posted) + ' | ' + self.content + ' | ' + str(self.id) + ' | ' 
