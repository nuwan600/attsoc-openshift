from django.shortcuts import render, redirect, get_object_or_404,render_to_response,RequestContext
from django.forms import ModelForm
from django.http import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.context_processors import request
from django.core.context_processors import request
from django.core import serializers
from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponseRedirect
from httplib import HTTPResponse
from django.core.urlresolvers import reverse
from django.template import Context,loader
from allModel.models import *
from django.core.exceptions import ValidationError
from xmlrpclib import datetime
from django.db.models import Q
import random, string,json
from numpy.lib.function_base import range
from django.views.decorators.csrf import csrf_exempt
#from numpy.lib.function_base import range
import numpy.lib.function_base
import classify_knn as classify_knn
import os




#---- random username creater ----#   
def random_username(length):
    return ''.join(random.choice(string.lowercase + datetime.datetime.now().strftime("%Y%m%d%H%M%S") ) for i in range(length))  



#---- random password creater ----#  
def random_pw():

    
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pw_length = 8
    mypw = ""

    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        mypw = mypw + alphabet[next_index]

    return mypw




def allsurveys(request):
     
    try:
        request.session['user_login_data']
        #surey_data=SuSurey.objects.all()
        survey_count=SuSureyDeptOrg.objects.filter(org=request.session['user_login_data']['org']).count()
        surey_data=SuSureyDeptOrg.objects.filter(org=request.session['user_login_data']['org'])
        
        if request.session['user_login_data']['is_HR']==1:
            su_data=SuSurey.objects.filter(create_by=request.session['user_login_data']['id'])
            surey_data=SuSureyDeptOrg.objects.filter(surey=su_data,org=request.session['user_login_data']['org'])
        
            #surey_data=SuSurey.objects.filter(create_by=request.session['user_login_data']['id'])
            #surey_data=SuSureyDeptOrg.objects.filter(surey=surey_data1)
            survey_count_HR=SuSureyDeptOrg.objects.filter(surey=su_data,org=request.session['user_login_data']['org']).count()
            return  render_to_response("pages/forms/allSurvey.html",{'allSurey':surey_data,'survey_count':survey_count_HR},context_instance=RequestContext(request))
        else:
            return  render_to_response("pages/forms/allSurvey.html",{'allSurey':surey_data,'survey_count':survey_count},context_instance=RequestContext(request))
     
    except KeyError, e:
        messages={'alert':'You need to loging'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request)) 
     
    
#---- adding new surey data view ----#   
def newsurveys(request):
    
    try:
        request.session['user_login_data']
        dept_data=SuUserDepartment.objects.filter(org=request.session['user_login_data']['org'])
        return render(request, 'pages/forms/newSurvey.html',{'dept_data': dept_data},context_instance=RequestContext(request))   
        
    
    except KeyError, e:
        messages={'alert':'No activity within 120 minutes; please log in again'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request))   
     
        
#---- view ad publish surey data ----#
def viewsurveys(request,survey_id=0,dept_id=0):
    
    try:
        request.session['user_login_data']
        dept_data=SuUserDepartment.objects.filter(org=request.session['user_login_data']['org'])
        dept=SuUserDepartment.objects.get(id=dept_id)
        if request.method == 'POST':
            user_count=request.POST.get('Users','')
            
            for i in range(0,int(user_count)):
                 
                user_data=SuUser(username=random_username(8),password=random_pw(),is_emp=1,is_active=1,user_id=request.session['user_login_data']['id'],date_join=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),org=request.session['user_login_data']['org'],dept=dept)
                
                try:
                    user_data.full_clean()
                    user_data.save(True,False,None, None)
                    
                    suuser_date=SuUser.objects.get(pk=user_data.id)
                    surey_data=SuSurey.objects.get(pk=survey_id)
                    user_surey_date=SuSureyAndUser(surey=surey_data,user=suuser_date,create_by=request.session['user_login_data']['id'],create_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    
                    try:
                        user_surey_date.full_clean()
                        user_surey_date.save(True,False,None, None)
                        
                        
                    except ValidationError as e:
                        
                        messages={'error':e.messages}
                        surey_data=SuSurey.objects.get(id=survey_id)
                        return render(request, 'pages/forms/publish.html',{'dept_data':dept_data,'surey_data':surey_data ,'messages': messages,'survey_id':survey_id,'dept_id':dept_id},context_instance=RequestContext(request))   
    
                except ValidationError as e:
                    messages={'error':e.messages}
                    surey_data=SuSurey.objects.get(id=survey_id)
                    return render(request, 'pages/forms/publish.html',{'dept_data':dept_data,'surey_data':surey_data ,'messages': messages,'survey_id':survey_id,'dept_id':dept_id},context_instance=RequestContext(request))   
    
           
           
            messages={'success':'Successfuly data added'}
            surey_data=SuSurey.objects.get(id=survey_id)
            #return render(request, 'pages/forms/publishSurveys.html',{'survey_id': survey_id,'dept_id': dept_id ,'messages': messages},context_instance=RequestContext(request))
            url = reverse('publishSurveys', kwargs={'survey_id': survey_id,'dept_id': dept_id })
            return HttpResponseRedirect(url)   
    
        else:
            surey_data=SuSurey.objects.get(id=survey_id)
            return  render_to_response("pages/forms/publish.html",{'dept_data':dept_data,'surey_data':surey_data, 'survey_id':survey_id,'dept_id':dept_id },context_instance=RequestContext(request))
    
    except KeyError, e:
        messages={'alert':'No activity within 120 minutes; please log in again'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request))   
   
    
