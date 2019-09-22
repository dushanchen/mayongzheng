from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import * 


def index(request):
    ctx = {'menu': '首页', 'title': '信托,定容-信托服务网'}

    ctx['links'] = Link.objects.all()
    ctx['config'] = Config.objects.all().first()


    ctx['page'] = page = 1
    if request.method == 'POST':
        ctx['page'] = page = int(request.POST.get('page', ''))

    ctx['hot1'] = Article.objects.all().order_by('-read')[:10]                           # 热门文章
    ctx['hot2'] = Article.objects.all().order_by('-comment_num')[:10]                    # 热评文章
    ctx['messages'] = Message.objects.all().order_by('-create_time')[:5]                  # 最新留言
    ctx['top'] = Article.objects.filter(head=1).order_by('-update_time')[:3]              # 头条推荐
    ctx['scroll_top'] = Article.objects.filter(scroll_head=1).order_by('-update_time')[:3]       # 滚动头条

    articles = Article.objects.all().order_by('-create_time')  # 最新文章

    paginator = Paginator(articles, 10) 

    try:
        articles = paginator.page(page)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages) 
    
    ctx['articles'] = articles

    return render(request, 'index.html', ctx)



def xintuo(request):
    ctx = {'menu': '信托', 'title': '信托产品-信托服务网'}

    ctx['links'] = Link.objects.all()
    ctx['config'] = Config.objects.all().first()



    ctx['page'] = page = 1
    if request.method == 'POST':
        ctx['page'] = int(request.POST.get('page', ''))

    ctx['hot1'] = Article.objects.all().order_by('-read')[:10]                           # 热门文章
    ctx['hot2'] = Article.objects.all().order_by('-comment_num')[:10]                    # 热评文章
    ctx['new10'] = Article.objects.all().order_by('-create_time')[:10]                   # 最新文章

    
    articles = Article.objects.filter(type=0).order_by('top','-create_time')  # 最新文章

    paginator = Paginator(articles, 10) 

    try:
        articles = paginator.page(page)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages) 
    
    ctx['articles'] = articles

    return render(request, 'second.html', ctx)


def dingrong(request):
    ctx = {'menu': '定容工具', 'title': '定融产品-信托服务网'}

    ctx['links'] = Link.objects.all()
    ctx['config'] = Config.objects.all().first()


    ctx['page'] = page = 1
    if request.method == 'POST':
        ctx['page'] = int(request.POST.get('page', ''))

    ctx['hot1'] = Article.objects.all().order_by('-read')[:10]                           # 热门文章
    ctx['hot2'] = Article.objects.all().order_by('-comment_num')[:10]                    # 热评文章
    ctx['new10'] = Article.objects.all().order_by('-create_time')[:10]                    # 最新文章
 
    articles = Article.objects.filter(type=1).order_by('top','-create_time')  # 最新文章

    paginator = Paginator(articles, 10) 

    try:
        articles = paginator.page(page)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages) 
    
    ctx['articles'] = articles

    return render(request, 'second.html', ctx)


def news(request):
    ctx = {'menu': '行业资讯', 'title': '信托资讯-信托服务网'}


    ctx['links'] = Link.objects.all()
    ctx['config'] = Config.objects.all().first()


    ctx['page'] = page = 1
    if request.method == 'POST':
        ctx['page'] = int(request.POST.get('page', ''))

    ctx['hot1'] = Article.objects.all().order_by('-read')[:10]                           # 热门文章
    ctx['hot2'] = Article.objects.all().order_by('-comment_num')[:10]                    # 热评文章
    ctx['new10'] = Article.objects.all().order_by('-create_time')[:10]                   # 最新文章

    articles = Article.objects.filter(type=2).order_by('top','-create_time')  # 最新文章

    paginator = Paginator(articles, 10) 

    try:
        articles = paginator.page(page)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages) 
    
    ctx['articles'] = articles

    return render(request, 'second.html', ctx)


def article(request, id):
    ctx = {'title': '信托,定融-信托服务网'}

    ctx['links'] = Link.objects.all()
    ctx['config'] = Config.objects.all().first()


    ctx['a'] = a = Article.objects.filter(id=id).first()
    if a: 
        ctx['menu'] = a.get_type_display()
    print(ctx['menu'])
    ctx['hot1'] = Article.objects.all().order_by('-read')[:10]                           # 热门文章
    ctx['hot2'] = Article.objects.all().order_by('-comment_num')[:10]                    # 热评文章
    ctx['new10'] = Article.objects.all().order_by('-create_time')[:10]                   # 最新文章
    ctx['relations'] = Article.objects.filter(type=a.type if a else 0).exclude(id=id).order_by('-read')[:8] # 相关文章

    return render(request, 'detail.html', ctx)
