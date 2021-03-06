from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404


from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    # function default
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(
    #         *args, **kwargs)
    #     print(context)
    #     return context
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)


# Detail

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "product/detail.html"

    # function default
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(
            *args, **kwargs)
        print(context)
        return context
    
    def get_object(self,*args,**kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("product doesn't exist")
        return instance

    #def get_queryset(self, *args, **kwargs):
        #request = self.request
        #return Product.objects.all()
    


def product_detail_view(request, pk=None, *args, **kwargs):
    print(args)
    #instance = Product.objects.get(pk=pk)
    #instance = get_object_or_404(Product, pk=pk)
    #try:
        #instance = Product.objects.get(id=pk)
    #except Product.DoestNotExist:
        #print('Not product here')
        #raise Http404("product doesn't exist")
    #except:
        #print("Huh?")

    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("product doesn't exist")


    #instance =  Product.objects.get_by_id(pk)
    
   # qs = Product.objects.filter(id=pk)
    
    #print(qs)
    #if qs.exists() and qs.count() == 1:
        instance = qs.first()
   # else:    
      #  raise Http404("product doesn't exist")

    context = {
        'object': instace
    }
    return render(request, "products/detail.html", context)