#---- editing surey data ----#
def editsurveys(request,survey_id=0):
    
    try:
        request.session['user_login_data']
      
        if request.method == 'POST':
            date=request.POST.get('dates','').split('-')
            survey_data=SuSurey.objects.get(id=survey_id)
            survey_data.su_name=request.POST.get('Name','')
            survey_data.description=request.POST.get('Description','')
            survey_data.duration=request.POST.get('Duration','')
            survey_data.audience=request.POST.get('Audience','')
            survey_data.start_date=date[0]
            survey_data.end_date=date[1]
            survey_data.update_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            survey_data.update_by=request.session['user_login_data']['id']

            try:
               
                survey_data.save(update_fields=['su_name','description','duration','audience','start_date','end_date','update_date','update_by'])
                
                messages={'success':'Successfuly data added'}
                all_surey_data=SuSurey.objects.filter(create_by=request.session['user_login_data']['id'])
                surey_data=SuSurey.objects.get(id=survey_id)
                dept_data=SuUserDepartment.objects.all()
                return  render_to_response("pages/forms/edit_Survey_questions.html",{'dept_data': dept_data,'surey_data':surey_data, 'survey_id': survey_id, 'allSurey': all_surey_data },context_instance=RequestContext(request))
   
            except ValidationError as e:
                messages={'error':e.messages}
                all_surey_data=SuSurey.objects.all()
                surey_data=SuSurey.objects.get(id=survey_id)
                dept_data=SuUserDepartment.objects.all()
                return  render_to_response("pages/forms/edit_Survey_questions.html",{'messages':messages,'dept_data': dept_data,'surey_data':surey_data, 'survey_id': survey_id, 'allSurey': all_surey_data },context_instance=RequestContext(request))
          
        else:
            all_surey_data=SuSurey.objects.filter(create_by=request.session['user_login_data']['id'])
            surey_data=SuSurey.objects.get(id=survey_id)
            dept_data=SuUserDepartment.objects.all()
            return  render_to_response("pages/forms/edit_Survey_questions.html",{'dept_data': dept_data,'surey_data':surey_data, 'survey_id': survey_id, 'allSurey': all_surey_data },context_instance=RequestContext(request))
          
    except KeyError, e:
        messages={'alert':'No activity within 120 minute,Please log in again'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request))
 
      
