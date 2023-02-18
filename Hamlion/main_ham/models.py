from django.db import models
from django.shortcuts import reverse
# Create your models here.


class For_man(models.Model):
    SUM = 'ЛЕТО'
    WIN = 'ЗИМА'
    AUT = 'ОСЕНЬ'
    SPR= 'ВЕСНА'

    SEASON = [
        (SUM,'ЛЕТО'),
        (WIN,'ЗИМА'),
        (AUT,'ОСЕНЬ'),
        (SPR,'ВЕСНА'),
    ]

    SIZE = [
        ('XXS','XSS'),
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
        ('XXL','XXL'),
        ('XXXL','XXXL'),
    ]

    name_tovar = models.CharField('Имя товара', max_length=100)
    about_the_tovar = models.CharField('О товаре ',max_length=3000)
    price = models.IntegerField('Цена',null=True)
    image_tovar = models.ImageField(upload_to='%Y/%m/%d',null=True)
    size = models.CharField('Размер',choices=SIZE, max_length=4,null=True,blank=True)
    color = models.CharField('Цвет ', null=True,max_length=100,blank=True)
    articul_tovar = models.CharField('Артикул', max_length=20)
    sostav_tovar = models.CharField('Состав', max_length=100)
    season = models.CharField('Сезон',choices=SEASON,max_length=5,default=SUM)
    country = models.CharField('Страна',max_length=20)
    double_table = models.ForeignKey('Category',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.name_tovar} {self.about_the_tovar} {self.image_tovar}'

    class Meta():
        verbose_name = 'Мужчина'
        verbose_name_plural = 'Мужчины'




class For_Women(models.Model):
    SUM = 'ЛЕТО'
    WIN = 'ЗИМА'
    AUT = 'ОСЕНЬ'
    SPR= 'ВЕСНА'

    SEASON = [
        (SUM,'ЛЕТО'),
        (WIN,'ЗИМА'),
        (AUT,'ОСЕНЬ'),
        (SPR,'ВЕСНА'),
    ]
    SIZE = [
        ('XXS','XSS'),
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
        ('XXL','XXL'),
        ('XXXL','XXXL'),
    ]


    name_tovar = models.CharField('Имя товара', max_length=100, null=True)
    about_the_tovar = models.CharField('О товаре ',max_length=3000, null=True)
    price = models.IntegerField('Цена',null=True)
    image_tovar = models.ImageField(upload_to='%Y/%m/%d',null=True)
    size = models.CharField('Размер',choices=SIZE, max_length=4,null=True,blank=True)
    color = models.CharField('Цвет ', null=True,max_length=100,blank=True)
    articul_tovar = models.CharField('Артикул', max_length=20,null=True)
    sostav_tovar = models.CharField('Состав', max_length=100,null=True)
    season = models.CharField('Сезон',choices=SEASON,max_length=5,default=SUM,null=True)
    country = models.CharField('Страна',max_length=20,null=True)
    double_table = models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    

    class Meta():
        verbose_name = 'Женщина'
        verbose_name_plural = 'Женщины'

    def get_url(self):
        return reverse('clothes',args=[self.id])



class Category(models.Model):
    CHILD = 'РЕБ'
    MAN = 'МУЖ'
    WOMEN = 'ЖЕН'
 
    PERSONS = [
        (CHILD, 'РЕБЕНОК'),
        (MAN, 'МУЖЧИНА'),
        (WOMEN, 'ЖЕНЩИНА'),
    ]
    ALL_CLOTHES = 'ВСЕ'
    TOP_CLOTHES = 'ВВЕРХ'
    PANTS = 'БРЮКИ'
    JEANS = 'ДЖИНСЫ'
    TSHIRT = 'ФУТБОЛКИ'
    HUDI = 'ХУДИ'

    CATEGORY = [
        (ALL_CLOTHES, 'ВСЯ ОДЕЖДА'),
        (TOP_CLOTHES, 'ВЕРХНЯЯ ОДЕЖДА'),
        (PANTS, 'БРЮКИ'),
        (JEANS, 'ДЖИНСЫ'),
        (TSHIRT, 'ФУТБОЛКИ'),
        (HUDI, 'ТОЛСТОВКИ И ХУДИ'),
    ]
    persons = models.CharField('Персона', choices=PERSONS,default=MAN,max_length=3)
    category = models.CharField('Категория',choices=CATEGORY,default=ALL_CLOTHES,max_length=8)

    def __str__(self):
        return f'{self.persons} {self.category}'

    class Meta():
        verbose_name = 'Категории'
        verbose_name_plural = 'Категория'


class Tovars(models.Model):
    id_clothes = models.IntegerField('ID товара ',null=True)
    accounte = models.CharField('login',max_length=50,null=True)
    like = models.BooleanField('Выбран',null=True)

    class Meta():
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.accounte}  {self.id_clothes} {self.like}'


class Corzina(models.Model):
    id_clothes = models.IntegerField('ID товара ',null=True)
    accounte = models.CharField('login',max_length=50,null=True)
    count = models.IntegerField('Количество',null=True,default=1)
    price_for_tovars = models.ForeignKey('For_man',on_delete=models.CASCADE,null=True)
    class Meta():
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'{self.accounte}  {self.id_clothes} {self.count} {self.price_for_tovars}'


# class LikeTovar(models.Model):
#     id_clothes = models.IntegerField('ID товара ',null=True)
#     accounte = models.CharField('login', max_length=50, null=True)
#     like = models.BooleanField('Выбран')
#
#

#     class Meta():
#         verbose_name = 'Лайкнутый товар'
#         verbose_name_plural = 'Лайкнутый товары'
#
#     def __str__(self):
#         return f'{self.accounte}  {self.id_clothes} {self.accounte} {self.like}'
#

class Cart(models.Model):
    user  = models.ForeignKey(For_man,on_delete=models.CASCADE)



class Product(models.Model):
    name = models.CharField(max_length=150,null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=True,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''

        return url
