from django.shortcuts import render,render_to_response,RequestContext,redirect
from django.core.urlresolvers import reverse
from allModel.models import SuUserDepartment,SuUser,SuOrganization
from django.http import HttpResponseRedirect
from froms import addDept
from compiler.ast import From
from django.core.exceptions import ValidationError,NON_FIELD_ERRORS
# Create your views here.
def index(request):
    try:
        request.session['user_login_data']
        return  render_to_response("pages/forms/addDept.html",locals(),context_instance=RequestContext(request))
    
    except KeyError, e:
        messages={'alert':'You need to loging'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request))   
        
    
        

def addDept(request):
    
    try:
        request.session['user_login_data']
        if request.method == 'POST':
           
            userId=SuUser.objects.get(id=request.session['user_login_data']['id'])
            org=SuOrganization.objects.get(id=request.session['user_login_data']['org_id'])
            
#             f=addDept(request.POST)
#             #from=addDept()
#             f.email=request.POST.get('Email','')
#             f.dept_name=request.POST.get('Dept_name','')
#             f.Description=request.POST.get('Description','')
#             f.user=userId
            #from
#             if f.IsValid():
#                 save_it=f.save(commit=False)
#                 save_it.save()
            #from=UserCreationForm(request.POST)
            data=SuUserDepartment(email=request.POST.get('Email',''),dept_name=request.POST.get('Dept_name',''),Description=request.POST.get('Description',''),contact_number=request.POST.get('Contact',''),user=userId,org=org )
            
            try:
                data.full_clean()
                data.save(True,False,None, None)
                messages={'success':'Successfuly data added'}
                return  render(request, 'pages/forms/addDept.html',{'messages': messages},context_instance=RequestContext(request))
   
            except ValidationError as e:
                messages={'error':e.message_dict}
                return render(request, 'pages/forms/addDept.html',{'messages': messages},context_instance=RequestContext(request))
    except KeyError, e:
        messages={'alert':'No activity within 120 minutes; please log in again'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request))
        #return render(request, '/',{'messages': messages})
        #return redirect(reverse("/",messages={'messages':messages}))
        #return HttpResponseRedirect(reverse("/",{'messages':messages}))
          
                 
            
    
   
