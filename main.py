from flask import Flask, render_template, request, redirect
from werkzeug.utils import html
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
    
# @app.route('/index')
# def index():
#     return render_template("index.html")

@app.route('/infertility')
def infertility():
    return render_template("infertility.html")

@app.route('/married')
def married():
    return render_template("married.html")

@app.route('/menopause')
def menopause():
    return render_template("menopause.html")

@app.route('/new_moms')
def new_moms():
    return render_template("new-moms.html")

@app.route('/portfolio-details')
def portfolio_details():
    return render_template("portfolio-details.html")

@app.route('/pregnant')
def pregnant():
    return render_template("pregnant.html")

@app.route('/teenage')
def teenage():
    return render_template("teenage.html")

@app.route('/pregtracker')
def pregtracker():
    return render_template("pregtracker.html")


@app.route('/edu')
def edu():
    return render_template("edu.html")

@app.route('/puberty')
def puberty():
    return render_template("puberty.html")

@app.route('/gender')
def gender():
    return render_template("gender.html")

@app.route('/abuse')
def abuse():
    return render_template("abuse.html")

@app.route('/one')
def one():
    return render_template("one.html")

@app.route('/two')
def two():
    return render_template("two.html")

@app.route('/three')
def three():
    return render_template("three.html")

@app.route('/preghealth')
def preghealth():
    return render_template("preghealth.html")

@app.route('/firsttrimister')
def firsttrimister():
    return render_template("firsttrimister.html")

@app.route('/secondtrimister')
def secondtrimister():
    return render_template("secondtrimister.html")

@app.route('/thirdtrimister')
def thirdtrimister():
    return render_template("thirdtrimister.html")

@app.route('/contraceptive')
def contraceptive():
    return render_template("contraceptive.html")

@app.route('/alternative')
def alternative():
    return render_template("alternative.html")

if __name__ == "__main__":
    app.run()