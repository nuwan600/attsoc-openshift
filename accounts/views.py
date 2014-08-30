from django.shortcuts import render, redirect, get_object_or_404,render_to_response,RequestContext
from django.forms import ModelForm
from django.http import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.context_processors import request
from django.core.context_processors import request
from django.http import HttpResponse
from httplib import HTTPResponse
from django.template import Context,loader
from twisted.test.test_sip import request1
from allModel.models import *
from django.http.response import HttpResponseRedirect
from django.conf import settings
from xmlrpclib import datetime
from django.core.exceptions import ValidationError
from surveys.views import random_username,random_pw
from MySQLdb.constants.FIELD_TYPE import NULL


# Create your views here.


def index(request):
    
    return render_to_response("index.html",locals(),context_instance=RequestContext(request))


def admin(request):
    try:
        request.session['user_login_data']
        if request.session['user_login_data']['is_admin']==1:
            survey_count=survey_count=SuSureyDeptOrg.objects.filter(org=request.session['user_login_data']['org']).count()
            user_count=SuUser.objects.filter(org=request.session['user_login_data']['org']).count()
            return  render_to_response("Admin.html",{'survey_count':survey_count,'user_count':user_count},context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/attsoc/error405')
    except KeyError, e:
        messages={'alert':'No activity within 120 minutes; please log in again'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request))


def HR(request):
    
    try:
        request.session['user_login_data']
        if request.session['user_login_data']['is_HR']==1:
            su_data=SuSurey.objects.filter(create_by=request.session['user_login_data']['id'])
            survey_count=SuSureyDeptOrg.objects.filter(surey=su_data,org=request.session['user_login_data']['org']).count()
            #survey_count=SuSurey.objects.filter(create_by=request.session['user_login_data']['id']).count()
            user_count=SuUser.objects.filter(org=request.session['user_login_data']['org']).count()
            return  render_to_response("HR.html",{'survey_count':survey_count,'user_count':user_count},context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/attsoc/error405')
    except KeyError, e:
        messages={'alert':'No activity within 120 minutes; please log in again'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request))


def emp(request):
    
    try:
        request.session['user_login_data']
        if request.session['user_login_data']['is_emp']==1:
            ss=request.session['user_login_data']['id']
            current_user=SuUser.objects.get(id=request.session['user_login_data']['id'])
            
            survey_user_data=SuSureyAndUser.objects.filter(user=current_user)
            survey_user_data_answered_count=SuSureyAndUser.objects.filter(user=current_user,is_answered=1)
            survey_user_data_all_count=SuSureyAndUser.objects.filter(user=current_user).count()
            return  render_to_response("allempsurevy.html",{'survey_user_data':survey_user_data,'answered_count':survey_user_data_answered_count,'all_count':survey_user_data_all_count},context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/attsoc/error405')
    except KeyError, e:
        messages={'alert':'No activity within 120 minutes; please log in again'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request))


def emp_survey_Answre(request,survey_id):
    return  render_to_response("empAnswresfrom.html",locals(),context_instance=RequestContext(request))

def auth(request):
    
    if 'user_login_date' not in request.session:
        if request.method == 'POST': 
            request.session.clear_expired()
         
            try:
                SuUser.objects.get(username=request.POST.get('username',''))
                user_data= SuUser()
                 
                user_data=SuUser.objects.get(username=request.POST.get('username',''))
                
                if user_data.password==request.POST.get('password',''):
                    
                    request.session['user_login_data']={}
                    request.session['user_login_data']['id']=user_data.id
                    request.session['user_login_data']['last_login']=user_data.last_login
                    request.session['user_login_data']['first_name']=user_data.first_name
                    request.session['user_login_data']['last_name']=user_data.last_name
                    request.session['user_login_data']['is_admin']=user_data.is_admin
                    request.session['user_login_data']['is_HR']=user_data.is_hr
                    request.session['user_login_data']['is_emp']=user_data.is_emp
                    request.session['user_login_data']['is_active']=user_data.is_active
                    request.session['user_login_data']['date_join']=user_data.date_join
                    request.session['user_login_data']['email']=user_data.email
                    request.session['user_login_data']['password']=user_data.password
                    request.session['user_login_data']['username']=user_data.username
                    request.session['user_login_data']['org']=user_data.org
                    request.session['user_login_data']['org_id']=user_data.org.id
                    request.session['user_login_data']['org_name']=user_data.org.name
                    request.session['user_login_data']['dept']=user_data.dept
                    request.session['user_login_data']['dept_id']=user_data.dept.id
                    request.session['user_login_data']['dept_name']=user_data.dept.dept_name
                    
                    #request.session.set_expiry(30)
                    if user_data.is_active==1:
                        sss= request.session['user_login_data']['org']
                        if user_data.is_admin==1:
                            user=SuUser.objects.get(id=user_data.id)
                            user.last_login=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            user.save(update_fields=['last_login'])
                            return HttpResponseRedirect('/attsoc/admin')
                            #return  render_to_response("Admin.html",locals(),context_instance=RequestContext(request))
                             
                        elif user_data.is_hr==1:
                            user=SuUser.objects.get(id=user_data.id)
                            user.last_login=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            user.save(update_fields=['last_login'])
                            return HttpResponseRedirect('/attsoc/HR')
                            #return  render_to_response("HR.html",locals(),context_instance=RequestContext(request))
                         
                        elif user_data.is_emp==1:
                            user=SuUser.objects.get(id=user_data.id)
                            user.last_login=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            user.save(update_fields=['last_login'])
                            return HttpResponseRedirect('/attsoc/emp')
                            #return  render_to_response("HR.html",locals(),context_instance=RequestContext(request))
                        
                    else:
                        messages={'error': 'Your account is not activated'}
                        return render(request, 'index.html',{'messages': messages})
                        #return HttpResponseRedirect('/')
        
                else:
                    messages={'error': 'invalide password'}
                    return render(request, 'index.html',{'messages': messages})
                
            except SuUser.DoesNotExist:
                messages={'error': 'username or password invalide '}
                return render(request, 'index.html',{'messages': messages})
                 
                
                     
            
                    #return render_to_response("index.html",locals(),context_instance=RequestContext(request))
    
        else:
            return  render_to_response("Admin.html",locals(),context_instance=RequestContext(request))
        

