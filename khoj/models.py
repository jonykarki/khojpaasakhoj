from django.db import models

# Create your models here.
class Post(models.Model):
    bimg = models.URLField()
    btype = models.CharField(max_length=200)
    bname = models.CharField(max_length=200)
    bservices = models.CharField(max_length=400)
    bphoneno = models.BigIntegerField(max_length=500)
    baddress = models.CharField(max_length=150)
    bowner = models.CharField(max_length=200, null=True)
    bemail = models.CharField(max_length=200, null=True)
    bwebsite = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.bname

# user model for storing the users
class User(models.Model):
    post = models.ForeignKey(Post)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

# store the reviews by the users 
class Review(models.Model):
    user = models.ForeignKey(User)
    review = models.CharField(max_length=3000)
    rating = models.IntegerField()

    def __str__(self):
        return self.review
