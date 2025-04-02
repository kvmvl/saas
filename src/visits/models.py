from django.db import models

# Create your models here.
class PageVisit (models.Model):
    #db -> table
    #id -> hidden -> primaty key -> autofield -> 1,2,3,4,5 ...
    path = models.TextField(blank=True, null=True) #column
    timestamp = models.DateTimeField(auto_now_add=True) #column