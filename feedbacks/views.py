from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import feedback,subscribe
from django.contrib.auth.models import User
from django.contrib import auth
from .models import tokens
from creator.models import months as crs,weeks as tp,content
# Create your views here.

D = None
CHK = None

def course(request):

	p = subscribe.objects.all()
	d = {}
	chk = {}
	d['res'] = -1
	chk['res'] = -1
	for q in p:
		if q.userid == request.user.id:
			if q.check:
				d['res'] = 1
			else:
				d['res'] = 0
	if subscribe.objects.filter(userid=request.user.id):
		if feedback.objects.filter(userid=request.user.id):
			chk['res'] = 1
		else:
			chk['res'] = 0

	c = crs.objects
	global D
	D = d
	global CHK
	CHK = chk
	return render(request,'course.html', {'d' : d, 'chk' : chk,'keys':c,"xyz":1})

def feed(request):
	v = request.GET['fb']
	uid = request.user.id
	f = feedback(userid=uid, summary=v)
	f.save()
	return render(request, 'course.html', {'Response' : 'Feedback Submitted Successfully! :)'})

def subs(request):

	if request.method == 'POST':
		#get the token from the user 
		token = request.POST['tkn']
		#match the token

		uid = request.user.id
		if tokens.objects.filter(token=token):
			#do the free one
			s = subscribe(userid=uid,check=1)
			s.save()	
			return render(request,'course.html',{'subs':'Coupon applied enjoy the course!'})
		else:
			#ask them to pay
			return HttpResponse("payyyyyy")
	else:
		uid = request.user.id
		s = subscribe(userid=uid,check=0)
		s.save()
		return render(request,'course.html',{'subs':'trial Activated'})

def topic(request):
	ids = request.GET['foreignKey']
	t = tp.objects.filter(cid=ids).order_by('oid')
	global D
	global CHK
	return render(request,'course.html', {'d' : D, 'chk' :CHK,'keys':t,"xyz":2})

def resource(request):
	ids = request.GET['foreignKey']
	con = content.objects.filter(tid=ids).order_by('oid')
	return render(request,'resources.html')


