from django.shortcuts import render,redirect
# from .views import *
from django.contrib.auth.decorators import login_required
# from .models import waterCharge
# from .models import tax
# from .models import dummy
from .models import *
from .models import tax
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.contrib import messages
from genuser.models import *
from .models import prevBill
import logging
# from datetime import date
from django.db.models import Sum
# from django.db.models.functions import Cast
from django.utils.safestring import mark_safe
import json




# Create your views here.

def bills(request):

    if request.method=="POST":
        units=request.POST.get('wateruni')
        month=request.POST.get('month')


logger = logging.getLogger(__name__)       

@login_required(login_url='/')
def calci(request):
    data={}
    dor=request.POST.get('dateReading')
    print(dor)
    unitUse=request.POST.get('units')
    print(unitUse)
    curuser=request.user
    print(curuser.id)
    

    # if request.method=='POST': 
    try:

        if request.method=='POST':
           if dor is not None and unitUse is not None:
            # dor=request.POST.get('dateReading')
            # print(dor)
            # unitUse=request.POST.get('units')
            # print(unitUse)
            # curuser=request.user
            # print(curuser.id)

            
            # print(unitUse)
            # charges=waterCharge.objects.all()
            # charges=waterCharge.objects.get(lessThanLiters__lte=8000)
            # print(charges.priceFOrLiters) works!!

            # if 'save' in request.POST:
        
            #     print(curuser.email)
            #     sanc=request.POST.get('sanitaryCharge')
            #     obj=dummy.objects.create(useid=curuser.id,name=sanc,charge=totalBill)
            #     print(obj)
            #     obj.save()
            #     return render(request, "bills.html")
            # else:

            # if dor is not None:
                dt=datetime.strptime(dor, '%Y-%m-%d')
                print(dt)
                d=dt.date()
                print(d)
                d2=d+relativedelta(months=1)
                d2=datetime.strftime(d2,'%Y-%m-%d')
                print(d2)
                unitUse=int(unitUse)
                if unitUse<8000:
                    charges=waterCharge.objects.get(lessThanLiters__lte=8000)

                    perKl=charges.priceFOrLiters
                    # perKl=waterCharge.filter(lessThanLiters__lte=8000).values()
                
                    waterVal= (unitUse*perKl)/1000
                    print(waterVal)
                
                elif unitUse>8000 and unitUse<16000:
                    charges=waterCharge.objects.filter(lessThanLiters__range=(8001,16000)).values()
                    for charge in charges:
                        # print(charge)
                        # print(charge['priceFOrLiters'])
                        perKl=charge['priceFOrLiters']
            
                    # perKl=charges.priceFOrLiters
                
                    # perKl=waterCharge.filter(lessThanLiters__lte=8000).values()
                
                    waterVal= (unitUse*perKl)/1000
                
                elif unitUse>8000 and unitUse<=16000:
                    charges=waterCharge.objects.filter(lessThanLiters__range=(8001,16000)).values()
                    for charge in charges:
                        perKl=charge['priceFOrLiters']                
                    waterVal= (unitUse*perKl)/1000

                elif unitUse>16000 and unitUse<=25000:
                    charges=waterCharge.objects.filter(lessThanLiters__range=(16001,25000)).values()
                    for charge in charges:
                        perKl=charge['priceFOrLiters']                
                    waterVal= (unitUse*perKl)/1000
                
                elif unitUse>25000 and unitUse<=50000:
                    charges=waterCharge.objects.filter(lessThanLiters__range=(25001,50000)).values()
                    for charge in charges:
                        perKl=charge['priceFOrLiters']                
                    waterVal= (unitUse*perKl)/1000
                
                elif unitUse>50000 and unitUse<=75000:
                    charges=waterCharge.objects.filter(lessThanLiters__range=(50001,75000)).values()
                    for charge in charges:
                        perKl=charge['priceFOrLiters']                
                    waterVal= (unitUse*perKl)/1000
                
                elif unitUse>75000 and unitUse<=100000:
                    charges=waterCharge.objects.filter(lessThanLiters__range=(75001,100000)).values()
                    for charge in charges:
                        perKl=charge['priceFOrLiters']                
                    waterVal= (unitUse*perKl)/1000
                
                elif unitUse>100000:
                    charges=waterCharge.objects.get(lessThanLiters__gt=100000)
                    for charge in charges:
                        perKl=charge['priceFOrLiters']                
                    waterVal= (unitUse*perKl)/1000
                
                curYear=datetime.now().year
                print(curYear)

                curTaxName=f'For{curYear}'
                print(curTaxName)
                curTax=tax.objects.filter(taxName=curTaxName).values()
               
                
            
                

                for obj in curTax:
                    meterCharge=obj['meterFee']
                    sanitaryCharge=obj['sanitaryCharges']
                    other=obj['otherCharges']

                print(meterCharge)
                totalBill=waterVal+meterCharge+sanitaryCharge+other

                print(totalBill)

                
                data={
                    'waterVal':waterVal,
                    'perKl':perKl,
                    'unitUse':unitUse,
                    'dor':dor,
                    'dueDate':d2,
                    'readDate':dor,
                    'sanitaryCharge':sanitaryCharge,
                    'meterCharge':meterCharge,
                    'totalBill':totalBill
                }

                print(data)

        # if 'save' in request.POST:
        #     print(curuser.email)
        #     sanc=request.POST.get('sanitaryCharge')
        #     obj=dummy(useid=curuser.id,name=sanc,charge=totalBill)
        #     print(obj)
        #     obj.save()
        #     return render(request, "bills.html")


            # return render(request, 'calci.html', data)
            # print(data)
        # else:
        #     messages.error(request, "Enter valid date and units")
        #     return render(request, 'calci.html')
        #     pass  ////////////uncomment this else statemnet


        # if "save" in request.POST:
        #     print(curuser)
        #     sanc=request.POST.get("sanitaryCharge")
        #     print(sanc)
        #     print(curuser)
        #     obj=dummy(useid=curuser,name="sra",charge=totalBill)
            
        #     print(curuser)
        #     obj.save()
        #     print(curuser)
        #     return render(request, "bills.html") works!!

            # if "save" in request.POST:
        
        if "save" in request.POST:

            meterUsage=int(request.POST.get("unitUse"))
            sanC=int(request.POST.get("sanitaryCharge"))
            dor=request.POST.get("dateofReading")
            readDate=datetime.strptime(dor,"%Y-%m-%d").date()
            year=readDate.year##new
            dD=request.POST.get("dueDate")
            dueDate=datetime.strptime(dD,"%Y-%m-%d").date()
            month=readDate.strftime("%B")
            print(month)
            meterCharge=float(request.POST.get("meterCharge"))
            waterVal=float(request.POST.get("waterVal"))
            totalBill=float(request.POST.get("totalBill"))
            # print(totalBill)
            checkuser=CustomUser.objects.get(username=request.user)

            if prevBill.objects.filter(month=month,userInfo=checkuser,readDate__year=year):
                                                          ##
                messages.error(request,"Bill already saved for this month")                                     ##
                return redirect("calci")                                                                        ##check if working
                                                                                                                ##working :)
            if meterUsage is not None:

                obj=prevBill(userInfo=checkuser,month=month,meterusage=meterUsage, readDate=readDate,dueDate=dueDate,
                            sanitaryCharge=sanC,meterCharge=meterCharge,waterValue=waterVal,totalamount=totalBill,currentDue=0)
                
                obj.save()
                print("Bill saved successfully:", obj)
                messages.success(request, "Bill saved successfully")
                return redirect("calci")
            else:
                messages.error(request,"Bill already saved")
                return redirect("calci")


            

            

    except:
          pass

    return render(request, 'calci.html', data)



