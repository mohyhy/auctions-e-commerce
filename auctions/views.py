from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

from django.shortcuts import render
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import login_required
from .forms import ListingForm,BidForm


from .models import User,listing,Bid,watchlist,category,comment


def index(request):
    return render(request, "auctions/index.html",
    {   
        "pro":listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
@login_required
def product(request,pk=None):
    pro = listing.objects.get(id=pk)
    c = comment.objects.filter(listing=pro)
    print(c)
    win = Bid.objects.filter(win=True,listing=pro,User=request.user)


        


    
    if request.method == "POST":
        

        bid = request.POST["start"]
        
        if int(pro.price) >= int(bid) :

            message = "entre number more"
        else:
            message = None    
            o=listing.objects.filter(id=pk).update(price=bid)
            u =Bid(User=User.objects.get(username=request.user) ,listing=listing.objects.get(id=pk),start=bid)
            u.save()
        p = listing.objects.get(id=pk)

        return  render(request, "auctions/list.html",{
            "pro":p,
            'form':BidForm(),
            "d":p.price,
            "message":message,
            "comment":c,
            "user":request.user,
            "win":win
        })

        


    else:
        return render(request, "auctions/list.html",{
            "pro":pro,
            'form':BidForm(),
            "d":pro.price,
            "comment":c,
            "user":request.user,
            "win":win

        })


@login_required
def cate(request):
    categorys = request.GET.get('cate')
    if categorys == None:
        catey = None
    else:
        catey = listing.objects.filter(category__name=categorys)    

    
    return render(request, "auctions/cate.html",{
        'a':category.objects.all(),
        'product':catey
    })
@login_required
def watch(request):
    if request.method == 'POST':
        name=request.POST['id']
        add = watchlist(listing=listing.objects.get(pk=name),User=User.objects.get(username=request.user)).save()
        return redirect(reverse("watchlist"))

    else:
        
        return render(request, "auctions/watchlist.html",{
            'all': watchlist.objects.filter(User=User.objects.get(username=request.user))
        })    
@login_required
def create(request):
    if request.method == 'POST':
        f = ListingForm(request.POST,request.FILES)
        print(f.errors)
        if f.is_valid():
            obj = f.save(commit = False)
            obj.User=request.user
            obj.save()

        
            
        return redirect(reverse("index"))
    else:

    
        return render(request, "auctions/create.html",{
            "form":ListingForm()

        }) 


def comments(request):
    if request.method == 'POST':
        des = request.POST["comment"]
        id = request.POST["ID"]
        if des:
            i = comment(listing= listing.objects.get(pk=id), User=User.objects.get(username=request.user),des=des)
            i.save()
            return redirect(reverse("pro",args=[id]))
        else:
            return redirect(reverse("pro",args=[id]))
    


def close(request):
    b = request.POST["id2"]
    a = request.POST["id3"]
    if a:
        win = Bid.objects.filter(start=a).update(win=True)
        print(win)
    


    if b:
        q=listing.objects.filter(id=b).update(active="False")
    return redirect(reverse("pro",args=[b]))    