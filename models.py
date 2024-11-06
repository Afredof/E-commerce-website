from django.db import models

# Create your models here.
class reg_table(models.Model):
    nm=models.CharField(max_length=25)
    em=models.EmailField()
    num=models.IntegerField()
    pwd=models.CharField(max_length=25)
    rpwd=models.CharField(max_length=25)
    
class item_table(models.Model):
    inm=models.CharField(max_length=25)
    img=models.FileField(upload_to='pic')
    prc=models.IntegerField()
    des=models.TextField()
class cart_table(models.Model):
    customer=models.ForeignKey(reg_table,on_delete=models.CASCADE)
    product=models.ForeignKey(item_table,on_delete=models.CASCADE)
    qty=models.PositiveBigIntegerField(default=1)
class Pay_table(models.Model):
    pro=models.CharField(max_length=25)
    qty=models.IntegerField()
    prc=models.IntegerField()
    tot=models.IntegerField()
    fn=models.CharField(max_length=25)
    ex=models.DateField()
    cvv=models.IntegerField()