#---- adding new surey data ----#
def addsurveys(request):
    
    try:
        request.session['user_login_data']
        if request.method == 'POST':
            date=request.POST.get('dates','').split('-')
           
            survey_data=SuSurey(su_name=request.POST.get('Name',''),description=request.POST.get('Description',''),duration=request.POST.get('Duration',''),audience=request.POST.get('Audience',''),start_date=date[0],end_date=date[1],org=request.session['user_login_data']['org'],create_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),create_by=request.session['user_login_data']['id'])
            dept_data=SuUserDepartment.objects.filter(org=request.session['user_login_data']['org'])
            selected_dept=SuUserDepartment.objects.get(id=request.POST.get('dept',''))
            
            try:
                survey_data.full_clean()
                survey_data.save(True,False,None, None)
                try:
                    survey_dept_org_date=SuSureyDeptOrg(surey=survey_data,org=selected_dept.org,dept=selected_dept,created_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),created_by=request.session['user_login_data']['id'])
                    survey_dept_org_date.full_clean()
                    survey_dept_org_date.save(True, False, None, None)
                    messages={'success':'Successfuly data added'}
                    url = reverse('addQuestionSurveys', kwargs={'survey_id': survey_data.id })
                    return HttpResponseRedirect(url)
                #return render(request, 'pages/forms/newQuestionsSurvey.html',{'dept_data': dept_data,'messages': messages,'survey_id':survey_data.id},context_instance=RequestContext(request))   
                except ValidationError as e:
                    SuSurey.objects.filter(id=survey_data.id).delete()
                    messages={'error':e.messages}
                    return render(request, 'pages/forms/newSurvey.html',{'dept_data': dept_data,'messages': messages},context_instance=RequestContext(request))   
    
            except ValidationError as e:
                messages={'error':e.messages}
                return render(request, 'pages/forms/newSurvey.html',{'dept_data': dept_data,'messages': messages},context_instance=RequestContext(request))   
    
    except KeyError, e:
        messages={'alert':'No activity within 120 minutes; please log in again'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request))
      
            
#---- add questuions and match factors ----#   

