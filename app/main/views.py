from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news , get_article



@main.route('/', methods=['GET'])
def index():

    '''
    view news page function that returns the news details  and its data
    '''
    
    news = get_news('category')
    articlesss = news['articles']
    url = []
    desc =[]
    news = []
    image = []
    time = []
    for i in range(len(articlesss)):
        myarticles = articlesss[i]
        desc.append(myarticles['title'])
        news.append(myarticles['description'])
        image.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        time.append(myarticles['publishedAt'])
    mylist = zip(desc,news,image,url,time)
    return render_template('index.html',context = mylist )





@main.route('/source/<id>')
def article(id):
    '''
    view news page function that returns the news details  and its data
    '''
    
    articles = get_article(id)
    title = "News"
    
    return render_template('article.html', articles = articles, title=title)






  
    
    