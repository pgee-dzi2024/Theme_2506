from django.db import models


# Групи в менюто
class Group(models.Model):
    name = models.CharField('Наименование', max_length=50, default='', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Раздел в менюто'
        verbose_name_plural = 'Раздели в менюто'


# Меню
class MenuItem(models.Model):
    name = models.CharField('Наименование', max_length=100, default='', blank=True)
    description = models.TextField('Описание', default='', blank=True)
    price = models.DecimalField('Цена', max_digits=6, decimal_places=2, default=0)
    photo = models.ImageField('Снимка', upload_to='menu', blank=True)
    section = models.ForeignKey(Group, verbose_name='Раздел/група', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Позиция в менюто'
        verbose_name_plural = 'Позиции в менюто'

