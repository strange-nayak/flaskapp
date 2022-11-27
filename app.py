from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/hello', methods=['POST','GET'])
def helloWorld():
    if request.method == 'GET':
        return "Hello World"
    if request.method == 'POST':
        return 'Namaste'

@app.route('/')
def indexRoute():
    return render_template("index.html")

@app.route('/add')
def addRoute():
    n1 = int(request.args.get("num1"))
    n2 = int(request.args.get("num2"))
    total = str(n1+n2)

    return render_template("output.html", sum=total, num1=n1,num2=n2)

# http://127.0.0.1/add?num1=2&num2=3
# http://127.0.0.1/add/2/3
# http://abc.xyz.com/post

if __name__ == "__main__":
    app.run(debug=True,port=80)