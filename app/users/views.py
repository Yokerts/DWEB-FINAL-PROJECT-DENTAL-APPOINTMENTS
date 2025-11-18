from django.views.generic import ListView
from .models import User  # o el modelo que uses

class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
