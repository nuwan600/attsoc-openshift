from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'attsoc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    
    #accounts
    #url(r'^$', 'accounts.views.index'),
    url(r'^$', 'accounts.views.index'),
    url(r'^accounts/auth','accounts.views.auth'),
    url(r'^accounts/logout','accounts.views.logout'),
    url(r'^accounts/admin','accounts.views.admin'),
    url(r'^accounts/register','accounts.views.register'),
    url(r'^accounts/allusers','accounts.views.allusers'),
    url(r'^accounts/editusers/(?P<user_id>\d+)','accounts.views.editusers'),
    
    #main urls
    url(r'^attsoc/admin','accounts.views.admin',name='admin'),
    url(r'^attsoc/HR','accounts.views.HR',name='HR'),
    
    url(r'^attsoc/emp','accounts.views.emp',name='emp'),
    
    url(r'^surveys/surveyAnswred/(?P<survey_id>\d+)','surveys.views.surveyAnswred'),
    
    
    #errors
     url(r'^attsoc/error405','accounts.views.error405',name='error405'),
    
    #Survey    
    url(r'^surveys/allsurveys','surveys.views.allsurveys'),
    url(r'^surveys/ajaxalldeptusers','surveys.views.ajax_all_dept_users'),
    url(r'^surveys/viewsurveys/(?P<survey_id>\d+)/(?P<dept_id>\d+)','surveys.views.viewsurveys'),
    url(r'^surveys/addsurveys','surveys.views.addsurveys'),
    url(r'^surveys/newsurveys','surveys.views.newsurveys'),
    url(r'^surveys/allQuestionSurvey/(?P<survey_id>\d+)','surveys.views.allQuestionSurvey'),
    url(r'^surveys/addQuestionSurveys/(?P<survey_id>\d+)','surveys.views.addQuestionSurveys',name='addQuestionSurveys'),
    url(r'^surveys/addQuestion_to_Surveys/(?P<survey_id>\d+)','surveys.views.addQuestion_to_Surveys',name='addQuestiontoSurveys'),
    url(r'^surveys/editsurveys/(?P<survey_id>\d+)','surveys.views.editsurveys',name='editSurveys'),
    url(r'^surveys/surveysuser/(?P<survey_id>\d+)','surveys.views.view_all_User_to_survey',name='Surveysuser'),
    url(r'^surveys/publishSurveys/(?P<survey_id>\d+)/(?P<dept_id>\d+)','surveys.views.publishSurveys',name='publishSurveys'),
    url(r'^surveys/publish/(?P<survey_id>\d+)/(?P<dept_id>\d+)','surveys.views.addUsers_to_Surveys',name='publish'),
    
    #departments
    url(r'^departments/Dept','departments.views.index'),
    url(r'^departments/addDept','departments.views.addDept'),
    
    #calender
    url(r'^calender/calender','calender.views.index'),
    
    #mail
    url(r'^mails/mailbox','mails.views.index'),
    
    #charts
    url(r'^charts/all','charts.views.allcharts'),
    url(r'^charts/linecharts','charts.views.linecharts'),
    url(r'^charts/paraboliccharts','charts.views.paraboliccharts'),
    url(r'^charts/charts','charts.views.charts'),
)
