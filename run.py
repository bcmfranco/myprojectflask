from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola mundo test"

if __name__ == '__main__':
    app.run(debug= True , port=8082)