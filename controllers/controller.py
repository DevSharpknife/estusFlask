from app import app

@app.route('/<name>')
def greet(name):
    return f"Hello {name}!"

# @app.route('/')
# def index():
#     return "El Nombre! Writing numbers in the desert sand! EL NOMBRE!!!"
@app.route('/')
def index():
    return "The Life Aquatic with Steve Zissou"