def addQuestionSurveys(request,survey_id=0):
    
    try:
        request.session['user_login_data']['id']
        allQuestions=SuQuestions.objects.all()
        if request.method == 'POST':
            question_data=SuQuestions(question=request.POST.get('Question',''),legat_scale=5,create_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),create_by=request.session['user_login_data']['id'])
            
            #replace1=request.POST.get('Question','').replace(',', '')
            #replace2=replace1.replace('?', '')
            #replace3=replace2.replace('.', '')
            txt=request.POST.get('Question','')
            #===================================================================
            # for char in string.punctuation:
            #     txt = txt.replace(char," ")
            # #txt1=txt.split(' ')
            # #final=replace3.split(' ')
            # 
            # #--- start text maching ---#
            # qset = Q()
            # for term in txt.split():
            #     qset |= Q(factor__iexact=term)
            # #--- end text maching ---#
            #===================================================================
            
            #############################
            
            # path = os.path.dirname(__file__)
            path =os.path.dirname(os.path.dirname(__file__))
            classifier = classify_knn.classify_knn(3, True, 1.0, 2.0)
            
            classifier.load(path+"/surveys/word_list.json", path+"/surveys/points.json")
            sbf = classifier.get_category(txt)
            #############################
            try:
                #matching_results=SuSubFactors.objects.extra(where=['factor IN '+txt1])
                #matching_results=SuSubFactors.objects.filter(qset)
                matching_results=SuSubFactors.objects.filter(factor=sbf)
            except ValueError,e:
                messages={'error1':'Some thing goes wrong'}
                return render(request, 'pages/forms/newQuestionsSurvey.html',{'messages': messages,'survey_id': survey_id,'allQuestions' : allQuestions},context_instance=RequestContext(request))   
            except MultipleObjectsReturned, e:
                messages={'error1':'Some thing goes wrong'}
                return render(request, 'pages/forms/newQuestionsSurvey.html',{'messages': messages,'survey_id': survey_id,'allQuestions' : allQuestions},context_instance=RequestContext(request))   
            except SuSubFactors.DoesNotExist:
                pass
            try:
                question_data.full_clean()
                question_data.save(True,False,None, None)
                
                survey_saved=SuSurey.objects.get(id=survey_id)
                questions_saved=SuQuestions.objects.get(id=question_data.id)
                
                try:
                    for results in matching_results:
                        question_factors=SuFactorsAndQuestions(question=questions_saved,subfactor=results,created_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),created_by=request.session['user_login_data']['id'])
                        try:
                            question_factors.full_clean()
                            question_factors.save(True,False,None, None)
                            question_survey_factors_data=SuSureyFactorsAndQuestions(surey=survey_saved,question=questions_saved,subfactor=results,created_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),created_by=request.session['user_login_data']['id'],question_subfactor=question_factors)
                
                            try:
                                question_survey_factors_data.full_clean()
                                question_survey_factors_data.save(True,False,None, None)
                                
                                
                            except ValidationError as e:
                                SuSureyFactorsAndQuestions.objects.filter(id=question_data.id).delete()
                                messages={'error':e.messages}
                                return render(request, 'pages/forms/newQuestionsSurvey.html',{'messages': messages,'survey_id': survey_id,'allQuestions' : allQuestions},context_instance=RequestContext(request))
                           
                        except ValidationError as e:
                                SuQuestions.objects.filter(id=question_data.id).delete()
                                messages={'error':e.messages}
                                return render(request, 'pages/forms/newQuestionsSurvey.html',{'messages': messages,'survey_id': survey_id,'allQuestions' : allQuestions},context_instance=RequestContext(request))
                    try:
                        suery_and_questions=SuSureyAndQuestions(surey=survey_saved,questions=question_data,create_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),create_by=request.session['user_login_data']['id'])
                        suery_and_questions.full_clean()
                        suery_and_questions.save(True,False,None, None)
                        messages={'success':'Successfuly question data added'}
                        return render(request, 'pages/forms/newQuestionsSurvey.html',{'messages': messages,'survey_id': survey_id,'allQuestions' : allQuestions},context_instance=RequestContext(request))   
                    except ValidationError as e:
                        messages={'error':e.messages}
                        return render(request, 'pages/forms/newQuestionsSurvey.html',{'messages': messages,'survey_id': survey_id,'allQuestions' : allQuestions},context_instance=RequestContext(request))
                          
                        
                except UnboundLocalError,e:
                    question_factors=SuFactorsAndQuestions(question=questions_saved,created_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),created_by=request.session['user_login_data']['id'])
                    try:
                        question_factors.full_clean()
                        question_factors.save(True,False,None, None)
                        
                        question_survey_factors_data=SuSureyFactorsAndQuestions(surey=survey_saved,question=questions_saved,subfactor=matching_results,created_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),created_by=request.session['user_login_data']['id'],question_subfactor=question_factors)
                
                        try:
                            question_survey_factors_data.full_clean()
                            question_survey_factors_data.save(True,False,None, None)
                            messages={'success':'Successfuly question data added, But System did not found matching factor'}
                            return render(request, 'pages/forms/newQuestionsSurvey.html',{'messages': messages,'survey_id': survey_id,'allQuestions' : allQuestions},context_instance=RequestContext(request))   
               
                        except ValidationError as e:
                            question_factors.objects.filter(id=question_data.id).delete()
                            messages={'error':e.messages}
                            return render(request, 'pages/forms/newQuestionsSurvey.html',{'messages': messages,'survey_id': survey_id,'allQuestions' : allQuestions},context_instance=RequestContext(request))         
                
                    except ValidationError as e:
                        SuQuestions.objects.filter(id=question_data.id).delete()
                        messages={'error':e.messages}
                        return render(request, 'pages/forms/newQuestionsSurvey.html',{'messages': messages,'survey_id': survey_id,'allQuestions' : allQuestions},context_instance=RequestContext(request))         
          
                    question_survey_factors_data=SuSureyFactorsAndQuestions(surey=survey_saved,question=questions_saved,created_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),created_by=request.session['user_login_data']['id'])
                
                    try:
                       
                        question_survey_factors_data.full_clean()
                        question_survey_factors_data.save(True,False,None, None)
                        
                        messages={'success':'Successfuly question data added, But System did not found matching factor'}
                        return render(request, 'pages/forms/newQuestionsSurvey.html',{'messages': messages,'survey_id': survey_id,'allQuestions' : allQuestions},context_instance=RequestContext(request))   
               
                    except ValidationError as e:
                        SuQuestions.objects.filter(id=question_data.id).delete()
                        messages={'error':e.messages}
                        return render(request, 'pages/forms/newQuestionsSurvey.html',{'messages': messages,'survey_id': survey_id,'allQuestions' : allQuestions},context_instance=RequestContext(request))         
                
            except ValidationError as e:
                
                messages={'error':e.messages}
                return render(request, 'pages/forms/newQuestionsSurvey.html',{'messages': messages,'survey_id': survey_id,'allQuestions' : allQuestions},context_instance=RequestContext(request))   
    
              
        else:
            #messages={'success':'Successfuly data added'}
            return render(request, 'pages/forms/newQuestionsSurvey.html',{'survey_id':survey_id,'allQuestions' : allQuestions},context_instance=RequestContext(request))
        
    except KeyError, e:
        allQuestions=SuQuestions.objects.all()
        messages={'alert':'No activity within 120 minutes; please log in again'}
        return render(request, 'index.html',{'messages': messages,'allQuestions' : allQuestions},context_instance=RequestContext(request)) 

#---- add questions to Surveys ----#

