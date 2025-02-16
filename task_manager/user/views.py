from django.shortcuts import render
from django.views import View


class IndexUserView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/index.html')
