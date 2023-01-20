import requests


def create_data(id, manufacturer, model, price, package, drive, hp, torque, color, max_wheel_radius, chasis_type):
    return {
    'id': id, 
    'manufacturer': manufacturer, 
    'model': model, 
    'price': price, 
    'package': package,
    'drive': drive,
    'hp': hp,
    'torque': torque,
    'color': color,
    'max_wheel_radius': max_wheel_radius,
    'chasis_type': chasis_type
}


requests.post('http://127.0.0.1:5000/cars', json=create_data(
    1, 'LADA', 'Vesta', 800000, 'ultraluxe', 'FWD', 110, 170, 'grey', 16, 'sedan'
))
requests.post('http://127.0.0.1:5000/cars', json=create_data(
    2, 'LADA', 'Vesta', 800000, 'ultraluxe', 'FWD', 110, 170, 'grey', 16, 'sedan'
))
requests.post('http://127.0.0.1:5000/cars', json=create_data(
    3, 'LADA', 'Vesta', 800000, 'ultraluxe', 'FWD', 110, 170, 'grey', 16, 'sedan'
))
requests.post('http://127.0.0.1:5000/cars', json=create_data(
    4, 'LADA', 'Vesta', 800000, 'ultraluxe', 'FWD', 110, 170, 'grey', 16, 'sedan'
))
requests.patch('http://127.0.0.1:5000/cars/4', json=create_data(
    4, 'BMW', 'G30530i', 2000000, 'ultraluxe', 'RWD', 230, 240, 'grey', 16, 'sedan'
))
