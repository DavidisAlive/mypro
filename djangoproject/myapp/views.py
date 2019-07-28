from django.shortcuts import render,HttpResponse
from myapp import models
# Create your views here.

def show_hello(request):
    return render(request,'profile.html')

def my_cv(request):
    name = request.GET.get("name")
    data={
        "name":name,
        "skills":["java","c","c#","JavaScript"]
    }
    return render(request, 'mycv.html', data)
def add(request):
    a=request.GET.get("a")
    b=request.GET.get("b")
    c=int(a)+int(b)
    return HttpResponse(c)

def comments(req):
    if(req.method=="POST"):
        has_commented=req.session.get("has_commented")
        if(not has_commented):
            req.session["has_commented"] = True
            user = req.POST.get("user")
            comment = req.POST.get("content")
            c = models.Comment(user=user,content=comment)
            c.save()
            return HttpResponse("Comment submitted")

        else:
            return HttpResponse("ya ve alread commented")
    elif(req.method=="GET"):
        comments=models.Comment.objects.all()
        d={
            "comments":comments
        }

        return render(req,'comments.html',d)

def test_session(req):
    c=req.session.get("count")
    if(c==None):
        req.session["count"]=1
    else:
        c=c+1
        req.session["count"]=c
    return HttpResponse("you have visited thsi page" +str(c)+" times")
