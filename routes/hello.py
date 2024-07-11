from flask_restful import Resource
from flask import request, jsonify

class Hello(Resource):
    def get(self):
        visitor_name = request.args.get('visitor_name', 'Visitor')
        client_ip = request.remote_addr
        
        # For demonstration, use a static city and temperature.
        # Ideally, you would use a service to determine the location based on the IP and get the temperature.
        city = "New York"
        temperature = 11  # Static temperature for demonstration

        response = {
            "client_ip": client_ip,
            "location": city,
            "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"
        }
        return jsonify(response)
