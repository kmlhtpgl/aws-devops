from flask import Flask, render_template, request

app=Flask(__name__)


@app.route('/', methods=["GET"])
def index():
        return render_template('index.html')

num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def num2roman(number):

    number_roman = ''
    

    if number > 0 and number < 4000:
        for i, r in num_map:
            while number >= i:
                number_roman += r
                number -= i

    return number_roman        

@app.route('/total',methods=["GET","POST"])
def total():
        if request.method=="POST":
                number=request.form.get("number")
                return render_template('result.html',total=num2roman(int(number)))
        else:
                return render_template('result.html')

                
                

if __name__=='__main__':
        app.run(host='0.0.0.0',port=80)                                