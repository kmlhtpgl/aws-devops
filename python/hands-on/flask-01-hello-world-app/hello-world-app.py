from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return "Hello World!"

@app.route('/kemal')
def second():
    return "This is Kemal`s page"

@app.route('/third/subthird')
def third():
    return "This is the subpage of thirdpage"

@app.route("/forth/<string:id>")
def forth(id):
    return f'Id of this page is {id}'

if __name__=='__main__':
    app.run(debug = True)