from django.db import models

# Create your models here.
class months     (models.Model):
    ids = models.AutoField(primary_key=True)
    title = models.TextField(max_length=100)
    desc = models.TextField(max_length=200)
    image = models.TextField(max_length=200,default='courseImage')
    def __str__(self):
        return self.title + " | " + "courseId: "+str(self.ids)
    # code = models.CharField(max_length=2)
    # res = models.FileField(upload_to='media/')

class weeks (models.Model):
    ids = models.AutoField(primary_key=True)
    cid = models.ForeignKey(months, on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    desc = models.TextField(max_length=200)
    oid = models.IntegerField()
    image = models.TextField(max_length=200,default='topicImage')
    def __str__(self):
        s = self.title +" | "+ self.cid.title + " | " + str(self.oid) + " | " + "topicId: " + str(self.ids)
        return s

class content (models.Model):
    conid =models.AutoField(primary_key=True)
    tid = models.ForeignKey(weeks, on_delete=models.CASCADE)
    code = models.CharField(max_length=1)
    data = models.TextField(max_length=300)
    oid = models.IntegerField()
    def __str__(self):
        s = self.code + " | " + self.tid.title +" | "+ self.tid.cid.title + " | " + str(self.oid)
        return s
