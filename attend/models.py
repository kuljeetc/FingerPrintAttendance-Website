from django.db import models

# Create your models here.
class User(models.Model):
    def __str__(self):
        return " user_id :" + self.user_id

    user_id = models.CharField(max_length=20, primary_key=True)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=1000)

class Attendance(models.Model):
    def __str__(self):
        return "Id :" + str(self.id) + " user_id :" + self.user.user_id + " attendance : " + str(self.attend_date)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attend_date = models.DateTimeField('Entry Date/Time')



