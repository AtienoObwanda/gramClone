from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.utils.decorators import method_decorator

from .forms import newPostForm

# @login_required
# def newImage(request):
#     if request.method == 'POST':
#         form = newPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # messages.success(request, f'Account created successfully! You can now login')
#             return redirect('feed')
#     else:
#         form = newPostForm()
#     return render(request, 'app/newImage.html', {'form': form})




# @login_required
# def feed(request):
#     images = Image.getImages()
    
#     return render(request, 'app/feed.html', {"images": images })


@method_decorator(login_required, name='dispatch')
class ImageListView(ListView):
    model = Image
    template_name = 'app/feed.html'
    context_object_name = 'images'
    ordering =['-uploadDate'] 



@method_decorator(login_required, name='dispatch')
class ImageDetailView(DetailView):
    model = Image
    template_name = 'app/ImgDetail.html'    
    context_object_name = 'image'

@method_decorator(login_required, name='dispatch')
class ImageCreateView(CreateView):
    model = Image
    fields=['image', 'caption']
    template_name = 'app/newImage.html'    
    def form_valid(self, form):
        form.instance.author = self.request.user
        # form.save()
        return super().form_valid(form)
        # return redirect('feed')

        



# @login_required
# def addPost(request):
    
#     return render(request, 'app/home.html')