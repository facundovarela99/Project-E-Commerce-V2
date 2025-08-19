from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from ..forms import UserForm
from ..models import Product

class UserListView(ListView):
    model = Product

class UserCreateView(CreateView):
    model = Product

class UserDeleteView(DeleteView):
    model = Product

class UserDetail(DetailView):
    model = Product

class UserUpdate(UpdateView):
    model = Product