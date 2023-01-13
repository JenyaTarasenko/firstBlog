from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
from .forms import AddPostForm
from django.views.generic import ListView, DetailView, CreateView
from .utils import *

category = ["Список товаров",  "Страница категорий"]

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Довать статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]



#класс представления
class WomenHome(ListView):
    paginate_by = 3    # нумерация страницы(пагинация)
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
#    extra_context = {'title': "Главная страница"}


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        #context['cat_selected'] = 0 #ховер все категории
        return context

    #все опубликованные статьи
    def get_queryset(self):
        return Women.objects.filter(is_published=True)








#передать переменную menu
#    def get_context_data(self, *, object_list=None, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['menu'] = menu
#        context['title'] = 'Главная страница'
#        context['cat_selected'] = 0 #сделать ховер выбранного меню
#        return context

#вывести все опубликованные статьи
   # def get_queryset(self):
      #  return Women.objects.filter(is_published=True)

#def index(request):
    #posts = Women.objects.all()
    #return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница' })


# первое представление
#def index(request):
   # return render(request, 'women/index.html', {'menu': menu, 'title': "Главная страница"})

def about(request):
    contact_list = Women.objects.all()
    paginator = Paginator(contact_list, 3)# работа пагинатора в функции


    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'women/about.html', {'page_obj': page_obj, 'category': category, 'title': "Страница О НАС"})





# форма для добавления новости + (ответ если форма неверна )
#def addpage(request):
#    if request.method == 'POST':
#        form = AddPostForm(request.POST, request.FILES)
 #       if form.is_valid():
            #проверка валидности
            #print(form.cleaned_data)
        #выдает ошибку если одинаковый пост в базе
            #try:
               # Women.objects.create(**form.cleaned_data)
#            form.save()
               # return redirect('home')
            #except:
               # form.add_error(None, 'Добавить ошибку поста')
 #   else:
  #      form = AddPostForm()
   # return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': "Добавить статью"})

def contact(request):
    return HttpResponse("Контакты")

def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ваша страница не найдена</h1>')

#посты  отображение статьи
#def show_post(request, post_id):
    #return HttpResponse(f"Отображение статьи с id={post_id}



# категория
#def show_category(request, cat_id):
#    posts = Women.objects.filter(cat_id=cat_id)


#    if len(posts) == 0:
#       raise Http404()

#    context = {
#        'post': posts,
#        'menu': menu,
#        'title': "Отображение по рубрикам",
#        'cat_selected': cat_id,
#    }
#    return render(request, 'women/index.html', context=context)


#класс Category
class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False #если нет записей исключение 404

    def get_queryset(self):
        return Women.objects.all.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория-' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context

#def show_post(request, post_slug):
#    post = get_object_or_404(Women, slug=post_slug)

#    context = {
#        'post': post,
#        'menu': menu,
#        'title': post.title,
#        'cat_selected': post.cat_id,
#    }
#    return render(request, 'women/post.html', context=context)

#функция отображения поста
class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name ='post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context



class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавить статью'
        return context

