from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .forms import NameForm
from .models import Eintrag

@login_required()
def get_name(request):


    # if this is a POST request we need to process the form data
    if request.method == 'POST' and 'add' in request.POST:
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #Eintrag.objects.filter(Name=request.user).delete()
            eintrag = form.save(commit=False)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            eintrag.User = request.user  # Set the user object here
            eintrag.pub_date = timezone.now()  # Set the user object here
            eintrag.save()

            return HttpResponseRedirect(request.path)  # generate an empty form

    if request.method == 'POST' and 'delete' in request.POST:
        Eintrag.objects.filter(id=request.POST['pk']).delete()
        #return HttpResponseRedirect(request.path)

    if request.method == 'POST' and 'update' in request.POST:
        eintrag = Eintrag.objects.get(id=request.POST['pk'])
        form = NameForm(instance=eintrag)
        posts = Eintrag.objects.filter(User=request.user)
        Eintrag.objects.filter(id=request.POST['pk']).delete()
        return render(request, 'form/index.html/', {'form': form, 'posts': posts})

        #form = NameForm()
        #form.instance.Anmeldung = Eintrag.objects.get(id=request.POST['pk']).Anmeldung
        #form.fields['Anmeldung'] = Eintrag.objects.get(id=request.POST['pk']).Anmeldung
        #form.fields['Essen'] = Eintrag.objects.get(id=request.POST['pk']).Essen
        #form.fields['Email'] = Eintrag.objects.get(id=request.POST['pk']).Email
        #return HttpResponseRedirect(request.path)
        #posts = Eintrag.objects.filter(Name=request.user)
        #return render(request, 'form/name.html', {'form': form, 'posts': posts})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    posts = Eintrag.objects.filter(User=request.user)
    return render(request, 'form/index.html', {'form': form, 'posts': posts})

