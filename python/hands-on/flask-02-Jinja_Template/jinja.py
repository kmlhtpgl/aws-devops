from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template("index.html", number=12, number_2=40)

@app.route('/kemal')
def number():
    var1, var2 = 23, 45
    return render_template('body.html', num1=var1, num2=var2, multiplication=var1*var2)


if __name__=='__main__':
    app.run(debug = True)