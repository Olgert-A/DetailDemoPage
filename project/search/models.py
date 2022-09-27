from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=50)

    def __str__(self):
        return self.product_name


class Assembly(models.Model):
    assembly_name = models.CharField(max_length=50)
    part_of_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.assembly_name


class Detail(models.Model):
    detail_name = models.CharField(max_length=50)
    part_of_assembly = models.ManyToManyField(Assembly, through="Binder")

    def __str__(self):
        return self.detail_name


class Binder(models.Model):
    STATUS_CHOISES = [
        ('Act', 'Active'),
        ('Arc', 'Archive')
    ]
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
    assembly = models.ForeignKey(Assembly, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    status = models.CharField(max_length=50, choices=STATUS_CHOISES)

    def __str__(self):
        return f'{self.detail} - {self.assembly}'
