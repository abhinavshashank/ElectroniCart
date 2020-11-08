from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Product
from .forms import ProductModelForm

# Create your views here.
def search_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello, home_view</h1>")
    query = request.GET.get('q')
    qs = Product.objects.filter(title__icontains = query[0])
    print(qs)
    context = {"name":"Abhinav Shashank Choudhary"}
    return render(request, 'home.html', context)

# def product_create_view(request, *args, **kwargs):
#     if request.method == "POST":
#         post_data = request.POST or None
#         if post_data != None:
#             my_form = ProductForm(request.POST)
#             if my_form.is_valid():
#                 print(my_form.cleaned_data.get('title'))
#                 title_from_input = my_form.cleaned_data.get('title')
#                 Product.objects.create(title=title_from_input)
#     return render(request, 'forms.html', {})
@staff_member_required
def product_create_view(request, *args, **kwargs):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        # data = form.cleaned_data
        # Product.objects.create(**data)
        
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = ProductModelForm()
    return render(request, 'forms.html', {"form":form})

def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(pk = pk)
    except Product.DoesNotExist:
        raise Http404
    #return HttpResponse(f'Product ID = {obj.id}')
    return render(request, 'products/detail.html', {"object":obj})

def product_list_view(request, *args, **kwargs):
    qs = Product.objects.all()
    context = {"products":qs}
    return render(request, 'products/list.html', context)

def product_api_detail_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message":"Not Found"})
    return JsonResponse({'id': obj.id})