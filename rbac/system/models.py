from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser 

class Role(models.Model): 
    ROLE_CHOICES = [ 
            ('SUPERADMIN', 'Super Admin'), 
            ('GENERAL_MANAGER', 'General Manager'), 
            ('OPERATIONS_MANAGER', 'Operations Manager'), 
            ('DEPARTMENT_HEAD', 'Department Head'), 
            ('UNDERWRITER', 'Underwriter'), 
            ('SALES_MANAGER', 'Sales Manager'), 
            ('TELECALLERS', 'Telecaller'), 
            ('ACCOUNTS', 'Accounts'), 
            ('CUSTOMERS', 'Customer'), 
        ] 
    name = models.CharField(max_length=30, choices=ROLE_CHOICES, unique=True) 
    level = models.IntegerField()   

    def __str__(self): 
        return self.name 

class Feature(models.Model):
    FEATURE_CHOICES = [ 
            ('CUSTOM USER MODEL', 'User Model'), 
            ('ROLE HIERARCHY ENFORCEMENT', 'Role Hierarchy Enforcement'), 
            ('USER CREATION & MODIFICATION', 'User Creation & Modification'), 
            ('CUSTOMER ONBOARDING', 'Customer Onboarding'), 
            ('AUDIT LOGGING READY', 'Audit Logging Ready'), 
        ] 
    name = models.CharField(max_length=30, choices=FEATURE_CHOICES, unique=True) 
    level = models.IntegerField()   
    def __str__(self1): 
        return self1.name  

class UserFlow(models.Model):
    USERFLOW_CHOICES = [ 
            ('SUPERADMIN CREATES GENERAL MANAGER', 'General Manager'), 
            ('GENERAL MANAGER CREATE OPERATIONS MANAGER', 'Operations Manager'), 
            ('OPERATIONS MANAGER CREATE DEPARTMENT HEAD/SALES MANAGER', 'Department Head/Sales Manager'), 
            ('SALES MANAGER CREATE TELECALLERS', 'Telecallers'), 
            ('TELECALLERS CREATE CUSTOMERS', 'Customers'),
            ('UNDERWRITER HANDLES APPROVALS','Underwriter' ),
            ('ACCOUNTS MANAGES FINANCIAL ACTIONS','Accounts'), 
        ] 
    name = models.CharField(max_length=60, choices=USERFLOW_CHOICES, unique=True) 
    level = models.IntegerField()   
    def __str__(self): 
        return self.name 

class Security(models.Model):
    SECURITY_CHOICES = [ 
            ('HIERARCHICAL PERMISSION CONTROL', 'Hierarchical Permission'), 
            ('RESTRICTED ACCESS LEVELS', 'Restricted Access'), 
            ('API-BASED DESIGN', 'API-Based Design'), 
        ] 
    name = models.CharField(max_length=60, choices=SECURITY_CHOICES, unique=True) 
    level = models.IntegerField()   
    def __str__(self): 
        return self.name  

class User(AbstractUser): 
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True) 
    phone = models.CharField(max_length=15, blank=True, null=True) 
    is_verified = models.BooleanField(default=False) 

    def __str__(self): 
        return self.username 

