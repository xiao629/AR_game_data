from django.db import models
import django.utils.timezone

class kstest(models.Model):
    ks_id  =models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    ks_name=models.CharField(max_length=20,default='請輸入名字')
    ks_time=models.DateTimeField(max_length=6,default=django.utils.timezone.now)
    ks_temperature=models.IntegerField(null=False,default='0')
    
    class Meta:
        db_table="posts_kstest"
    



