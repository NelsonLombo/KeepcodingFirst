# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import  User

# Create your models here.
COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

LICENSES = (
    (COPYRIGHT, 'Copyright'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creative Commons')
)

PUBLIC = 'PUB'
PRIVATE = 'PRI'
VISIBILITY = (
    (PUBLIC, 'pública'),
    (PRIVATE, 'privada')
)
class Photo(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=150)
    url = models.URLField()
    description  = models.TextField(blank=True,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now=True)
    license = models.CharField(max_length=3,choices=LICENSES)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=PUBLIC)

    def __unicode__(self): # metodo de 0 parametros
        return self.name
