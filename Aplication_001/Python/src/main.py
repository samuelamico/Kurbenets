from flask import Flask, request


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
    if request.method == 'GET':
            return "Hello World"
    else:
        return "Erro"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9999)