# def showBills(request):

#     if request.method=='POST':

#         if 'save' in request.POST:
#         # obj=CustomUser.objects.get(user=request.user)
#         # print(obj)
#              sanitaryBill=request.POST.get("sanitaryCharge")
#         # u=request.user
#              obj=dummy.objects.create(user=request.user,charge=sanitaryBill)
#         obj.save()

@login_required(login_url="/")       
def bills(request):

    userBills=prevBill.objects.filter(userInfo=request.user).order_by('-readDate')
 
    selected_month = request.GET.get('month')

    if selected_month:
        userBills = userBills.filter(month=selected_month)
        # print("search is working")
        # print(f'bills are :{userBills}')


    return render(request, "bills.html",{"bills":userBills, "selected_month":selected_month})


###########################
@login_required(login_url="/")
def taxpage(request):

    curYear=datetime.now().year
    curTaxName=f'For{curYear}'
    curTax=tax.objects.filter(taxName=curTaxName).values()
    charges=waterCharge.objects.all().order_by('lessThanLiters')
    
    chargeRanges = []
    
    
    for i in range(len(charges)):
        if i == 0:
            range_text = f"unit usage < {charges[i].lessThanLiters}"
        
        elif i==len(charges)-1:
            range_text=f"unit usage >{charges[i].lessThanLiters-1}"
            
        else:
            range_text = f"{charges[i-1].lessThanLiters} < unit usage ≤ {charges[i].lessThanLiters}"
        
        chargeRanges.append((range_text, charges[i].priceFOrLiters))
    

    for obj in curTax:
        meterCharge=obj['meterFee']
        sanitaryCharge=obj['sanitaryCharges']
        other=obj['otherCharges']   

    data={
        "meterCharge":meterCharge,
        "sanitaryCharge":sanitaryCharge,
        "other":other,   
        "chargeRanges":chargeRanges  

    }  
 
    
    return render(request, "tax.html",data)



# ###############################
@login_required(login_url="/")
def meterDashboard(request):

    user = request.user 
    selected_year = int(request.GET.get('year', datetime.now().year))
    print(selected_year)
    bills = prevBill.objects.filter(userInfo=user, readDate__year=selected_year)
    monthly_usage = bills.values('month').annotate(total_usage=Sum('meterusage')).order_by('readDate')

    months = [entry['month'] for entry in monthly_usage]
    usages = [entry['total_usage'] for entry in monthly_usage]
    print("Months:", months)  
    print("Usages:", usages)  

    # months_json = mark_safe(json.dumps(months))
    # usages_json = mark_safe(json.dumps(usages))
    months_json = json.dumps(months)
    usages_json = json.dumps(usages)

    available_years = prevBill.objects.filter(userInfo=user).dates('readDate', 'year')

    return render(request, 'dashboard.html', {
        # 'months': months,
        # 'usages': usages,
        # 'months_json': months_json,
        # 'usages_json': usages_json,
        'months_json': mark_safe(months_json),
        'usages_json': mark_safe(usages_json),
        'selected_year': int(selected_year),
        'available_years': available_years,
    })
