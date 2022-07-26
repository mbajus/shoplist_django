from django.shortcuts import render
from .models import ShopList, Item

def index(response):
    return render(response, 'main/home.html', {})

def mylist(response):
    if response.user.is_authenticated:
        if response.method == 'POST':
            print(response.POST)
            if response.POST.get("addlist"):
                txt = response.POST.get("newlist")
                if len(txt) != 0:
                    sl = ShopList.objects.create(user = response.user, name=txt)
                    sl.save()           
        return render(response, 'main/mylists.html', {})
    else:
        return render(response, 'main/home.html', {})

def curlist(response, id):    
    sl = ShopList.objects.get(id = id)
    print(sl)
    if response.user.is_authenticated:
        if sl in response.user.shoplist.all():
            if response.method == "POST":
                print(response.POST)                
                if response.POST.get("new"):
                    txt = response.POST.get("new")
                    if len(txt) > 2:
                        sl.item_set.create(name = txt, complete = False)
                    else:
                        print("invalid")
                    for item in sl.item_set.all():
                        if response.POST.get("c" + str(item.id)) == "clicked":
                            item.complete = True
                        else:
                            item.complete = False
                        item.save()                
                elif response.POST.get("save"):
                    for item in sl.item_set.all():
                        if response.POST.get("c" + str(item.id)) == "clicked":
                            item.complete = True
                        else:
                            item.complete = False
                        item.save()   
                elif response.POST.get("delItem"):
                    id = response.POST.get("delItem")
                    sl.item_set.filter(id=id).delete()
                elif response.POST.get("delList"):
                    sl.delete()             
                    return render(response, 'main/mylists.html', {})    
            return render(response, "main\list.html", {"sl": sl})
    return render(response, "main\home.html", {})
