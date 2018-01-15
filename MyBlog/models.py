from django.db import models

# Create your models here.
class ArticleTarget(models.Model):
    targetName = models.CharField(primary_key=True,max_length=100,blank=False)

    def __str__(self):
        return self.targetName


class Article(models.Model):
    Title = models.CharField(max_length=200,blank=False)
    target = models.ForeignKey(ArticleTarget)
    recordTime= models.DateField(auto_now=True)
    showPicture = models.ImageField(upload_to='showImg')
    articleDes = models.CharField(max_length=300,blank=False)
    #articleDetial = models.CharField(max_length=10000,blank=False)
    articleDetial = models.TextField(max_length=10000,blank=False)
    def __str__(self):
        return self.Title