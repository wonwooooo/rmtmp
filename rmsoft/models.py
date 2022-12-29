from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=200)
    company_boss_name = models.CharField(max_length=200)
    company_phone_number = models.CharField(max_length=200)

    objects = CompanyName()

    class Meta:
        unique_together = [['company_name']]


class CompanyName(models.Model):
    def get_by_natural_key(self, company_name):
        return self.get(company_name=company_name)

class Product(models.Model):
    p_name = models.CharField(max_length=200)
    p_price = models.IntegerField()
    p_registerdate = models.DateTimeField(auto_now_add=True)
    p_company_name = models.ForeignKey(Company, on_delete=models.CASCADE)

class Client(models.Model):
    client_name = models.CharField(max_length=200)
    client_phone_number = models.CharField(max_length=200)

class Order(models.Model):
    o_p_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    o_client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    o_date =  models.DateTimeField(auto_now_add=True)
    o_number = models.IntegerField()

