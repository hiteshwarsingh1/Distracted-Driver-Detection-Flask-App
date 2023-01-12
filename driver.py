from flask import Flask , render_template, request
import model as m

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/prediction", methods = ['GET','POST'])
def upload_image():  
    print("-----------------------------------------------",request.method,"--------------------------------------------")
    if request.method == 'POST':
        file = request.files['file']
        if file:
            driver_pred = m.detect(file)
            prediction = driver_pred
            # print(drp)
            return render_template('index.html',prediction = prediction)
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')