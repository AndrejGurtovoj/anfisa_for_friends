from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator

from .forms import ContestForm
from .models import Contest


def proposal(request, pk=None):
    if pk is not None:
        instance = get_object_or_404(Contest, pk=pk)
    else:
        instance = None
    form = ContestForm(
        request.POST or None,
        files=request.FILES or None,
        instance=instance
    )
    if form.is_valid():
        form.save()
    context = {'form': form, 'instance': instance}
    return render(request, 'contest/form.html', context)


def delete_proposal(request, pk):
    instance = get_object_or_404(Contest, pk=pk)
    form = ContestForm(instance=instance)
    if request.method == 'POST':
        instance.delete()
        return redirect('contest:list')
    context = {'form': form, 'instance': instance}
    return render(request, 'contest/form.html', context)


def proposal_list(request):
    contest_proposals = Contest.objects.order_by('id')
    paginator = Paginator(contest_proposals, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'contest_proposals': contest_proposals, 'page_obj': page_obj}
    return render(request, 'contest/contest_list.html', context)
