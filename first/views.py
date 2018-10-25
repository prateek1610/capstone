from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from first.forms import MenuForm
from first.models import fooditem
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from first.forms import MenuForm
# Create your views here.
@login_required
def welcome(request,pk=fooditem.pk):
    #enter = get_object_or_404(fooditem,pk=pk)
    return render(request, 'mess/base.html')

def about(request):
    return render(request,'mess/about.html')

@login_required
def menu_entry(request):
    if request.method == "POST":
        if request.method == "POST":
            mess_form = MenuForm(data=request.POST)
            mess_form.day = 'MONDAY'
            if mess_form.is_valid():
                mess = mess_form.save(commit=False)
                # mess.item_name=item_name
                # mess.username=request.user
                mess.save()
                return redirect('mess_update')
            else:
                print(mess_form.errors)
        else:
            mess_form = MenuForm()
        return render(request, 'mess/mess_update.html',
                      {'mess_form': mess_form, 'lunch_time': lunch_time, 'breakfast_time': breakfast_time
                          , 'dinner_time': dinner_time, 'week_day': week_days, 'item1': item1})


def viewmenu(request):
    query_results = fooditem.objects.all()
    return render(request,'mess/view_menu.html',{'query_results':query_results})

