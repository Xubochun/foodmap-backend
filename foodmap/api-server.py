from flask import Flask
from flask_restful import Api, Resource

# create flask app object
app = Flask(__name__)
api = Api(app)

# create output data
output = [
    {
        "pid": "1",
        "title": "Example01",
        "price": 10,
        "img": "https://picsum.photos/id/999/1200/600",
        "isAvailable": True
    },
    {
        "id": "2",
        "title": "Example02",
        "price": 60,
        "img": "https://picsum.photos/id/1070/1200/600",
        "isAvailable": True
    }
]

@app.route("/")
def hello():
    return "<h1>Hello, this a restful api server by Flask...</h1>"


class Products(Resource):
    def get(self):
        return {"products": {"Message": "Get all products..", "output": output}}, 200

    def post(self):
        return "OK"

    def delete(self):
        return "delete"

api.add_resource(Products, '/products')

# # 建立products路由，回傳 output，及狀態 200
# @app.route("/products")
# def products():
#     return {"products": {"Message": "Get all products..", "output": output}}, 200
#

if __name__ == '__main__':
# Port 監聽 8080 並啟動除錯模式
    app.run(port=8080, debug=True)
