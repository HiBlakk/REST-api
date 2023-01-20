from flask import Flask, abort, request
import json
import os


app = Flask(__name__)


POSSIBLE_ATTRIBUTES = {
    'id': (type(1),), 
    'manufacturer': (type('1'),), 
    'model': (type('1'),), 
    'price': (type(1.0), type(1)), 
    'package': (type('1'),),
    'drive': (type('1'),),
    'hp': (type(1), type(1.0)),
    'torque': (type(1), type(1.0)),
    'color': (type('1'),),
    'max_wheel_radius': (type(1), type(1.1)),
    'chasis_type': (type('1'),)
}


with open(os.path.dirname(__file__) + '/cars.json', 'r') as file:
    data = json.load(file)
    CARS = {int(key): value for key, value in data.items()}



def dump_data(data):
    with open(os.path.dirname(__file__) + '/cars.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def validate_car(good):
    for key, value in good.items():
        if key not in POSSIBLE_ATTRIBUTES and not isinstance(value, POSSIBLE_ATTRIBUTES.get(key)):
            return False
    return len(POSSIBLE_ATTRIBUTES) == len(good)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/cars', methods=['GET'])
def show_all():
    return CARS


@app.route('/cars/<id>', methods=['GET'])
def show_one(id):
    return CARS.get(int(id)) if int(id) in CARS else abort(404)


@app.route('/cars', methods=['POST'])
def store():
    recieved_data = request.get_json()

    if not validate_car(recieved_data):
        return 406

    if CARS.get(recieved_data['id']):
        return 409

    CARS[recieved_data['id']] = recieved_data

    dump_data(CARS)

    return CARS


def validate_modification(data):
    for key, value in data.items():
        if key not in POSSIBLE_ATTRIBUTES or not isinstance(value, POSSIBLE_ATTRIBUTES.get(key)):
            return False
    return True


@app.route('/cars/<id>', methods=['PATCH'])
def modify_car(id):
    recieved_data = request.get_json()

    if not validate_modification(recieved_data):
        return 406

    print(CARS)

    print(id, type(id), '!!!')

    CARS[int(id)] = CARS[int(recieved_data['id'])] | recieved_data

    print(CARS)

    dump_data(CARS)

    return CARS[int(id)]


@app.route('/cars/<id>', methods=['DELETE'])
def delete_car(id):
    try:
        CARS.pop(int(id))
        dump_data(CARS)
        return {'ok': 200}
    except KeyError:
        return abort(404)


def run():
    app.run(debug=True)

        
if __name__ == '__main__':
    run()
