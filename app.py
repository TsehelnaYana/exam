from flask import Flask
app = Flask(__name__)

@app.route('/')
  def progress(n):
    d = 3
    a = 2
    return a + n * d

if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0')
