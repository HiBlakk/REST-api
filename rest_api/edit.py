import requests

requests.patch('http://127.0.0.1:5000/cars/5', json={ "id": 5, "manufacturer": "LADA", "model": "Vesta Super", "price": 80000, "package": "ultraluxe", "drive": "FWD", "hp": 110, "torque": 170, "color": "grey", "max_wheel_radius": 16, "chasis_type": "universal"})