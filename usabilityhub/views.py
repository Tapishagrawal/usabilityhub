from django.shortcuts import render
def home(request):
    return render(request,'index.html')
def overview(request):
    return render(request,'overview.html')
def card_sorting(request):
    return render(request,'card-sorting.html')
def prototype(request):
    return render(request,'prototype.html')
def design_surveys(request):
    return render(request,'design-surveys.html')
def five_second(request):
    return render(request,'five-second.html')
def preference(request):
    return render(request,'preference.html')
def first_click(request):
    return render(request,'first-click.html')
def panel(request):
    return render(request,'panel.html')
def customer(request):
    return render(request,'customer.html')
def pricing(request):
    return render(request,'pricing.html')
def guides(request):
    return render(request,'guides.html')
