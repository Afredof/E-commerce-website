from datetime import date, timedelta
from django.contrib import messages
from django.shortcuts import redirect, render
from.models import reg_table
from . models import item_table
from . models import cart_table ,Pay_table
# Create your views here.
def index(request):
    return render (request,"index.html")
def signup(request):
    if request.method=='POST':
        name=request.POST.get('nm')
        email=request.POST.get('em')
        mob=request.POST.get('num')
        password=request.POST.get('pwd')
        rpassword=request.POST.get('rpwd')
        obj=reg_table.objects.create(nm=name,em=email,num=mob,pwd=password,rpwd=rpassword)
        obj.save()
        if obj:
            return render(request,"signin.html")
        else:
            return render(request,"signup.html")
    else:
        return render(request,"signup.html")
def signin(request):
    print("inside signin")
    if request.method=='POST':
        email=request.POST.get('em')
        password=request.POST.get('pwd')
        obj=reg_table.objects.get(em=email,pwd=password)
        if obj:
            # for ls in obj:
            idno=obj.id
            request.session['idl']=idno
            return render(request,"home.html")
        else:
            msg= 'Invalid mail or password'
            return render(request,"signin.html",{"error":msg})
    else:
        return render(request,"signin.html")
def itemview(request):
        obj=item_table.objects.all()
        return render(request,"itemview.html",{"card":obj})
def addtocart(request):
    number=request.GET.get('id')
    userid=request.session.get('idl')
    uobj=reg_table.objects.get(id=userid)
    pobj=item_table.objects.get(id=number)
    cartitem,created=cart_table.objects.get_or_create(customer=uobj,product=pobj)
    if not created:
        cartitem.qty+=1
        cartitem.save()
        messages.success(request,"Item added to cart")
    return redirect('/itemview')
def viewcart(request):
    cid=request.session.get('idl')
    cusobj=reg_table.objects.get(id=cid)
    cartobj=cart_table.objects.filter(customer=cusobj)
    if cartobj:
        total_price=0
        for i in cartobj:
            pro=i.product.prc*i.qty
            total_price=total_price+pro
        return render (request,"cart.html",{'cartitems':cartobj,'total_price':int(total_price)})
    else:
        return render (request,"cart.html",{"info":"Your Cart is empty"})
def cart_del(request):
    number=request.GET.get('idn')
    cart=cart_table.objects.get(id=number)
   
    cart.delete()
    return redirect('/viewcart')
def paydirect(request):
    cid=request.session.get('idl')
    cusobj=reg_table.objects.get(id=cid)
    obb=reg_table.objects.filter(id=cid)
    for ls in obb:
        fnm= ls.nm
    cartobj=cart_table.objects.filter(customer=cusobj)
    if cartobj:
        total_price=0
        for i in cartobj:
            pro=i.product.prc*i.qty
            total_price=total_price+pro
        return render(request,"pay.html",{'cartitems':cartobj,'total_price':int(total_price),"user":fnm})
    return render(request,"cart.html")
def pay(request):
    current_date=date.today()
    future_date= current_date+timedelta(days=9)
    idno= request.session['idl']
    obj=reg_table.objects.filter(id=idno)
    for ls in obj:
        fname=ls.nm
    if request.method=='POST':
        pro= request.POST.get('pro')
        qty= request.POST.get('qty')
        prc= request.POST.get('prc')
        tot= request.POST.get('tot')
        fn= request.POST.get('fn')
        cd= request.POST.get('cd')
        ex= request.POST.get('ex')
        cvv= request.POST.get('cvv')
        obb= Pay_table.objects.create(pro=pro,prc=prc,tot=tot,fn=fn,ex=ex,cvv=cvv,qty=qty)        
        obb.save()
        if obb:
            msg="Payment Successfull.."
        return render(request,"success.html",{"success":msg,"ret":fname,"current_date":current_date,"future_date":future_date})
    return render(request,"pay.html")    


