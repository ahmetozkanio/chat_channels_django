from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# class Room(models.Model):
#     name = models.CharField(max_length=255,unique=True)
#     teacher = models.ForeignKey(User,on_delete=models.CASCADE)
#     students = models.ManyToManyField(User,blank=True,related_name="students")
    
#     def __str__(self):
#         return self.name

class Message(models.Model):
    # room = models.ForeignKey(Room,null=True,on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages():
        return Message.objects.order_by('-timestamp').all()[:10]