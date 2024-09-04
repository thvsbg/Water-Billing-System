from django.shortcuts import redirect, render
from django.http  import HttpResponse
from genuser.models import CustomUser
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method=="POST":

        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('mail')
        meterno=request.POST.get('meterno')
        add=request.POST.get('add')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        if CustomUser.objects.filter(username=username):
            messages.error(request, "Username already exists")
            return redirect("signup")
    
        if CustomUser.objects.filter(email=email):
            messages.error(request,"Email already registered")
            return redirect("signup")
        
        if CustomUser.objects.filter(meternumber=meterno):
            messages.error(request, "Meter Number already registered")
            return redirect("signup")
        
        if not pass2.isalnum() or len(pass2)<6:
            messages.error(request, "Password should be alphanumeric and of length 6")
            return redirect("signup")

        
        if len(meterno)>6 :
            messages.error(request, "please enter valid meter number")
            return redirect("signup")
        
        if pass1!=pass2:
            messages.error( request,"passwords don't match")
            return redirect("signup")
        

        newuser= CustomUser(username=username,first_name=fname,last_name=lname,email=email,meternumber=meterno,address=add,password="")
        newuser.set_password(pass2)
        newuser.save()
        messages.success(request, "Profile Created Successfully.Please Login")

        return redirect('/signin')


    return render(request, 'authentication/signup.html')

def signin(request):

    # if request.method=="POST":
    #     uname=request.POST['uname']
    #     passw=request.POST['passw']
    
    #     user=authenticate(username=uname,password= passw)

    #     if user is not None:
    #         login(request, user)
    #         return render(request, "base.html")
    #     else:
    #         messages.error(request, "bad credentials")
        
    #         return redirect('/signin')
    
    

    return render(request, 'authentication/signin.html')




def signout(request):

    logout(request)
    return redirect('home')
    # response.delete_cookie('user_location')
    # return response
    # return redirect("signout")



# @login_required(login_url="/")
def doLogin(request):
    if request.method=="POST":
        uname=request.POST['uname']
        passw=request.POST['passw']
    
        user=authenticate(username=uname,password= passw)

        if user is not None:
            login(request, user)
            return redirect("base")
           #return render(requst, "base.html") 
        else:
            messages.error(request, "bad credentials")
        
            return redirect('/signin')
    


    return render(request, 'authentication/signin.html')

    # return render(request, 'base.html')


@login_required(login_url='/')
def base(request):
    return render(request, "base.html")

@login_required(login_url="/")
def profile(request):

    user=CustomUser.objects.get(id=request.user.id)
    data={
        'user':user
    }
    return render(request, "authentication/profile.html",data)

@login_required(login_url='/')
def update(request):

    if request.method=="POST":
        newmail=request.POST.get("email")
        newPass=request.POST.get("newPass")
        finPass=request.POST.get("finPass")

        if not finPass.isalnum() or len(finPass)<6:
            messages.error(request,"Password should be  of length 6 and alphanumeric")
            redirect("update")

        # if newPass!=finPass:
        #     messages.error(request,"Passwords didn't match")
        #     return render(request,"authentication/profile.html")
        try:
            curUser=CustomUser.objects.get(id=request.user.id)
            curUser.email=newmail
            if newPass==finPass and finPass!=None and finPass!="":
                curUser.set_password(finPass)
            
            curUser.save()
            messages.success(request,"Updated Succesfully")
            redirect("profile")


        
        except:
            messages.error(request,"Failed to update Profile")

    return render(request,"authentication/profile.html")