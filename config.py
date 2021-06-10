import os

class Config:

    NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?q=apple&from=2021-06-08&to=2021-06-08&sortBy=popularity&apiKey=6fd6f306204d4fc79908618ff7bc14ea'

    NEWS_ARTICLE_URL =  'https://newsapi.org/v2/everything?q=Apple&from=2021-06-09&sortBy=popularity&apiKey={}'

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}