from django.db import models


class school(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    desc = models.CharField(max_length=1000,blank=True,null=True)
    school_type = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    website = models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField(default="media/uni1.png")
    
    # many to many relationiships
    # degree = models.ManyToManyField(degree_programs,blank=True)
    # hnd = models.ManyToManyField(hnd_programs,blank=True)
    # diploma = models.ManyToManyField(diploma_programs,blank=True)
    
    def __str__(self):
        return self.name
    

class degree_type(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name

class hnd_programs(models.Model):
    name = models.CharField(max_length=200, blank=True,null=True)
    school = models.ForeignKey(school,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=50,blank=True,null=True)
    d_type = models.ForeignKey(degree_type,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(default="media/uni2.png")
    
    duration = models.CharField(max_length=50,null=True,blank=True)
    department = models.CharField(max_length=50,null=True,blank=True)
    mode = models.CharField(max_length=50,null=True,blank=True)
    about = models.CharField(max_length=2000,null=True,blank=True)
    readmore = models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    
class degree_programs(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    school = models.ForeignKey(school,on_delete=models.CASCADE,null=True)
    type = models.CharField( max_length=50,blank=True,null=True)
    d_type = models.ForeignKey(degree_type,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(default="media/uni2.png")
    
    duration = models.CharField(max_length=50,null=True,blank=True)
    department = models.CharField(max_length=50,null=True,blank=True)
    mode = models.CharField(max_length=50,null=True,blank=True)
    about = models.CharField(max_length=2000,null=True,blank=True)
    readmore = models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return self.name

class diploma_programs(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    school = models.ForeignKey(school,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length = 50,blank=True,null=True)
    d_type = models.ForeignKey(degree_type,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(default="media/uni2.png")
    
    duration = models.CharField(max_length=50,null=True,blank=True)
    department = models.CharField(max_length=50,null=True,blank=True)
    mode = models.CharField(max_length=50,null=True,blank=True)
    about = models.CharField(max_length=2000,null=True,blank=True)
    readmore = models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    

