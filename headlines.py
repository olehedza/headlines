from flask import Flask
import feedparser

app = Flask(__name__)

# RAD_SVOBOD_FEED = "https://www.radiosvoboda.org/api/zuogtepggt"

RSS_FEEDS = {'radsv': 'https://www.radiosvoboda.org/api/ziqioejuip',
             'obozr': 'https://www.obozrevatel.com/rss.xml',
             'tv24': 'https://24tv.ua/rss/all.xml',
             'korres': 'http://k.img.com.ua/rss/ua/technews.xml'}


# @app.route("/")
# @app.route("/radsv")
# def radsv():
#     return get_news('radsv')
#
#
# @app.route("/obozr")
# def obozr():
#     return get_news('obozr')
#
#
# @app.route("/tv24")
# def tv24():
#     return get_news("tv24")
#
#
# @app.route("/korres")
# def korres():
#     return get_news("korres")

@app.route("/")
@app.route("/<publication>")
def get_news(publication="radsv"):

    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    last_article = feed['entries'][len(feed['entries'])-1]
    return '''
           <html>
             <body>
               <h1>Headlines</h1>
               <b>{0}</b> <br/>
               <i>{1}</i> <br/>
               <p>{2}</p> <br/> <br/>
               <hr> <hr> <br/> <br/>
               <b>{3}</b> <br/>
               <i>{4}</i> <br/>
               <p>{5}</p> <br/>
             </body>
           </html>
           '''.format(first_article.get("title"),
                      first_article.get("published"),
                      first_article.get("summary"),
                      last_article.get("title"),
                      last_article.get("published"),
                      last_article.get("summary")
                      )


if __name__ == '__main__':
    app.run(port=8000, debug=True)
