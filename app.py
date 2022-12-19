from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    n = 5
    x = 2
    for i in range(n):
        x = x+x+3
    return x

if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0')
