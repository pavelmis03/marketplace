from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from .models import Category, Product


# class ProductListView(ListView):
#     template_name = 'shop/product/list.html'
#     queryset = Product.objects.all()
#     def get_context_data(self, **kwargs):
#         context = super(ProductListView, self).get_context_data(**kwargs)
#         context['category_list'] = Category.objects.all()
#         return context


def product_list(request, category_slug=None):
    """
    Страница со списком товаров

    :param request: объект c деталями запроса
    :type request: :class:`django.http.HttpRequest`
    :param category_slug: заготовка категории
    :return: объект ответа сервера с HTML-кодом внутри
    """
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    """
    Страница свойства товара

    :param request: объект c деталями запроса
    :type request: :class:`django.http.HttpRequest`
    :param id: идентификатор
    :param slug: заготовка
    :return: объект ответа сервера с HTML-кодом внутри
    """
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)
