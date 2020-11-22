from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from products.models import Product
from .forms import OrderForm
from .models import Order

@login_required
def order_checkout_view(request):
    qs = Product.objects.filter(featured=True)
    if not qs.exists:
        return redirect('/')
    product = qs.first()
    user = request.user
    order_id = request.session.get('order_id')
    try:
        order_obj = Order.objects.get(id=order_id)
    except:
        order_obj = None
        new_creation = False
    if order_id == None :
        new_creation = True
        order_obj = Order.objects.create(product=product,user=user)
    if order_obj == None and new_creation == False:
        if order_obj.product.id != product.id:
            order_obj = Order.objects.create(product=product,user=user)
    request.session['order_id'] = order_obj.id   
    form = OrderForm(request.POST or None, product=product)
    if form.is_valid():
        order_obj.shipping_address = form.cleaned_data.get("shipping_address")
        order_obj.billing_address = form.cleaned_data.get("billing_address")
    return render(request, 'forms.html', {"form" : form})