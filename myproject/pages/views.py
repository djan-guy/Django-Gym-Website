from django.shortcuts import render, get_object_or_404, redirect
from .models import Page
from .forms import PageForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/users/login/")
def page_list(request):
    pages = Page.objects.order_by('-date')
    return render(request, 'pages/page_list.html', {'pages': pages})

@login_required(login_url="/users/login/")
def page_page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'pages/page_page.html', {'page': page})

@login_required(login_url="/users/login/")
def page_new(request):
    if request.method == "POST":
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pages:list')
    else:
        form = PageForm()
    return render(request, 'pages/page_new.html', {'form': form})


def page_delete(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if request.method == "POST":
        page.delete()
        return redirect('pages:list')
    return redirect('pages:list')