def error405(request):
    try:
        request.session['user_login_data']
        return  render_to_response("405.html",locals(),context_instance=RequestContext(request))
        
    except KeyError, e:
        messages={'alert':'No activity within 120 minutes; please log in again'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request))


def register(request):
    try:
        request.session['user_login_data']
        if request.method == 'POST':
            
                if  'Users' not in request.POST:
                    if request.POST.get('password','')==request.POST.get('con_password',''):
                        
                        if request.POST.get('admin','')== 'on' or request.POST.get('HR','')== 'on':
                            user_date=SuUser
                            if request.POST.get('admin','')== 'on':
                                if request.POST.get('active','')== 'on':
                                    user_date=SuUser(first_name=request.POST.get('first_name',''),last_name=request.POST.get('last_name',''),is_admin=1,is_active=1,date_join=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),email=request.POST.get('email',''),password=request.POST.get('password',''),user_id=request.session['user_login_data']['id'],username=request.POST.get('username',''),org=request.session['user_login_data']['org'])
                                else:
                                    user_date=SuUser(first_name=request.POST.get('first_name',''),last_name=request.POST.get('last_name',''),is_admin=1,date_join=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),email=request.POST.get('email',''),password=request.POST.get('password',''),user_id=request.session['user_login_data']['id'],username=request.POST.get('username',''),org=request.session['user_login_data']['org'])
                                
                            else:
                                if request.POST.get('active','')== 'on':
                                    user_date=SuUser(first_name=request.POST.get('first_name',''),last_name=request.POST.get('last_name',''),is_hr=1,is_active=1,date_join=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),email=request.POST.get('email',''),password=request.POST.get('password',''),user_id=request.session['user_login_data']['id'],username=request.POST.get('username',''),org=request.session['user_login_data']['org'])
                                else:
                                    user_date=SuUser(first_name=request.POST.get('first_name',''),last_name=request.POST.get('last_name',''),is_hr=1,date_join=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),email=request.POST.get('email',''),password=request.POST.get('password',''),user_id=request.session['user_login_data']['id'],username=request.POST.get('username',''),org=request.session['user_login_data']['org'])
                                
                            try:
                                user_date.full_clean()
                                user_date.save(True,False,None, None)
                                messages={'success':'Successfuly saved'}
                                return render(request, 'pages/forms/register.html',{'messages':messages},context_instance=RequestContext(request))
                    
                            
                            except ValidationError as e:
                                messages={'error':e.messages}
                                return render(request, 'pages/forms/register.html',{'messages':messages},context_instance=RequestContext(request))
                        else:
                            messages={'error':'Please click HR or Admin '}
                            return render(request, 'pages/forms/register.html',{'messages':messages},context_instance=RequestContext(request))
                    
                        
                        
                    else:
                        messages={'error':'Please enter the same password'}
                        return render(request, 'pages/forms/register.html',{'messages':messages},context_instance=RequestContext(request))
                    
                else:
                    user_count=request.POST.get('Users','')
                    
                    for i in range(0,int(user_count)):
                        user_data=SuUser(username=random_username(8),password=random_pw(),is_emp=1,is_active=1,user_id=request.session['user_login_data']['id'],date_join=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),org=request.session['user_login_data']['org'])
                
                        try:
                            user_data.full_clean()
                            user_data.save(True,False,None, None)
                        
                        except ValidationError as e:
                                messages={'error':e.messages}
                                return render(request, 'pages/forms/register.html',{'messages':messages},context_instance=RequestContext(request))
                    
                    messages={'success':'Successfuly saved'}
                    return render(request, 'pages/forms/register.html',{'messages':messages},context_instance=RequestContext(request))
              
        else:
            return render(request, 'pages/forms/register.html',locals(),context_instance=RequestContext(request))
        
        
    except KeyError, e:
        messages={'alert':'No activity within 120 minutes; please log in again'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request))
  
      
