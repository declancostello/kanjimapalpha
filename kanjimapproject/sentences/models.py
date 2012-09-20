from django.db import models

# Create your models here.
class Sentence(models.Model):
    sentence = models.TextField()
    views = models.IntegerField()

    def __unicode__(self):
        return self.sentence

# 1 to 1 source
class Source(models.Model):
    sentence = models.ForeignKey(Sentence)
    source = models.CharField(max_length=200)

    def __unicode__(self):
        return self.source
