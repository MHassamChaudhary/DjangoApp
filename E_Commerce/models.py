from django.db import models


class HomeSlider(models.Model):
    objects = None
    description = models.CharField(max_length=30, default='')
    image = models.ImageField(upload_to="E_Commerce/HomeSlider", default='')

    def __str__(self):
        dp_name = self.description
        return dp_name


class TopProducts(models.Model):
    objects = None
    strikeprice = models.IntegerField(default='')
    price = models.IntegerField(default='')
    name = models.CharField(max_length=20, default='')
    top_prod_image = models.ImageField(upload_to="E_Commerce/TopProducts", default='')

    def __str__(self):
        dp_name = self.name
        return dp_name


class TrendingProducts(models.Model):
    objects = None
    strikeprice = models.IntegerField(default='')
    price = models.IntegerField(default='')
    name = models.CharField(max_length=20, default='')
    top_prod_image = models.ImageField(upload_to="E_Commerce/TopProducts", default='')

    def __str__(self):
        dp_name = self.name
        return dp_name


class MenProducts(models.Model):
    objects = None
    strikeprice = models.IntegerField(default='')
    price = models.IntegerField(default='')
    name = models.CharField(max_length=20, default='')
    men_prod_image = models.ImageField(upload_to="E_Commerce/TopProducts", default='')

    def __str__(self):
        dp_name = self.name
        return dp_name


class ProdCard(models.Model):
    objects = None
    cardname = models.CharField(max_length=20, default='')
    carddesc = models.CharField(max_length=2000, default='')
    cardbuy = models.CharField(max_length=10, default='')
    cardImage = models.ImageField(upload_to="E_Commerce/Cards", default='')

    def __str__(self):
        dp_name = self.cardname
        return dp_name

# Customer Signin Info
class CustomerSignUp(models.Model):
    objects = None
    UserName = models.CharField(max_length=100, default='')
    usermail = models.CharField(max_length=100, default='')
    userpass = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.usermail


class SpecialOffers(models.Model):
    objects = None
    strikeprice = models.IntegerField(default='')
    price = models.IntegerField(default='')
    name = models.CharField(max_length=20, default='')
    special_prod_image = models.ImageField(upload_to="E_Commerce/SpecialOffers", default='')

    def __str__(self):
        dp_name = self.name
        return dp_name

