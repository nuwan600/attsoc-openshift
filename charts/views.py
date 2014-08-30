from django.shortcuts import render
from allModel.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404,render_to_response,RequestContext 
from django.template import RequestContext,loader
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
import MLP,PIL,PIL.Image,StringIO,matplotlib.pyplot as plt,numpy as np
from django.core.context_processors import request
from reportlab.pdfgen.canvas import Canvas
from matplotlib import pylab
from gnome import canvas
from MySQLdb.constants.FIELD_TYPE import NULL

# Create your views here.
def allcharts(request):
    print "Learning the sin function"
    network =MLP.MLP(2,10,1)
   
    samples = np.zeros(2000, dtype=[('x',  float, 1), ('y', float, 1)])
    samples['x'] = np.linspace(-5,5,2000)
    samples['y'] = np.sin(samples['x'])
    #samples['y'] = np.linspace(-4,4,2500)

    for i in range(100000):
        n = np.random.randint(samples.size)
        network.propagate_forward(samples['x'][n])
        network.propagate_backward(samples['y'][n])

    plt.figure(figsize=(10,5))
    # Draw real function

    x = samples['x']
    y = samples['y'] 
    #x=np.linspace(-6.0,7.0,50)
    plt.plot(x,y,color='b',lw=1)


    samples1 = np.zeros(2000, dtype=[('x1',  float, 1), ('y1', float, 1)])
    samples1['x1'] = np.linspace(-4,4,2000)
    samples1['y1'] = np.sin(samples1['x1'])

    # Draw network approximated function
    for i in range(samples1.size):
        samples1['y1'][i] = network.propagate_forward(samples1['x1'][i])
        #x[i] = network.propagate_backward(y[i])

    #pl.plot(samples['x'], samples['y'] ,'.',x , y, '-')
    #l.legend(['train target', 'net output'])
    #pl.show()
    plt.plot(samples1['x1'],samples1['y1'],color='r',lw=3)
    plt.axis([-2,2,-2,2])
    plt.show()
    plt.close()
    return HttpResponseRedirect('/charts/charts')  
    #buffer=StringIO.StringIO()
    #canvas=pylab.get_current_fig_manager().canvas
    #canvas.draw()
    #graphIMG =PIL.Image.fromstring("RGB",canvas.get_width_height(),canvas.tostring_rgb())
    #graphIMG.save(buffer, "PNG")
    #pylab.close()
    #return HttpResponse(buffer.getvalue(),content_type="image/png")
    #return render(request, 'pages/forms/charts.html',context_instance=RequestContext(request))  
    
def linecharts(request):
    print "Learning the line function"
    network =MLP.MLP(2,10,1)
   
    samples = np.zeros(2000, dtype=[('x',  float, 1), ('y', float, 1)])
    samples['x'] = np.linspace(-5,5,2000)
    samples['y'] = np.linspace(-5,5,2000)
    #samples['y'] = np.linspace(-4,4,2500)

    for i in range(100000):
        n = np.random.randint(samples.size)
        network.propagate_forward(samples['x'][n])
        network.propagate_backward(samples['y'][n])

    plt.figure(figsize=(10,5))
    # Draw real function

    x = samples['x']
    y = samples['y'] 
    #x=np.linspace(-6.0,7.0,50)
    plt.plot(x,y,color='b',lw=1)


    samples1 = np.zeros(1000, dtype=[('x1',  float, 1), ('y1', float, 1)])
    samples1['x1'] = np.linspace(-8,8,1000)
    samples1['y1'] = np.linspace(-8,8,1000)

    # Draw network approximated function
    for i in range(samples1.size):
        samples1['y1'][i] = network.propagate_forward(samples1['x1'][i])
        #x[i] = network.propagate_backward(y[i])

    #pl.plot(samples['x'], samples['y'] ,'.',x , y, '-')
    #l.legend(['train target', 'net output'])
    #pl.show()
    plt.plot(samples1['x1'],samples1['y1'],color='r',lw=3)
    plt.axis([-1,1,-1,1])
    plt.show()
    plt.close()
    return HttpResponseRedirect('/charts/charts')  


def paraboliccharts(request):
    print "Learning the parabolic function"
    network = MLP.MLP(1,10,1)
    samples = np.zeros(500, dtype=[('x',  float, 1), ('y', float, 1)])
    samples['x'] = np.linspace(0,1,500)
    samples['y'] = np.sin(samples['x']*np.pi)

    for i in range(10000):
        n = np.random.randint(samples.size)
        network.propagate_forward(samples['x'][n])
        network.propagate_backward(samples['y'][n])

    plt.figure(figsize=(10,5))
    # Draw real function
    x,y = samples['x'],samples['y']
    plt.plot(x,y,color='b',lw=1)
    # Draw network approximated function
    for i in range(samples.shape[0]):
        y[i] = network.propagate_forward(x[i])
    plt.plot(x,y,color='r',lw=3)
    plt.axis([0,1,0,1])
    plt.show()
    plt.close()
    return HttpResponseRedirect('/charts/charts')  


def charts(request):
    try:
        request.session['user_login_data']
        dept_data=SuUserDepartment.objects.filter(org=request.session['user_login_data']['org'])
        allsurveyassign=SuSureyAndUser.objects.count()
        answered=SuSureyAndUser.objects.filter(is_answered=1).count()
        unanswred=SuSureyAndUser.objects.exclude(is_answered__isnull=False).count()
        return render(request, 'pages/forms/charts.html',{'dept_data': dept_data,'allsurveyassign':allsurveyassign,'answered':answered,'unanswred':unanswred},context_instance=RequestContext(request))   
        
    
    except KeyError, e:
        messages={'alert':'No activity within 120 minutes; please log in again'}
        return render(request, 'index.html',{'messages': messages},context_instance=RequestContext(request))   
     
  
      