from django.shortcuts import render, redirect
from .models import Double
from .forms import DoubleForm
import re


def double_list(request):
    double = Double.objects.all()
    return render(request, 'double_list.html', {'double': double})



def double_create(request):
    form = DoubleForm(request.POST or None)
    name_user = form.data.get('name')
    val_user = request.POST.get('value')
    value_user = int(val_user or 0)
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')


    if value_user > 1000 or value_user < -1000:
        erro_value = 'Please do not use value greater than 1000 or greater than -1000'
        return render(request, 'double_create.html', {'form': form, 'erro_value': erro_value})


    elif form.is_valid() and (regex.search(name_user) != None):
        erro_char = "Please Don't use especial character!"
        return render(request, 'double_create.html', {'form': form, 'erro_char': erro_char})

    elif form.is_valid() and (regex.search(name_user) == None):
        form.save()
        return redirect('double_list')
    return render(request, 'double_create.html', {'form': form})



