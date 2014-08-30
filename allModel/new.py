# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class SuContacts(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    user = models.ForeignKey(AuthUser, db_column='User_ID') # Field name made lowercase.
    contact_number = models.CharField(db_column='Contact_number', max_length=10, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'su_contacts'

class SuDeptContacts(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    dept = models.ForeignKey('SuUserDepartment', db_column='Dept_ID', blank=True, null=True) # Field name made lowercase.
    contact_number = models.CharField(db_column='Contact_number', max_length=10, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'su_dept_contacts'

class SuMainFactors(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    factor = models.CharField(db_column='Factor', max_length=20, blank=True) # Field name made lowercase.
    surey = models.ForeignKey('SuSurey', db_column='Surey_ID') # Field name made lowercase.
    questions = models.ForeignKey('SuQuestions', db_column='Questions_ID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'su_main_factors'

class SuQuestions(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    question = models.CharField(db_column='Question', max_length=100) # Field name made lowercase.
    catagory = models.CharField(db_column='Catagory', max_length=50, blank=True) # Field name made lowercase.
    create_date = models.DateTimeField(db_column='Create_date', blank=True, null=True) # Field name made lowercase.
    update_date = models.DateTimeField(db_column='Update_date', blank=True, null=True) # Field name made lowercase.
    create_by = models.IntegerField(blank=True, null=True)
    update_by = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'su_questions'

class SuSubFactors(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    factor = models.CharField(db_column='Factor', max_length=20, blank=True) # Field name made lowercase.
    main_factor = models.ForeignKey(SuMainFactors, db_column='Main_factor_ID') # Field name made lowercase.
    surey = models.ForeignKey('SuSurey', db_column='Surey_ID') # Field name made lowercase.
    questions = models.ForeignKey(SuQuestions, db_column='Questions_ID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'su_sub_factors'

class SuSueryAndQuestions(models.Model):
    surey = models.ForeignKey('SuSurey', db_column='Surey_ID') # Field name made lowercase.
    questions = models.ForeignKey(SuQuestions, db_column='Questions_ID') # Field name made lowercase.
    create_date = models.DateTimeField(db_column='Create_date', blank=True, null=True) # Field name made lowercase.
    update_date = models.DateTimeField(db_column='Update_date', blank=True, null=True) # Field name made lowercase.
    create_by = models.IntegerField(blank=True, null=True)
    update_by = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'su_suery_and_questions'

class SuSurey(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    su_name = models.CharField(db_column='su_Name', max_length=30) # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True) # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration') # Field name made lowercase.
    audience = models.CharField(db_column='Audience', max_length=20, blank=True) # Field name made lowercase.
    start_date = models.DateTimeField(db_column='Start_date', blank=True, null=True) # Field name made lowercase.
    end_date = models.DateTimeField(db_column='End_date', blank=True, null=True) # Field name made lowercase.
    create_date = models.DateTimeField(db_column='Create_date', blank=True, null=True) # Field name made lowercase.
    update_date = models.DateTimeField(db_column='Update_date', blank=True, null=True) # Field name made lowercase.
    create_by = models.IntegerField(db_column='Create_by', blank=True, null=True) # Field name made lowercase.
    update_by = models.IntegerField(db_column='Update_by', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'su_surey'

class SuSureyAndUser(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    surey = models.ForeignKey(SuSurey, db_column='Surey_ID') # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_ID') # Field name made lowercase.
    create_date = models.DateTimeField(db_column='Create_date', blank=True, null=True) # Field name made lowercase.
    update_date = models.DateTimeField(db_column='Update_date', blank=True, null=True) # Field name made lowercase.
    create_by = models.IntegerField(db_column='Create_by', blank=True, null=True) # Field name made lowercase.
    update_by = models.IntegerField(db_column='Update_by', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'su_surey_and_user'

class SuUser(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    last_login = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_admin = models.IntegerField(blank=True, null=True)
    is_hr = models.IntegerField(db_column='is_HR', blank=True, null=True) # Field name made lowercase.
    is_emp = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    date_join = models.DateTimeField(blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=75, blank=True) # Field name made lowercase.
    password = models.CharField(max_length=10, blank=True)
    user_id = models.IntegerField(blank=True, null=True)
    def __unicode__(self):
        return self.first_name
    class Meta:
        managed = False
        db_table = 'su_user'
# def create_user_callback(sender,instance,**kwargs):
#     user,new =SuUser.objects.get_or_create(user=instance)
# post_save.connect(create_user_callback,User)




class SuUserDepartment(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    user = models.ForeignKey(SuUser, db_column='User_ID') # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=10, blank=True) # Field name made lowercase.
    dept_name = models.CharField(db_column='Dept_name', max_length=20, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'su_user_department'

