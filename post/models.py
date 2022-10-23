from django.db import models

# Create your models here.
""" 'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018' 
        'thumbnail': 'https://picsum.photos/200/300' """
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author) + ' | ' + str(self.date_posted) + ' | ' + self.content + ' | ' + str(self.id) + ' | ' 
