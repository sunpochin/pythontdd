from django.http import HttpResponse
from django.shortcuts import render, redirect
from lists.models import Item

# Create your views here.

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text = request.POST['item_text'] )
        return redirect('/')

#    return render(request, 'home.html')
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items } )

'''
def home_page(request):
#    print('debug request.POST: ', request.POST.get('item_text', ''))
    if request.method == 'POST':
        new_item_text = request.POST.get('item_text', '')
        
        #Item.objects.create(text = new_item_text)
        item = Item(text = new_item_text)
        item.save()
    else:
        new_item_text = ''
    return render(request, 'home.html', {
#        'new_item_text': request.POST['item_text']
#        'new_item_text': request.POST.get('item_text', '')
        'new_item_text': new_item_text
    } )
#    if request.method == 'POST':
#        return HttpResponse(request.POST['item_text'])
    return render(request, 'home.html')
'''

