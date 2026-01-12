from django.shortcuts import render

# Create your views here.
def tracking_page(request):
    return render(request, 'tracking/tracking_page.html')