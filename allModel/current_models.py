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
    id = models.IntegerField(db_column='ID') # Field name made lowercase.
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

class SuFactorsAndQuestions(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    question = models.ForeignKey('SuQuestions')
    subfactor = models.ForeignKey('SuSubFactors', blank=True, null=True)
    created_date = models.CharField(max_length=50, blank=True)
    created_by = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'su_factors_and_questions'

class SuMainFactors(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    factor = models.CharField(db_column='Factor', max_length=100) # Field name made lowercase.
    surey = models.ForeignKey('SuSurey', db_column='Surey_ID', blank=True, null=True) # Field name made lowercase.
    questions = models.ForeignKey('SuQuestions', db_column='Questions_ID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'su_main_factors'

class SuOrganization(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact_number = models.CharField(db_column='Contact_number', max_length=100) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'su_organization'

class SuQuestions(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    question = models.CharField(db_column='Question', max_length=500) # Field name made lowercase.
    legat_scale = models.IntegerField(blank=True, null=True)
    create_date = models.CharField(db_column='Create_date', max_length=50, blank=True) # Field name made lowercase.
    update_date = models.CharField(db_column='Update_date', max_length=50, blank=True) # Field name made lowercase.
    create_by = models.IntegerField(blank=True, null=True)
    update_by = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'su_questions'

class SuSubFactorAvarage(models.Model):
    id = models.IntegerField(primary_key=True)
    survey = models.ForeignKey('SuSurey')
    subfactor = models.ForeignKey('SuSubFactors')
    number_of_emp = models.IntegerField()
    sum = models.FloatField()
    avarage = models.FloatField()
    critical = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'su_sub_factor_avarage'

class SuSubFactors(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    factor = models.CharField(db_column='Factor', max_length=20, blank=True) # Field name made lowercase.
    main_factor = models.ForeignKey(SuMainFactors, db_column='Main_factor_ID') # Field name made lowercase.
    surey = models.ForeignKey('SuSurey', db_column='Surey_ID', blank=True, null=True) # Field name made lowercase.
    questions = models.ForeignKey(SuQuestions, db_column='Questions_ID', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'su_sub_factors'

class SuSurey(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    su_name = models.CharField(db_column='su_Name', max_length=30) # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True) # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration') # Field name made lowercase.
    audience = models.CharField(db_column='Audience', max_length=20, blank=True) # Field name made lowercase.
    start_date = models.CharField(db_column='Start_date', max_length=50, blank=True) # Field name made lowercase.
    end_date = models.CharField(db_column='End_date', max_length=50, blank=True) # Field name made lowercase.
    create_date = models.CharField(db_column='Create_date', max_length=50, blank=True) # Field name made lowercase.
    update_date = models.CharField(db_column='Update_date', max_length=50, blank=True) # Field name made lowercase.
    create_by = models.IntegerField(db_column='Create_by', blank=True, null=True) # Field name made lowercase.
    update_by = models.IntegerField(db_column='Update_by', blank=True, null=True) # Field name made lowercase.
    is_active = models.IntegerField(blank=True, null=True)
    active_date = models.CharField(max_length=50, blank=True)
    org = models.ForeignKey(SuOrganization)
    class Meta:
        managed = False
        db_table = 'su_surey'

class SuSureyAndQuestions(models.Model):
    surey = models.ForeignKey(SuSurey, db_column='Surey_ID') # Field name made lowercase.
    questions = models.ForeignKey(SuQuestions, db_column='Questions_ID') # Field name made lowercase.
    create_date = models.CharField(db_column='Create_date', max_length=50, blank=True) # Field name made lowercase.
    update_date = models.CharField(db_column='Update_date', max_length=50, blank=True) # Field name made lowercase.
    create_by = models.IntegerField(blank=True, null=True)
    update_by = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'su_surey_and_questions'

class SuSureyAndUser(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    surey = models.ForeignKey(SuSurey, db_column='Surey_ID') # Field name made lowercase.
    user = models.ForeignKey('SuUser', db_column='User_ID') # Field name made lowercase.
    create_date = models.CharField(db_column='Create_date', max_length=50, blank=True) # Field name made lowercase.
    update_date = models.CharField(db_column='Update_date', max_length=50, blank=True) # Field name made lowercase.
    create_by = models.IntegerField(db_column='Create_by', blank=True, null=True) # Field name made lowercase.
    update_by = models.IntegerField(db_column='Update_by', blank=True, null=True) # Field name made lowercase.
    is_answered = models.IntegerField(blank=True, null=True)
    answered_date = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'su_surey_and_user'

class SuSureyDeptOrg(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    surey = models.ForeignKey(SuSurey)
    org = models.ForeignKey(SuOrganization)
    dept = models.ForeignKey('SuUserDepartment')
    created_date = models.CharField(max_length=50, blank=True)
    created_by = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'su_surey_dept_org'

class SuSureyFactorsAndQuestions(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    surey = models.ForeignKey(SuSurey)
    question = models.ForeignKey(SuQuestions)
    subfactor = models.ForeignKey(SuSubFactors, blank=True, null=True)
    created_date = models.CharField(max_length=50, blank=True)
    created_by = models.IntegerField()
    question_subfactor = models.ForeignKey(SuFactorsAndQuestions, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'su_surey_factors_and_questions'

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
    username = models.CharField(unique=True, max_length=100)
    org = models.ForeignKey(SuOrganization)
    dept = models.ForeignKey('SuUserDepartment', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'su_user'

class SuUser11(models.Model):
    is_admin = models.IntegerField(blank=True, null=True)
    is_hr = models.IntegerField(db_column='is_HR', blank=True, null=True) # Field name made lowercase.
    is_emp = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'su_user11'

class SuUserAndAnswers(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    surey = models.ForeignKey(SuSurey)
    question = models.ForeignKey(SuQuestions)
    catorgory = models.ForeignKey(SuSureyFactorsAndQuestions)
    answered_date = models.CharField(max_length=50, blank=True)
    answer_by = models.IntegerField()
    ligat_scale = models.IntegerField(blank=True, null=True)
    answer = models.CharField(max_length=200, blank=True)
    class Meta:
        managed = False
        db_table = 'su_user_and_answers'

class SuUserDepartment(models.Model):
    id = models.IntegerField(db_column='ID') # Field name made lowercase.
    user = models.ForeignKey(SuUser, db_column='User_ID') # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=75, blank=True) # Field name made lowercase.
    dept_name = models.CharField(db_column='Dept_name', max_length=20, blank=True) # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True) # Field name made lowercase.
    contact_number = models.CharField(db_column='Contact_number', max_length=10, blank=True) # Field name made lowercase.
    org = models.ForeignKey(SuOrganization, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'su_user_department'

