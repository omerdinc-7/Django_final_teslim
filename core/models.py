from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.forms import CharField


class AbstractModel(models.Model):
    updated_date = models.DateTimeField(auto_now=True, blank=True, verbose_name='Updated Date')
    created_date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Created Date')

    class Meta:
        abstract = True


class GeneralSetting(AbstractModel):
    name = models.CharField(default='', max_length=254, blank=True, verbose_name='Name',
                            help_text='This is variable of the settings.')
    description = models.CharField(default='', max_length=254, blank=True, verbose_name='Description')
    parameter = models.CharField(default='', max_length=254, blank=True, verbose_name='Parameter')

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ['name', ]


class ImageSetting(AbstractModel):
    name = models.CharField(default='', max_length=254, blank=True, verbose_name='Name',
                            help_text='This is variable of the settings.')
    description = models.CharField(default='', max_length=254, blank=True, verbose_name='Description')
    file = models.ImageField(default='', max_length=254, blank=True, verbose_name='Image', upload_to='images/')

    def __str__(self):
        return f'Image Setting: {self.name}'

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ['name', ]


class Skill(AbstractModel):
    order = models.IntegerField(default=0, verbose_name='Order')
    name = models.CharField(default='', max_length=254, blank=True, verbose_name='Name',
                            help_text='This is variable of the settings.')

    percentage = models.IntegerField(default=50, blank=True, verbose_name='Percentage',
                                     validators=[MinValueValidator, MaxValueValidator])

    def __str__(self):
        return f'Skill: {self.name}'

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['order', ]


class SocialMedia(AbstractModel):
    order = models.IntegerField(default=0, verbose_name='Order')
    link = models.URLField(default='', max_length=254, blank=True, verbose_name='Link')
    icon = models.CharField(default='', max_length=254, blank=True, verbose_name='Icon')

    def __str__(self):
        return f'Social Media: {self.link}'

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Media'
        ordering = ['order', ]


class Document(AbstractModel):
    order = models.IntegerField(default=0, verbose_name='Order')
    name = models.CharField(default='', max_length=254, blank=True, verbose_name='Name',
                            help_text='This is variable of the settings.')
    file = models.FileField(default='', blank=True, verbose_name='File', upload_to='documents/')
    slug = models.SlugField(default='', max_length=254, blank=True, verbose_name='Slug',
                            help_text='This is variable of the settings. It is used for URL.')
    button_text = models.CharField(default='', max_length=254, blank=True, verbose_name='Button Text')

    def __str__(self):
        return f'Document: {self.name}'

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        ordering = ['name', ]
