from django.db import models

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default=' ')
    email = models.CharField(max_length=50, default=' ')
    balance = models.IntegerField(default=0)
    Date_of_Creation = models.DateField(auto_now=True)

    #def __str__(self):
    #   return self.name



class Transaction(models.Model):
    T_id = models.AutoField(primary_key=True)
    from_account = models.CharField(max_length=50, default=' ')
    to_account = models.CharField(max_length=50, default=' ')
    amount = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)

    #def __str__(self):
    #    return self.T_id
#
#