def addQuestion_to_Surveys(request,survey_id=0):
    try:
        request.session['user_login_data']['id']
        allQuestions=SuQuestions.objects.all()
        
        if request.method == 'POST':
            try:
                post_data=request.POST.copy()
                del post_data['csrfmiddlewaretoken']
                #post_data=post_data.pop()
                #post_data=post_data.pop()
                
                for key, value in post_data:
                    question_data=SuQuestions.objects.get(id=key)
                    survey_data=SuSurey.objects.get(id=survey_id)
                    suery_and_questions=SuSureyAndQuestions(surey=survey_data,questions=question_data,create_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),create_by=request.session['user_login_data']['id'])
                    suery_and_questions.full_clean()
                    suery_and_questions.save(True,False,None, None)
                    
                       
                messages={'success':'Successfuly question data added'}
                return render(request, 'pages/forms/newQuestionsSurvey.html',{'messages': messages,'survey_id': survey_id,'allQuestions' : allQuestions},context_instance=RequestContext(request))   
            except ValidationError as e:
                    
                    messages={'error':e.messages}
                    return render(request, 'pages/forms/newQuestionsSurvey.html',{'messages': messages,'survey_id':survey_id,'allQuestions' : allQuestions},context_instance=RequestContext(request))
 
            
        else:
            #messages={'success':'Successfuly data added'}
            return render(request, 'pages/forms/newQuestionsSurvey.html',{'survey_id':survey_id,'allQuestions' : allQuestions},context_instance=RequestContext(request))
 
            
    except KeyError, e:
        allQuestions=SuQuestions.objects.all()
        messages={'alert':'No activity within 120 minutes; please log in again'}
        return render(request, 'index.html',{'messages': messages,'allQuestions' : allQuestions},context_instance=RequestContext(request)) 


#---- all user to a survey ----# 
def view_all_User_to_survey(request,survey_id=0):
    
    try:
        request.session['user_login_data']
        survey_data=SuSurey.objects.get(id=survey_id)
        user_survey_data=SuSureyAndUser.objects.filter(surey=survey_data)
        return  render_to_response("pages/forms/allusers_for_survey.html",{'user_survey':user_survey_data,'survey_data':survey_data},context_instance=RequestContext(request))
    
    except KeyError, e:
        messages={'alert':'You need to loging'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request)) 
    

def allQuestionSurvey(request,survey_id=0):
    try:
        request.session['user_login_data']
        survey_data=SuSurey.objects.get(id=survey_id)
        survey_question_data=SuSureyFactorsAndQuestions.objects.filter(surey=survey_data)
        count=SuSureyFactorsAndQuestions.objects.filter(surey=survey_data).count()
        return  render_to_response("pages/forms/allQuestionstoSurvey.html",{'survey_question_data':survey_question_data,'survey_data':survey_data,'count':count},context_instance=RequestContext(request))
    
    except KeyError, e:
        messages={'alert':'You need to loging'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request)) 



@csrf_exempt
def surveyAnswred(request,survey_id=0):
    try:
        request.session['user_login_data']
        if request.method == 'POST':
            
            survey_data=SuSurey.objects.get(id=survey_id)
            survey_question_data=SuSureyFactorsAndQuestions.objects.filter(surey=survey_data)
            count=SuSureyFactorsAndQuestions.objects.filter(surey=survey_data).count()
            
            post_data=request.POST
            
            #post_data.pop('csrfmiddlewaretoken')
            #del post_data['csrfmiddlewaretoken']
            post_data_vales=request.POST.values()
            post_data_keys=request.POST.keys()
            post_data_all=request.POST.items()
            #del post_data_keys['csrfmiddlewaretoken']
            #del post_data_vales['csrfmiddlewaretoken']
            #post_data_keys.pop()
            #post_data_vales.pop()
            #post_data.pop()
