from django.db import models
from django.db.models.fields import CharField,IntegerField,BooleanField
# Create your models here.


class topic(models.Model):
    t_id = models.CharField(max_length=500)
    tname=models.CharField(max_length=500)
    surano=models.IntegerField()
    suraname=models.CharField(max_length=100)
    verseno=models.IntegerField()
    verse=models.CharField(max_length=50000)

    def __str__(self) :
        return self.tname   
 
class btopic(models.Model):
    bt_id = models.CharField(max_length=500)
    btname=models.CharField(max_length=500)
    bsurano=models.IntegerField()
    bsuraname=models.CharField(max_length=100)
    bverseno=models.CharField(max_length=200)
    bverse=models.CharField(max_length=50000)

    def __str__(self) :
        return self.btname      

#=============================
class spl(models.Model):
    av=models.CharField(max_length=1000) #arabic verse
    eu=models.CharField(max_length=1000)#  pronunciation word by word
    v=models.CharField(max_length=50000) #English translation exact verse with surano and verse no
    q=models.CharField(max_length=50000) #question
    

    def __str__(self) :
        return self.v   
 
class bspl(models.Model):
    bav=models.CharField(max_length=10000) #arabic verse
    bu=models.CharField(max_length=10000)#  pronunciation word by word
    bv=models.CharField(max_length=50000) #bangla translation exact verse with surano and verse no
    bq=models.CharField(max_length=50000) #question and traditional translation
    

    def __str__(self) :
        return self.bv      
    
#===========================================       
class Contact(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    desc = models.TextField(max_length=5000, null=True)

    class Meta:
        verbose_name_plural = "Contacts"


