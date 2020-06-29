from flask import Flask, render_template
from newsapi import NewsApiClient
 
 
 
 
app = Flask(__name__)
 
 
 
@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="bdaeccc3c6254656a10a400046032975")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news,the-verge")
 
 
    articles = topheadlines['articles']
 
    title = []
    desc = []
    auth = []
    published_at = []
    img = []
 
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
 
        title.append(myarticles['title'])
        desc.append(myarticles['description'])
        auth.append(myarticles['author'])
        published_at.append(myarticles['publishedAt'])
        img.append(myarticles['urlToImage'])
 
 
 
    mylist = zip(title, desc, auth, published_at, img)
 
 
    return render_template('index.html', context = mylist)
 
 
 
@app.route('/bbc')
def bbc():
    newsapi = NewsApiClient(api_key="YOUR-API-KEY")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")
 
    articles = topheadlines['articles']
 
    title = []
    desc = []
    auth = []
    published_at = []
    img = []
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
        title.append(myarticles['title'])
        desc.append(myarticles['description'])
        auth.append(myarticles['author'])
        published_at.append(myarticles['publishedAt'])
        img.append(myarticles['urlToImage'])
        
    mylist = zip(title, desc, auth, published_at, img)
 
    return render_template('bbc.html', context=mylist)
 
 
 
if __name__ == "__main__":
    app.run(debug=True)