from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import For_man,For_Women,Tovars,Corzina,Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.





@login_required
def add_to_favorite(request,product_id):
     product = get_object_or_404(Product, id=product_id)
     Tovars.objects.create(id_clothes = product, accounte = request.user, like = True)
 

     return JsonResponse({'status':'success'})

def main(request):
    corzina = Corzina.objects.all()
    
    users_cor = []
    dict = {}
   
    counter = 0
    for item in Corzina.objects.all():
        dict[item.id_clothes] = item.count
        users_cor.append(item.accounte)
        counter+=dict[item.id_clothes]
    dlina = len(dict)
    print(dlina)
    
    return render(request,'main_ham/index.html',{
        'man':For_man.objects.all(),
        'women':For_Women.objects.all(),
        'users_cor':users_cor,
        'acc':str(request.user),
        'dlina':dlina>=1,
        'dict':dict,
        'counter':counter
    

    })


@login_required
def delete_to_favorite(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    Tovars.objects.delete(id_clothes = product, accounte = request.user)

    return JsonResponse({'status':'success'})



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'main_ham/register.html', {'form':form})


def user_logout(request):
    logout(request)
    return redirect('home')

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'main_ham/login.html', {'form':form})

def show_one_clothes(request,id_clothes:int):
    like = Tovars.objects.all()
    idd = []
    userss = []
    likee = []

    for item in Tovars.objects.all():
        idd.append(item.id_clothes)
        userss.append(item.accounte)
        likee.append(item.like)
    print(idd)
    print(userss)
    message = ''


    id_cor = []
    users_cor = []
    count_cor = []

    for item in Corzina.objects.all():
        id_cor.append(item.id_clothes)
        users_cor.append(item.accounte)
        count_cor.append(item.count)

    if request.method == "POST":
        if request.POST.get('create'):
            like = Tovars()
            like.id_clothes = id_clothes
            like.accounte = request.user
            like.like = True
            like.save()
            message = 'Товар добавлен'
            print(id_clothes == like.id_clothes)
            return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))
        elif request.POST.get('delete'):
            like = Tovars.objects.get(id_clothes = id_clothes)
            like.delete()
            message = 'Товар удален'
            return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))
        elif request.POST.get('add_btn'):
            corzina = Corzina()
            corzina.id_clothes = id_clothes
            corzina.accounte = request.user
            corzina.count = 1
            corzina.save()
            return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))
        elif request.POST.get('delete_btn'):
            corzina = Corzina.objects.get(id_clothes = id_clothes)
            corzina.delete()
            return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))


        else:
            print('Нет такой кнопки')
            

    print(request)


    for_man = get_object_or_404(For_man,   id = id_clothes)
    id_likes = 0
    count = 0
    return render(request, 'main_ham/show_one_clothes.html', {
        'for_man':for_man,
        'clothes':For_man.objects.all(),
        'id':id_likes,
        'like':Tovars.objects.all(),
        'id_clothes':id_clothes,
        'idd':idd,
        'userss':userss,
        'likee':likee,
        'acc':str(request.user),
        'message':message,
        'id_cor':id_cor,
        'users_cor':users_cor,
        'count_cor':count_cor



    })


def likes(request):

    if request.user.is_authenticated:
        sum = Tovars.objects.filter(accounte = request.user).count()
        return render(request, 'main_ham/likes.html', {'likes':For_man.objects.all(),
                                                       'tovars':Tovars.objects.all(),
                                                        'count': sum
                                                       })

    else:
        return redirect('login')

def korzina(request):
    idl = 0
    corzina = Corzina.objects.all()
    
    users_cor = []
    dict = {}
    id_count = []
    counter = 0
    for item in Corzina.objects.all():
        id_count.append(item.id_clothes)
        dict[item.id_clothes] = item.count
        users_cor.append(item.accounte)
        counter+=dict[item.id_clothes]
    dlina = len(dict)
    print(dlina)

    if request.POST.get(f'delete'):
        cor = Corzina.objects.get(id_clothes = idl)
        cor.delete()


    if request.user.is_authenticated:
        return render(request, 'main_ham/korzina.html', {'for_man':For_man.objects.all(),
                                                       'korzina':Corzina.objects.all(),
                                                        'count': sum,
                                                        'idl':idl})
    else:
        return redirect('login')



def all_man(request):
    return render(request,'main_ham/clothes_man/all_man.html', {'man':For_man.objects.all()})

def bruki_man(request):
    return render(request,'main_ham/clothes_man/bruki_man.html', {'man':For_man.objects.all()})

def jeans_man(request):
    return render(request,'main_ham/clothes_man/jeans_man.html', {'man':For_man.objects.all()})

def hudi_man(request):
    print(Category.objects.all())
    return render(request,'main_ham/clothes_man/hudi_man.html', {'man':For_man.objects.all()})


def top_man(request):
    return render(request,'main_ham/clothes_man/top_man.html', {'man':For_man.objects.all()})

def tshirt_man(request):
    return render(request,'main_ham/clothes_man/tshirt_man.html', {'man':For_man.objects.all()})