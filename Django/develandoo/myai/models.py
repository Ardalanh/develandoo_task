from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=255)
    user_file = models.FileField(upload_to='docs/%Y/%m/%d/')
    logreg_result = models.FileField(upload_to='docs/%Y/%m/%d/result/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
