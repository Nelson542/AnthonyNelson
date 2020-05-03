import os
from flask import Flask, render_template, request,json
app = Flask(__name__)



SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "static/data", "data.json")
data = json.load(open(json_url))



@app.route('/')
def form():
   return render_template('form.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        word = request.form['word']
        word = word.lower()
        if word in data:
            output = data[word]
            return render_template('result.html',  **locals() )
        elif word.title() in data:
            output =  data[word.title()]
            return render_template('result.html',  **locals())
        else:
            No = "Word doesn't exist"
            return render_template('result.html', No=No)







if __name__ == '__main__':
   app.run(debug = True)