import datetime
from datetime import date
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
x=2
sumx=0
print('Введіть число n')
for i in range(int(input())):
    sumx+=x
    x+=3
print('Сума n перших членів арифметичної прогресії х=2, 5, 8...: ' + str(sumx))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
