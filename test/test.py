from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup, re
from selenium import webdriver
import pwjt
import requests
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service





app = Flask(__name__, template_folder='my_templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password1234567@localhost:5432/coins'
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'
db = SQLAlchemy(app)



def coining(coin):
    return coin.strip().lower().replace(' ','-')


@app.route('/')
def home():
    return render_template('my.html')


@app.route('/news', methods=['GET'])
def coin_news():
    return render_template('titl.html')


@app.route('/paragraphs', methods=['GET'])
def coin_paragraphs():
    return render_template('sub.html')




@app.route('/news', methods=['POST'])
def newses():
    coin_name = coining(request.form.get('coin_name'))

    m = News.query.filter_by(coin=coin_name).all()

    if not m:
        URL = "https://coinmarketcap.com/currencies/" + coin_name +"/news/"
        options = Options()
        options.headless = True


        browser = webdriver.Firefox(options=options,executable_path='geckodriver.exe')
        browser.get(URL)

        page_source = (browser.page_source).encode('utf-8')

        soup = BeautifulSoup(page_source, 'lxml')
        title_list = [h.getText() for h in soup.find_all('h3', {'class': 'sc-1q9q90x-0 gEZmSc'})]
        p_list = [p.getText() for p in soup.find_all('p',class_=re.compile('svowul-3 ddtKCV'))]

        for title, parag in zip(title_list,p_list):
            news = News(coin=coin_name, title=title, parag=parag)
            db.session.add(news)
        db.session.commit()

        m = News.query.filter_by(coin=coin_name).all()
        return render_template('titl.html', results=m)
    
    return render_template('titl.html', results=m)


@app.route('/paragraphs', methods=['POST'])
def paragraph():
    coin_name = coining(request.form.get('coin_name'))
    m = News.query.filter_by(coin=coin_name).all()

    if not m:
        URL = "https://coinmarketcap.com/currencies/" + coin_name +"/"
        req = requests.get(URL)
        soup = BeautifulSoup(r.text, 'lxml')
        title_tags = soup.find_all(['h2'])
        parag_tags = soup.find_all(['p'])
        
        for p in parag_tags:
            paragraphs = Paragraphs(coin=coin_name, title=title_tags[0].text, paragraph=p.text)
            db.session.add(paragraphs)
        db.session.commit()

        m = Paragraphs.query.filter_by(coin=coin_name).all()
        return render_template('sub.html', results=m)

    return render_template('sub.html', results=m)




class News(db.Model):
    __tablename__ = 'News'
    id = db.Column('id', db.Integer, primary_key=True)
    coin = db.Column('coin', db.String(255))
    title = db.Column('title', db.Text)
    parag = db.Column('parag', db.Text)

    def __init__(self, coin, title, parag):
        self.coin = coin
        self.title = title
        self.parag = parag

    def __repr__(self):
        return f"News('{self.title}', '{self.parag}')"


class Paragraphs(db.Model):
    __tablename__ = 'Paragraphs'
    id = db.Column('id', db.Integer, primary_key=True)
    coin = db.Column('coin', db.String(255))
    title = db.Column('title', db.Text)
    parag = db.Column('parag', db.Text)

    def __init__(self, coin, title, parag):
        self.coin = coin
        self.title = title
        self.parag = parag

    def __repr__(self):
        return f"Paragraphs('{self.title}', '{self.parag}')"


db.drop_all()
db.create_all()


if __name__ == "__main__":
    app.run()
