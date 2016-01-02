# -*- coding: utf-8 -*-
from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='documents')



class FileInfo(models.Model):
	file_name = models.CharField(max_length = 200, default = 'APK file')
	permissions_info = models.CharField(max_length = 2000, default = 'It may not be an APK file')


