from http import HTTPStatus
import json
from flask import jsonify, request
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS
from models import Orders, OrderView
from RabbitQueue import sendIntoQueue
from start import create_app


app = create_app()

CORS(app)
client = PyMongo(app, uri=app.config.get('DATABASE_URI'))
db = client.db

@app.route("/welcome", methods=["GET"])
def index():
    try:
        return jsonify(message="Welcome to Pizza House", status=HTTPStatus.OK)
    except:
        return jsonify(message="Some Error Occurred", status=HTTPStatus.BAD_REQUEST)
    
@app.route("/order", methods=["POST"])
def insertData():
    try:
        orders = json.loads(request.get_data().decode()).get("orders")
        new_order = Orders(order = orders)
        result = db.orders.insert_one(new_order.dict())
        return jsonify(id=str(result.inserted_id), status=HTTPStatus.CREATED)
    except:
        return jsonify(message="Some Error Occurred", status=HTTPStatus.BAD_REQUEST)
    
    
@app.route("/orderByQueue", methods=["POST"])
def insertDataIntoQueue():
    order = json.loads(request.get_data().decode()).get("orders")
    sendIntoQueue.sender(order)
    order_obj = Orders(order = order)
    response = db.orders.insert_one(order_obj.dict())
    return jsonify(id=str(response.inserted_id), status=HTTPStatus.CREATED)
    
    
@app.route("/getorders", methods=["GET"])
def getAllOrders():
    try:
        all_orders = db.orders.find()
        result = []
        for order in all_orders:
            result.append(dict(OrderView(id=str(order["_id"]), order=order["order"], orderTime=order["orderTime"])))
        return jsonify(all_orders=result, status=HTTPStatus.OK)
    except:
        return jsonify(message="Some Error Occurred", status=HTTPStatus.BAD_REQUEST)
    
    
@app.route("/getorders/<string:order_id>", methods=["GET"])
def getOrdersById(order_id):
    try:
        order = db.orders.find_one({"_id":ObjectId(order_id)})
        if len(order) > 0:
            result = dict(OrderView(id=str(order["_id"]), order=order["order"], orderTime=order["orderTime"]))
            return jsonify(order=result, status=HTTPStatus.OK)
        else:
            return jsonify(message="Result not Found", status=HTTPStatus.NOT_FOUND)
    except:
        return jsonify(message="Not a valid Id", status=HTTPStatus.BAD_REQUEST)
    

if __name__ == "__main__":
    app.run(debug=True)
