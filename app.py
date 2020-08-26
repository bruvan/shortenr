from flask import Flask,render_template,request,redirect
import db


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',long="",short="",result="")

@app.route("/add",methods=['POST'])
def add():
    result= db.add_data(request.form['long'],request.form['short'])
    return render_template('index.html',long = request.form['long'],short=request.form['short'],result=result)

@app.route("/<short>")
def redirect_to(short):
    long = db.find_url(short)
    if long == 'LINK NOT FOUND SORRI':
        return long
    else:
        return redirect(long)