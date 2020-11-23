from django.db import models

class mhs(models.Model):
      nama=models.CharField(max_length=100)
      ttl=models.CharField(max_length=100) 
      alamat=models.CharField(max_length=100) 
      jalan=models.CharField(max_length=100) 

      class Meta: 
          db_table='api_mhs'  
            

 
 