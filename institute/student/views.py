from django.shortcuts import render
from secretary.models import StudentSiteRegister
from student.models import StudentRegister 
# Create your views here.

def IndexView(request):
    return render(request, 'student/index.html')

def Profile(request, request_id):
    if request.method == 'POST':
        code = request_id
        name = request.POST['Name']
        family = request.POST['FamilyName']
        address = request.POST['Address']
        tel = request.POST['Tel']
        phone = request.POST['Phone']
        age = request.POST['Age']
        s = StudentRegister.objects.filter(NationalCode = code ).update(Name = name, FamilyName = family, Address = address, Tele= tel, Phone = phone, Age = age)
        #s = StudentRegister(NationalCode = code, Name = name, FamilyName = family, Address = address, Tele= tel, Phone = phone, Age = age)
        #s.save()
        
         
    return render(request, 'student/profile.html')

def LogIn(request):
    if request.method == 'POST':        
        username = request.POST['Username']
        password = request.POST['Password']
        s = StudentSiteRegister.objects.filter(Username = username ,Password = password).count()
        if s == 1: 
            context = {'request_id':str( username)}
            return render(request, 'student/index.html', context)
    return render(request, 'student/login.html')

def PrintDegree(request):
    return render(request, 'student/PrintDegree.html')

def Salary(request):
    return render(request, 'student/SalaryPayment.html')

def TermInfo(request):
    return render(request, 'student/TermInfo.html')


#Error
def error400(request):
    return render(request, 'student/400.html')

def error403(request):
    return render(request, 'student/403.html')

def error404(request):
    return render(request, 'student/404.html')

def error500(request):
    return render(request, 'student/500.html')

def error503(request):
    return render(request, 'student/503.html')


