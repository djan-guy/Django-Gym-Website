from django.shortcuts import render, redirect
from .forms import MembershipForm
from django.contrib.auth.decorators import login_required

@login_required(login_url="/users/login/")
def membership_page(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('membership:membership_verification')
    else:
        form = MembershipForm()

    return render(request, 'membership/membership_page.html', {'form': form})

@login_required(login_url="/users/login/")
def membership_verification(request):
    return render(request, 'membership/membership_verification.html')
