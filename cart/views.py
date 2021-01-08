from django.shortcuts import render,	get_object_or_404
from	.models	import	category,	product
from cartsession.forms import CartAddProductForm
def	product_list(request,	category_slug=None):
        product_category=None
        categories=category.objects.all()
        products=product.objects.filter(available=True)
        if	category_slug:
            product_category=get_object_or_404(categories,slug=category_slug)
            products=products.filter(category=category)
        return render(request,'list.html',{'category':	product_category,'categories':	categories,'products':products})
def	product_detail(request,	id,	slug):
    
    product_info	=	get_object_or_404(product,id=id,slug=slug,available=True)
    cart_product_form=CartAddProductForm()
    return	render(request,'detail.html',{'product':product_info,'cart_product_form':cart_product_form})        