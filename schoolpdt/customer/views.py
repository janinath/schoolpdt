from django.shortcuts import render
from seller.models import Product,Category

# Create your views here.
def HoMe(request):
    book_category = Category.objects.get(c_name='BOOKS')
    pdts=Product.objects.filter(category=book_category)
    return render(request,'customer/home.html',{'product':pdts})