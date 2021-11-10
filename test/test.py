from flask import Flask, render_template
from flask import request
from flask.json import jsonify
import jwt
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from bs4 import BeautifulSoup
from urllib.request import urlopen


app = Flask(__name__,template_folder="my_templates")
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234567@localhost:5432/coin'
db = SQLAlchemy(app)
class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(255),nullable=False)
    par= db.Column(db.String(255),nullable=False)
    link= db.Column(db.String(255),nullable=False)



class Paragraphs(db.Model):
    __tablename__ = 'paragraph'
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255),nullable=False )
    price=db.Column(db.Float,nullable=False )
    hours=db.Column(db.Float,nullable=False )
    week=db.Column(db.Float,nullable=False )
    marketCap=db.Column(db.Integer,nullable=False )
    volume=db.Column(db.Integer,nullable=False )




@app.route("/coin", methods=["GET", "POST"])
def coin():
    refresh()
    if request.method == "POST":
        coin = request.form["CoinName"]
          
    return render_template("login.html")

def refresh():
    url = "https://coinmarketcap.com"
    html = urlopen(url)
    soup = BeautifulSoup(html, 'lxml')
    response=soup.find_all("p")
    paginations_count=int(soup.find("ul", class_="pagination").find_all("a")[-2].text)
    print(paginations_count)
    
    
    paragraphs=soup.find("table", class_="h7vnx2-2").find_all("tr")
    
    for i in paragraphs:
        
        
            some_name = ""
        some_market = 0
        some_name = i.find_all("td")[2].get('a').text
    
        some_v = i.find_all("td")[2].find('span',class_="sc-1ow4cwt-0").text.replace('$',"")
        some_v = some_v.replace('T',"")
        #some_v = some_v.replace('.',",")
        some_v = some_v.replace('B',"")
        some_market = float(some_v)
       
        para_1 = Paragraphs(name=some_name,marketCap=some_market)
        db.session.add(para_1)
        print(para_1.name,para_1.marketCap)

    #for page in range(2,paginations_count+1):
    #    url="https://coinmarketcap.com/?page="+str(page)
         
    



    





if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()