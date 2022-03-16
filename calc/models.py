<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import User

class calc(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=12)
    rans = models.CharField(max_length=12)
    rques = models.CharField(max_length=12)
    birthday=models.DateField()
    token = models.CharField( max_length=200,default='')
    is_varified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    






=======
from django.db import models
from django.contrib.auth.models import User

class calc(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=12)
    rans = models.CharField(max_length=12)
    rques = models.CharField(max_length=12)
    birthday=models.DateField()
    token = models.CharField( max_length=200,default='')
    is_varified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    






>>>>>>> feff908ca3cc4f9fc888c5f3fcf21edaf7ac79b9
