from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
def index(request):
    item_list=Item.objects.all()
    
    context={'item_list':item_list,}
    return render(request,'food/index.html',context)
#class list view
class IndexClassView(ListView):
    model=Item
    template_name='food/index.html'
    context_object_name='item_list'


def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request,'food/detail.html',context)

#class detailed View
class FoodDetails(DetailView):
    model=Item
    template_name='food/detail.html'
#adding food view function
def addfood(request):
    form=ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/addfood.html',{'form':form})
#classbased view for adding food items
class CreateItem(CreateView):
    model=Item
    fields=['item_name','item_desc','item_price','item_image']
    template_name='food/addfood.html'
    def form_valid(self,form):
        form.instance.user_name=self.request.user
        return super().form_valid(form)
    


#updating food view
def update_item(request,id):
    item=Item.objects.get(id=id)
    form =ItemForm(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/addfood.html',{'form':form,'item':item})
#deleting food
def delete_item(request,id):
    item=Item.objects.get(id=id)
    if request.method=="POST":
        item.delete()
        return redirect('food:index')
    return render(request,'food/item-delete.html',{'item':item})
def items(request):
    return HttpResponse('<h1>This is an Item View</h1>')