#             for key,value in post_data:
#                 ss=key
#                 sss=value

            for i in range(0, len(post_data_keys)):
                try:
                    question_data=SuQuestions.objects.get(id=post_data_keys[i])
                    survey_question_data1 = SuSureyFactorsAndQuestions.objects.get(surey_id=survey_id, question_id=post_data_keys[i])
                    user_answer_date=SuUserAndAnswers(surey=survey_data, question=question_data, catorgory=survey_question_data1, answered_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), answer_by=request.session['user_login_data']['id'], answer=post_data_vales[i])
                    try:
                        user_answer_date.full_clean()
                        user_answer_date.save(True,False,None, None)
                        
                    except ValidationError as e:
                        print "Error", e.messages
                    
                    if survey_question_data1.subfactor_id != None:
                    
                        try:
                            sb=SuSubFactors.objects.get(id=survey_question_data1.subfactor_id)    
                            try:                            
                                obj= SuSubFactorAvarage.objects.get(survey=survey_data, subfactor=sb)
                                obj.number_of_emp = obj.number_of_emp + 1
                                obj.sum = obj.sum + float(post_data_vales[i])
                                obj.avarage = float(obj.sum) / obj.number_of_emp
                                if obj.avarage > 3:
                                    obj.critical= 1
                                else:
                                    obj.critical= 0                                
                                obj.save()
                                
                            except SuSubFactorAvarage.DoesNotExist as e:
                                ct = 0
                                if float(post_data_vales[i]) > 3:
                                    ct = 1
                                data=SuSubFactorAvarage(survey=survey_data, subfactor=sb, number_of_emp=1, sum=post_data_vales[i], avarage=float(post_data_vales[i]), critical= ct)
                                data.full_clean()                    
                                data.save(True,False,None, None)
                                
                            
                        except ValidationError as e:
                            print "Error", e.messages        
                    
                except UnboundLocalError,e:
                    print "error"
            messages={'success':'Successfuly answer the Survey'}
            return  render_to_response("empAnswresfrom.html",{'messages':messages,'survey_question_data':survey_question_data,'survey_data':survey_data,'count':count},context_instance=RequestContext(request))
    
        else:
            survey_data=SuSurey.objects.get(id=survey_id)
            survey_question_data=SuSureyFactorsAndQuestions.objects.filter(surey=survey_data)
            count=SuSureyFactorsAndQuestions.objects.filter(surey=survey_data).count()
            return  render_to_response("empAnswresfrom.html",{'survey_question_data':survey_question_data,'survey_data':survey_data,'count':count},context_instance=RequestContext(request))
    
    except KeyError, e:
        messages={'alert':'You need to loging'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request)) 
    
    
def ajax_all_dept_users(request):
    try:
        request.session['user_login_data']
        dept_data=SuUserDepartment.objects.filter(org=request.session['user_login_data']['org'])
        dept=request.POST.get('dept','')
        survey_id=request.POST.get('Surey_ID','')
        responce_data={}
        
        if request.method == 'POST':
            surey_data=SuSurey.objects.get(id=survey_id)
            allusers=SuUser.objects.filter(dept_id=dept)
            #responce_data['allusers']=allusers
            #responce_data['dept_data']=dept_data
            #responce_data['surey_data']=surey_data
            #responce_data = [ allusers, dept_data, surey_data ] 
            #responce_data['survey_id']=survey_id
            
            #responce_data = [ surey_data, ] + dept_data + allusers
            
            #data = serializers.serialize('json', responce_data)
            #return HttpResponse(json.dumps(responce_data),content_type="application/json;charset=utf8")
            return HttpResponse(json.dumps({'allusers':allusers,'dept_data':dept_data,'surey_data':surey_data, 'survey_id':survey_id }),content_type="application/json; charset=utf8")
            #return  render_to_response("pages/forms/publish.html",{'allusers':allusers,'dept_data':dept_data,'surey_data':surey_data, 'survey_id':survey_id },context_instance=RequestContext(request))
    
        
    except KeyError, e:
        messages={'alert':'You need to loging'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request))    

@csrf_exempt  
def publishSurveys(request,survey_id=0,dept_id=0):
    try:
        request.session['user_login_data']
        
        
        if request.method == 'POST':
            
