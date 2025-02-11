from django.shortcuts import render, redirect
from django.views import View


class HomePageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'layout.html')
