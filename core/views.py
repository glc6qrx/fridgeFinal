from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


from .models import Item

@login_required
def index(request):
    items = Item.objects.all()
    context = {
        'fridge_items' : items,
    }
    return render(request, 'index.html',context)


from .forms import ItemForm


@login_required
# Create your views here.
def add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ItemForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            i = Item(name = form.cleaned_data['item_name'])
            i.save()
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ItemForm()

    return render(request, 'add.html', {'form': form})