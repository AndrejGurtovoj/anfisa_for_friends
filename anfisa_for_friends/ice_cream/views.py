from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from ice_cream.models import IceCream


def ice_cream_detail(request, pk):
    template_name = 'ice_cream/detail.html'
    ice_cream = get_object_or_404(
        IceCream.objects.filter(
            is_published=True, category__is_published=True
            ),
        pk=pk
    )
    context = {
        'ice_cream': ice_cream,
    }
    return render(request, template_name, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    ice_cream_list = IceCream.objects.order_by('id', 'category').filter(
        is_published=True,
        category__is_published=True
    ).order_by('category')
    paginator = Paginator(ice_cream_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'ice_cream_list': ice_cream_list, 'page_obj': page_obj}
    return render(request, template, context)
