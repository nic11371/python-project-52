from django.shortcuts import render, redirect
from django.views import View
from .models import CustomStatus
from .forms import StatusForm
from django.urls import reverse
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class IndexStatusView(View):

    def get(self, request, *args, **kwargs):
        status = CustomStatus.objects.all()
        return render(request, 'statuses/index.html', context={
            'statuses': status,
        })


class StatusCreateView(View):

    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'statuses/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(request.POST)
        form.save()
        messages.success(
            request, _("Status was created successfully.")
        )
        return redirect(reverse('statuses'))


class StatusUpdateView(View):
    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = CustomStatus.objects.get(id=status_id)
        form = StatusForm(instance=status)
        return render(
            request, 'statuses/update.html', {
                'form': form, 'status_id': status_id})

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = CustomStatus.objects.get(id=status_id)
        form = StatusForm(request.POST, instance=status)
        form.save()
        messages.success(request, _("Status was changed successfully"))
        return redirect(reverse('statuses'))


class StatusDeleteView(View):
    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = CustomStatus.objects.get(id=status_id)
        form = StatusForm(status)
        return render(
            request, 'statuses/delete.html', {
                'form': form, 'status': status})

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = CustomStatus.objects.get(id=status_id)
        status.delete()
        messages.success(request, _("Status was deleted successfully"))
        return redirect(reverse('statuses'))
