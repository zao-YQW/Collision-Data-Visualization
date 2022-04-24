# from django.contrib.auth.models import User
from django.db import models
from django.db.models import UniqueConstraint


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    manager_name = models.CharField(max_length=45)
    department = models.CharField(max_length=45)
    nickname = models.CharField(max_length=45)
    # user = models.ForeignKey(User,  related_name='employees', on_delete=models.PROTECT)


    def __str__(self):
        if self.nickname == '':
            result = f'{self.last_name}, {self.first_name}'
        else:
            result = f'{self.last_name}, {self.first_name} ({self.nickname})'
        return result

    class Meta:
        ordering = ['last_name', 'first_name', 'nickname']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'nickname'], name='unique_employee')
        ]


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length=225, unique=True)
    nickname = models.CharField(max_length=45)
    # user = models.ForeignKey(User, related_name='customer', on_delete=models.PROTECT)

    def __str__(self):
        if self.nickname == '':
            result = f'{self.last_name}, {self.first_name}'
        else:
            result = f'{self.last_name}, {self.first_name} ({self.nickname})'
        return result

    class Meta:
        ordering = ['last_name', 'first_name', 'nickname']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'nickname'], name='unique_customer')
        ]


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_type = models.CharField(max_length=45)
    card_type = models.CharField(max_length=45)
    card_number = models.IntegerField(unique=True)

    def __str__(self):
        result = f'{self.payment_type} : {self.card_number}'
        return result

    class Meta:
        ordering = ['payment_type', 'card_type']
        constraints = [
            UniqueConstraint(fields=['card_type', 'card_number'], name='unique_payment')
        ]


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    line1 = models.CharField(max_length=225)
    line2 = models.CharField(max_length=225)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    customer = models.ForeignKey(Customer, related_name='addresses', on_delete=models.PROTECT)

    def __str__(self):
        result = f'{self.line1}{self.line2} {self.city} {self.state}'
        return result

    class Meta:
        ordering = ['line1', 'line2', 'city', 'state']
        constraints = [
            UniqueConstraint(fields=['line1', 'line2', 'city', 'state'], name='unique_address')
        ]


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField()
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.PROTECT)
    payment = models.ForeignKey(Payment, related_name='orders', on_delete=models.PROTECT)
    #address = models.ForeignKey(Address, related_name='orders', on_delete=models.PROTECT)

    def __str__(self):
        result = f'{self.customer.last_name} {self.customer.first_name} ordered by {self.order_date} '
        return result

    class Meta:
        ordering = ['order_date', 'customer']


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=45, unique=True)
    year_founded = models.IntegerField()
    company = models.CharField(max_length=225)

    def __str__(self):
        result = f'{self.brand_name} by {self.company}'
        return result

    class Meta:
        ordering = ['brand_name', 'year_founded', 'company']
        constraints = [
            UniqueConstraint(fields=['brand_name', 'year_founded', 'company'], name='unique_brand')
        ]


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=45, unique=True)
    product_price = models.IntegerField()
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.PROTECT)

    def __str__(self):
        result = f'{self.product_name} -- {self.product_price}'
        return result

    class Meta:
        ordering = ['product_name', 'product_price', 'brand']
        constraints = [
            UniqueConstraint(fields=['product_name', 'product_price', 'brand'], name='unique_product')
        ]


class OrderDetail(models.Model):
    order_detail_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    item_total_price = models.FloatField()
    order = models.ForeignKey(Order, related_name='orderdetails', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name='orderdetails', on_delete=models.PROTECT)

    def __str__(self):
        result = f'{self.product.product_name} * {self.quantity} = {self.item_total_price}'
        return result

    class Meta:
        ordering = ['order__order_date', 'product__product_name']
        constraints = [
            UniqueConstraint(fields=['order', 'product'], name='unique_orderdetail')
        ]
