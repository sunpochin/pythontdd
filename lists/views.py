from django.http import HttpResponse
from django.shortcuts import render, redirect
from lists.models import Item, List

# Create your views here.

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text = request.POST['item_text'], list=list_ )
    return redirect('/lists/the-only-list-in-the-world/')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items} )

def home_page(request):
#    if request.method == 'POST':
#        Item.objects.create(text = request.POST['item_text'] )
#        return redirect('/lists/the-only-list-in-the-world/')
#        return redirect('/')

    return render(request, 'home.html')
#    items = Item.objects.all()
#    return render(request, 'home.html', {'items': items } )


