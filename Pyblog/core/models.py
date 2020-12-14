from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Publish(models.Model):
    title = models.CharField('Título', max_length=200)
    photo = models.ImageField('Foto')
    content = RichTextUploadingField('Conteudo')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Título'
        verbose_name_plural = 'Títulos'

    def __str__(self):
        return self.title
