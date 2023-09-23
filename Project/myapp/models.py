from django.db import models

class User(models.Model):
    # any data from the user that we would like to have
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    gender = models.CharField(max_length = 10)
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)

# A table User will get created in the database and it will look like:

# Id   Name      Age     Gender      Email       Password
# 1    abc       17        F         ab@h.com    231#
# 2    vgf       27        M         ty@h.com    121#
# 3    tyu       57        F         6b@h.com    251#

# Create your models here.

# Health Details Table will look like this:

# user  age pregnancies .. is_diabetic
# 2     45  4                          

class HealthDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    pregnancies = models.IntegerField()
    glucose = models.IntegerField()
    blood_pressure = models.IntegerField()
    skin_thickness = models.IntegerField()
    insulin = models.IntegerField()
    bmi = models.IntegerField()
    diabetes_pedigree_function = models.IntegerField()
    is_diabetic = models.IntegerField()