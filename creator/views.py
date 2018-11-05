from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.
from .models import months,weeks,content
TID = None
TOPICS = None
CID = None
import json
from django.core.files.storage import FileSystemStorage


from django.contrib.auth.models import User
from django.http import JsonResponse

def validate_username(request):
    username = request.GET.get('ids', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


def creator(request):
    # displaying the course page!!!
    c = months.objects
    print(c.all)
    if request.user.id == 42 or request.user.id == 1:
        return render(request,'creator.html',{'keys':c, 'chk':3,'magic':1})
    else:
        return redirect('accd')

def topics(request): #change
    ids = request.GET.get('content', None)
    
    tops = weeks.objects.filter(cid=ids).order_by('oid')
    coursetitle = months.objects.all()
    l = len(tops)+1
    #todo : order id hidden and prefillled
    global TOPICS
    TOPICS = tops
    global CID
    CID = ids
    qs_json = serializers.serialize('json', tops)
    cs_json = serializers.serialize('json',coursetitle)
    finalJson = {
        'qsjson' : qs_json,
        'csjson' : cs_json
    }
    # final = serializers.serialize('json',finalJson)
    final = json.dumps(finalJson)
    # print(cs_json)
    # #finalJson = qs_json.concat(cs_json)
    # finalJson = {
    #     'data1' : qs_json,
    #     'data2' : cs_json
    # }
    return HttpResponse(final, content_type='application/json')

def resource(request): #change
    ids = request.GET.get('content', None)
    cid = request.GET.get('cid',None)
    con = content.objects.filter(tid=ids).order_by('oid')
    tops = weeks.objects.filter(cid=cid).order_by('oid').all()

    l = len(con)+1
    global TID
    TID  = ids
    #todo : order id hidden and prefillled
    qs_json = serializers.serialize('json', con)
    ts_json = serializers.serialize('json',tops)
    finalJson = {
        'rsjson':qs_json,
        'tsjson':ts_json
    }
    final = json.dumps(finalJson)
    return HttpResponse(final, content_type='application/json')

def addcourse(request): #change in progress
    temp = request.GET.get('pickachu', None)
    #myfile = request.FILES['thmb']
    # myfile = request.FILES.get('image', None)
    # print("myfile", myfile)
    print("temp", temp)
    print("title", request.GET.get('title', None))
    print("desc", request.GET.get('desc', None))
    # fs = FileSystemStorage()
    # filename = fs.save(myfile.name, myfile)
    # uploaded_file_url = fs.url(filename)
    return HttpResponse("done!")
    # if temp == '2':
    #     naam = course.objects.filter(ids=request.POST['getcid'])
    #     tops = topic.objects.filter(cid=request.POST['getcid'])

    #     details = topic(cid=naam[0],title=request.POST['ctitle'],desc=request.POST['cdesc'],oid=request.POST['orderid'],image=uploaded_file_url)
    #     details.save()
    #     oid = int(request.POST['orderid'])+1
    #     return render(request,'creator.html',{'keys':tops, 'chk':1, 'courseID':request.POST['getcid'],'ordLen':oid})
    # else:
    #     details = course(title=request.GET.get('title', None),desc=request.GET.get('desc', None),image=uploaded_file_url)
    #     details.save()
    #     return HttpResponse('Course Added!')

def reorder(request): #change
    global CID,TOPICS
    tops = TOPICS
    s = request.GET.get('content', None)
    naam = months.objects.filter(ids=CID)
    recurr(0,s,naam[0])
    print(s)
    return HttpResponse(CID)

def recurr(i,s,naam):
    if(i == len(s)):
        return
    obj = weeks.objects.get(Q(oid=int(s[i])) & Q(cid=naam))
    obj.oid = i + 1
    i = i + 1
    print(s[i-1], i)
    recurr(i,s,naam)
    obj.save()


def reorderRes(request):
    s = request.GET['setvalue']
    global TID
    naam = weeks.objects.filter(ids=TID)
    con = content.objects.filter(tid=TID).order_by('oid')
    l = len(con)+1
    recurrRes(0,s,naam[0])
    print(s)
    return render(request,'creator.html',{'keys':con,'chk':2,'topicID':TID,'topOrdLen':l})


def recurrRes(i,s,naam):
    if(i == len(s)):
        return
    obj = content.objects.get(Q(oid=int(s[i])) & Q(tid=naam))
    obj.oid = i + 1
    i = i + 1
    print(s[i-1], i)
    recurrRes(i,s,naam)
    obj.save()


def recurr(i,s,naam):
    if(i == len(s)):
        return
    obj = weeks.objects.get(Q(oid=int(s[i])) & Q(cid=naam))
    obj.oid = i + 1
    i = i + 1
    print(s[i-1], i)
    recurr(i,s,naam)
    obj.save()


def addRes(request):
    temp = request.POST['resId']
    print(temp)
    naam = weeks.objects.filter(ids=request.POST['Fkey'])
    cons = content.objects.filter(tid=request.POST['Fkey'])
    code = request.POST['rSelected']
    if temp=='1':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        data = {}
        data['code'] = code
        data['url'] = uploaded_file_url
        dataJson = json.dumps(data)
        details = content(tid=naam[0],code= request.POST['rSelected'],data= dataJson,oid=request.POST['orderid'])
        details.save()
    elif temp=='0':
        # all about text and questions
        ques = request.POST['title']
        ans = request.POST['summary']
        data = {}
        data['code'] = code
        data['content'] = {}
        data['content']['question'] = ques
        data['content']['answer'] = ans
        print(data)
        dataJson = json.dumps(data)
        print(dataJson)
        details = content(tid=naam[0],code= request.POST['rSelected'],data=dataJson,oid=request.POST['orderid'])
        details.save()
    else:
        # all about MCQ's
        ques = request.POST['title']
        optA = request.POST['A']
        optB = request.POST['B']
        optC = request.POST['C']
        optD = request.POST['D']
        data1 = {}
        data1['code'] = 'M'
        data1['ques'] = ques
        data1['A'] = optA
        data1['B'] = optB
        data1['C'] = optC
        data1['D'] = optD
        data1['ans'] = request.POST['rSelected']
        print(data1)
        dataJson = json.dumps(data1)
        details = content(tid=naam[0],code='M',data= dataJson,oid= request.POST['orderid'])
        details.save()
    oid = int(request.POST['orderid'])+1
    #return HttpResponse('Done!')
    return render(request,'creator.html',{'keys':cons,'chk':2,'topicID':request.POST['Fkey'],'topOrdLen':oid})