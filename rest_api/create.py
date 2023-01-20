import requests

requests.post('http://127.0.0.1:5000/cars', json={ "id": 5, "manufacturer": "LADA", "model": "Vesta Cross", "price": 800000, "package": "ultraluxe", "drive": "FWD", "hp": 130, "torque": 170, "color": "blue", "max_wheel_radius": 16, "chasis_type": "universal"})