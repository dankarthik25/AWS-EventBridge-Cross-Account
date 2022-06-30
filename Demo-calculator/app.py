from flask import Flask, render_template, request


app = Flask(__name__) 

@app.route('/')
def man():
    return render_template('home.html')


@app.route('/Multiply', methods=['POST'])
def home():
    data1 = request.form['d1']
    data2 = request.form['d2']
    data3 = int(data1)*int(data2)
    return render_template('after.html', data=data3)
@app.route('/Add', methods=['POST'])
def home1():
    data1 = request.form['d4']
    data2 = request.form['d5']
    data3 = int(data1)+int(data2)
    return render_template('after.html', data=data3)    
@app.route('/Subtraction', methods=['POST'])
def home2():
    data1 = request.form['d6']
    data2 = request.form['d7']
    data3 = int(data1)-int(data2)
    return render_template('after.html', data=data3)


if __name__=='__main__':
    app.run(host='0.0.0.0',port=80,debug=True)