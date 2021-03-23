from flask import Flask,render_template, url_for, request, redirect
import sys
import logging

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/', methods=['POST','GET'])
def home():
    global height
    if request.method == 'POST':
        height = request.form['height']
        return redirect('/opr_ves')
    else:
        return render_template("index.html")

@app.route('/opr_ves', methods=['GET','post'])
def opr():
    weight = int(height) - 110
    height2 = (int(height) * 0.01) * (int(height) * 0.01)
    index = weight/height2
    return render_template("rost.html",weight = weight,index = index)
if __name__ == "__main__":
    app.run()