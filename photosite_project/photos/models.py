from django.db import models

class page(models.Model):
    pageNum = models.IntegerField(default = 0, unique = True)
    
    
    
    
class photo(models.Model):
    imagename = models.CharField(max_length = 128)
    pageName = models.ForeignKey(page, on_delete = models.CASCADE)
    
    
    @property
    def image_url(self):
        return 'images/{}'.format(self.imagename)
    
    def __str__(self):
        return self.imagename



# Create your models here.
