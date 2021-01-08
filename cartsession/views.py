from	django.shortcuts	import	render,	redirect,	get_object_or_404
from	django.views.decorators.http	import	require_POST
from	cart.models	import	product
from	.cart	import	Cart
from	.forms	import	CartAddProductForm
from cart.views import product_list
def	cart_detail(request):
    cart	=	Cart(request)
    for	item	in	cart:
        item['update_quantity_form']=CartAddProductForm(initial={'quantity':	item['quantity'],'update':	True})
    
    return	render(request,	'cartdetails.html',	{'cart':	cart})

@require_POST
def	cart_add(request,	product_id):
        cart	=	Cart(request)
        Product	=	get_object_or_404(product,	id=product_id)
        form	=	CartAddProductForm(request.POST)
        if	form.is_valid():
            cd	=	form.cleaned_data
            cart.add(product=Product,quantity=cd['quantity'],update_quantity=cd['update'])
        return	redirect('cartsession:cart_detail')
def	cart_remove(request,	product_id):
                cart	=	Cart(request)
                Product	=	get_object_or_404(product,	id=product_id)
                cart.remove(Product)
                return	redirect('cartsession:cart_detail')
def clear(request):
    cart=Cart(request)
    cart.clear()
    return redirect('cart:product_list')