from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola mundo"


if __name__ == '__main__':
    app.run(debug= True , port=8082)



# Dejé acá
# https://www.youtube.com/watch?v=iPMzFz_2B4E&list=PLagErt3C7iltAydvN6SgCVKsOH4xQQKsk&index=6