from django.db import models



class Hall(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()


class Table(models.Model):
    table_types = (
        ('R', 'Rectangular'),
        ('O', 'Oval'),
    )
    table_id = models.AutoField(primary_key=True)
    seats_number = models.IntegerField()
    table_type = models.CharField(max_length=1, choices=table_types)
    table_center_x = models.IntegerField()
    table_center_y = models.IntegerField()
    scale = models.IntegerField()


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    email = models.CharField(max_length=40)
    client_name = models.CharField(max_length=40)



 
    