def logout(request):
    try:
        request.session['user_login_data']
        del request.session['user_login_data']
        return HttpResponseRedirect('/')
    except KeyError, e:
        return HttpResponseRedirect('/')
    
def allusers(request):
    
    try:
        request.session['user_login_data']
        
        user_admin=SuUser.objects.filter(org=request.session['user_login_data']['org'],is_admin=1)
        user_hr=SuUser.objects.filter(org=request.session['user_login_data']['org'],is_hr=1)
        user_emp=SuUser.objects.filter(org=request.session['user_login_data']['org'],is_emp=1)
        
        admin_count=SuUser.objects.filter(org=request.session['user_login_data']['org'],is_admin=1).count()
        hr_count=SuUser.objects.filter(org=request.session['user_login_data']['org'],is_hr=1).count()
        emp_count=SuUser.objects.filter(org=request.session['user_login_data']['org'],is_emp=1).count()
        
        counts={'admin_count':admin_count,'hr_count':hr_count,'emp_count':emp_count}
        return  render_to_response("pages/forms/allUsers.html",{'user_admin':user_admin,'user_hr':user_hr,'user_emp':user_emp,'counts':counts},context_instance=RequestContext(request))
        
    except KeyError, e:
        messages={'alert':'No activity within 120 minutes; please log in again'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request))



def editusers(request,user_id=0):
    
    try:
        request.session['user_login_data']
        user_data=SuUser.objects.get(id=user_id)
        if request.method == 'POST':
            if request.POST.get('password','')==request.POST.get('con_password',''):
                        
                        if request.POST.get('admin','')== 'on' or request.POST.get('HR','')== 'on':
                            
                            if request.POST.get('admin','')== 'on':
                                
                                user_data.first_name=request.POST.get('first_name','')
                                user_data.last_name=request.POST.get('last_name','')
                                user_data.is_hr=NULL
                                user_data.is_admin=1
                                
                                if request.POST.get('active','')== 'on':
                                    user_data.is_active=1
                                else:
                                    user_data.is_active=NULL
                                    
                                user_data.date_join=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                user_data.email=request.POST.get('email','')
                                user_data.password=request.POST.get('password','')
                                user_data.username=request.POST.get('username','')
                                
                                
                            else:
                                user_data.first_name=request.POST.get('first_name','')
                                user_data.last_name=request.POST.get('last_name','')
                                user_data.is_hr=1
                                user_data.is_admin=NULL
                                
                                if request.POST.get('active','')== 'on':
                                    user_data.is_active=1
                                else:
                                    user_data.is_active=NULL
                                    
                                user_data.date_join=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                user_data.email=request.POST.get('email','')
                                user_data.password=request.POST.get('password','')
                                user_data.username=request.POST.get('username','')
                                
                            try:
                                user_data.full_clean()
                                user_data.save(update_fields=['first_name','last_name','is_hr','is_admin','is_active','date_join','email','password','username'])
                                messages={'success':'Successfuly saved'}
                                return HttpResponseRedirect('/accounts/allusers')
                                #return render(request, 'pages/forms/register.html',{'messages':messages,'user_data':user_data,'user_id':user_id},context_instance=RequestContext(request))
                    
                            
                            except ValidationError as e:
                                user_data=SuUser.objects.get(id=user_id)
                                messages={'error':e.messages}
                                return render(request, 'pages/forms/edituser.html',{'messages':messages,'user_data':user_data,'user_id':user_id},context_instance=RequestContext(request))
                        else:
                            messages={'error':'Please click HR or Admin '}
                            user_data=SuUser.objects.get(id=user_id)
                            return render(request, 'pages/forms/edituser.html',{'messages':messages,'user_data':user_data,'user_id':user_id},context_instance=RequestContext(request))
                    
                        
                        
            else:
                messages={'error':'Please enter the same password'}
                user_data=SuUser.objects.get(id=user_id)
                return render(request, 'pages/forms/edituser.html',{'messages':messages,'user_data':user_data,'user_id':user_id},context_instance=RequestContext(request))
                   
            
        else:
            user_data=SuUser.objects.get(id=user_id)
            return  render_to_response("pages/forms/edituser.html",{'user_data':user_data,'user_id':user_id},context_instance=RequestContext(request))
        
        
    except KeyError, e:
        messages={'alert':'No activity within 120 minutes; please log in again'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request))
   