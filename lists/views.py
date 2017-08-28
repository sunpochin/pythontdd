from django.http import HttpResponse
from django.shortcuts import render, redirect
from lists.models import Item, List

# Create your views here.

def add_item(request, list_id):
    # how to add item?
    list_ = List.objects.get(id=list_id)

    Item.objects.create(text = request.POST['item_text'], list = list_ )
    print('request.POST[\'item_text\']: ', request.POST['item_text'] )

    return redirect(f'/lists/{list_.id}/')
    pass


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text = request.POST['item_text'], list=list_ )
#    return redirect('/lists/the-only-list-in-the-world/')
    return redirect(f'/lists/{list_.id}/')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
#    items = Item.objects.filter(list=list_)
#    return render(request, 'list.html', {'items': items} )
    return render(request, 'list.html', {'list': list_ } )



def home_page(request):
#    if request.method == 'POST':
#        Item.objects.create(text = request.POST['item_text'] )
#        return redirect('/lists/the-only-list-in-the-world/')
#        return redirect('/')

    return render(request, 'home.html')
#    items = Item.objects.all()
#    return render(request, 'home.html', {'items': items } )


