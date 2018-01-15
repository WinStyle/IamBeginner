from django.shortcuts import render
from django.shortcuts import render_to_response
from MyBlog.models import *


# Create your views here.
def main(request):
    articleList = Article.objects.all()

    return render_to_response('index.html',{'articleList':articleList})

def articleDetial(request,id_no):
    article = Article.objects.get(id=id_no)
    return  render_to_response('content.html',{'article':article})
def ICknowledge(request):
    articleList = Article.objects.filter(target=ArticleTarget.objects.get(targetName='IC知识'))
    return render_to_response('index.html', {'articleList': articleList})
def testTheoretics(request):
    articleList = Article.objects.filter(target=ArticleTarget.objects.get(targetName='测试理论'))
    return render_to_response('index.html', {'articleList': articleList})
def ATETest(request):
    articleList = Article.objects.filter(target=ArticleTarget.objects.get(targetName='ATE测试'))
    return render_to_response('index.html', {'articleList': articleList})
def DataAnalysis(request):
    articleList = Article.objects.filter(target=ArticleTarget.objects.get(targetName='数据分析'))
    return render_to_response('index.html', {'articleList': articleList})