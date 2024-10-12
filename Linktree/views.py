from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Profile, Links

class Link_class_view(ListView):
    model = Links # we just have to assign model to a variable model to fetch all object from db
    # it will now by default look for model_list.html and render our model data --> in our case it is link_list.html

class Link_create_view(CreateView):
    model = Links
    fields = "__all__"
    success_url = reverse_lazy("link_list")

class Link_update_view(UpdateView):
    model = Links
    fields = ['text', 'url']
    success_url = reverse_lazy("link_list")

class Link_delete_view(DeleteView):
    model = Links
    success_url = reverse_lazy("link_list")

# class profile_list_view(ListView):
#     model = Links
#     template_name = "profile.html"
#     def get_queryset(self):
#         # Filter links where clicks are greater than 10
#         queryset = Links.objects.filter()
#         # Optionally, select specific fields
#         # queryset = Links.objects.filter(clicks__gt=10).values('name', 'url')
#         return queryset

def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    print("################3")
    print(profile)
    print("################3")
    links = profile.link.all()
    print(links)
    context = {
        'profile': profile,
        'links': links
    }

    return render(request, 'Linktree/profile.html', context)