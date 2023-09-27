from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return f"Client: {self.name}, email: {self.email}, id: {self.id}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product: {self.name}, price: {self.price}, count: {self.count}"

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        title = f'Order by {self.client}, \nproducts: \n  '
        body = "\n  ".join(str(i) for i in self.products.all())
        return title + body