#             if(survey_id==0,dept_id==0):
#                 dept_id=request.POST.get('dept_id','')
#                 survey_id=request.POST.get('Surey_ID','')
            try:
                #dept_id=request.POST.get('dept','')
                #survey_id=request.POST.get('Surey_ID','')
                surey_data=SuSurey.objects.get(id=request.POST.get('Surey_ID',''))
                dept=SuUserDepartment.objects.get(id=request.POST.get('dept',''))
                allusers=SuUser.objects.filter(org=request.session['user_login_data']['org'],dept=dept)
                survey_count=SuUser.objects.filter(org=request.session['user_login_data']['org'],dept=dept).count() 
                return render(request, 'pages/forms/publishSurveys.html',{'surey_data': surey_data,'dept_id': dept_id,'allusers':allusers,'survey_count':survey_count},context_instance=RequestContext(request))

            except ValueError, e:
                if request.method == 'POST':
                    post_data_vales=request.POST.values()
                    post_data_keys=request.POST.keys()
                    post_data_all=request.POST.items()
                    Post_data=request.POST
                    checked_list = request.POST.getlist('checks[]')
                    survey=SuSurey.objects.get(id=survey_id)
                    for i in range(0, len(checked_list)):
                        user_date=SuUser.objects.get(id=checked_list[i])
                        surveyanduser=SuSureyAndUser(surey=survey,user=user_date,create_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),create_by=request.session['user_login_data']['id'])
                        try:
                            surveyanduser.full_clean()
                            surveyanduser.save(True,False,None, None)
                        
                        except ValidationError as e:
                            print "Error", e.messages
                            
                    surey_data=SuSurey.objects.get(id=survey_id)
                    dept=SuUserDepartment.objects.get(id=dept_id)
                    allusers=SuUser.objects.filter(org=request.session['user_login_data']['org'],dept=dept)
                    survey_count=SuUser.objects.filter(org=request.session['user_login_data']['org'],dept=dept).count() 
                    return render(request, 'pages/forms/publishSurveys.html',{'surey_data': surey_data,'dept_id': dept_id,'allusers':allusers,'survey_count':survey_count},context_instance=RequestContext(request))

                else:
                    surey_data=SuSurey.objects.get(id=survey_id)
                    dept=SuUserDepartment.objects.get(id=dept_id)
                    allusers=SuUser.objects.filter(org=request.session['user_login_data']['org'],dept=dept)
                    survey_count=SuUser.objects.filter(org=request.session['user_login_data']['org'],dept=dept).count() 
                    return render(request, 'pages/forms/publishSurveys.html',{'surey_data': surey_data,'dept_id': dept_id,'allusers':allusers,'survey_count':survey_count},context_instance=RequestContext(request))

                       
        else:
            
            surey_data=SuSurey.objects.get(pk=survey_id)
            dept=SuUserDepartment.objects.get(id=dept_id)
#             allusers=SuUser.objects.filter(org=request.session['user_login_data']['org'],dept=dept)
#             survey_count=SuUser.objects.filter(org=request.session['user_login_data']['org'],dept=dept).count() 
            allusers=SuUser.objects.filter(dept=dept)
            survey_count=SuUser.objects.filter(dept=dept).count() 
           
            return render(request, 'pages/forms/publishSurveys.html',{'surey_data': surey_data,'dept_id': dept_id,'allusers':allusers,'survey_count':survey_count},context_instance=RequestContext(request))
   
    except KeyError, e:
        messages={'alert':'You need to loging'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request))    
       
def addUsers_to_Surveys(request,survey_id=0,dept_id=0):
    try:
        request.session['user_login_data']
        
        
        if request.method == 'POST':
            
#             if(survey_id==0,dept_id==0):
#                 dept_id=request.POST.get('dept_id','')
#                 survey_id=request.POST.get('Surey_ID','')
            surey_data=SuSurey.objects.get(id=request.POST.get('Surey_ID',''))
            dept=SuUserDepartment.objects.get(id=request.POST.get('dept',''))
            allusers=SuUser.objects.filter(org=request.session['user_login_data']['org'],dept=dept)
            survey_count=SuUser.objects.filter(org=request.session['user_login_data']['org'],dept=dept).count() 
            return render(request, 'pages/forms/publishSurveys.html',{'surey_data': surey_data,'dept_id': dept_id,'allusers':allusers,'survey_count':survey_count},context_instance=RequestContext(request))
   
        else:
            
            surey_data=SuSurey.objects.get(pk=survey_id)
            dept=SuUserDepartment.objects.get(id=dept_id)
#             allusers=SuUser.objects.filter(org=request.session['user_login_data']['org'],dept=dept)
#             survey_count=SuUser.objects.filter(org=request.session['user_login_data']['org'],dept=dept).count() 
            allusers=SuUser.objects.filter(dept=dept)
            survey_count=SuUser.objects.filter(dept=dept).count() 
           
            return render(request, 'pages/forms/publishSurveys.html',{'surey_data': surey_data,'dept_id': dept_id,'allusers':allusers,'survey_count':survey_count},context_instance=RequestContext(request))
   
    except KeyError, e:
        messages={'alert':'You need to loging'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request))    
   

   
        


