# Flask RESTful API Example

This project is a simple Flask web server that exposes a RESTful API endpoint. It responds with a JSON object containing the client's IP address, a static location (New York), and a greeting message that includes the temperature.

## Task Description

Set up a basic web server in your preferred stack. Deploy it to any free hosting platform and expose an API endpoint that conforms to the criteria below:

### Endpoint

GET [Endpoint](https://flask-api-project-seven.vercel.app/api/hello?visitor_name=Mark)

### Response

```json
{
  "client_ip": "127.0.0.1",
  "location": "New York",
  "greeting": "Hello, Mark!, the temperature is 11 degrees Celsius in New York"
}
```

## How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/sbendavid/flask-api-project.git
cd flask-api-project
```

2. Install dependencies:

```bash
pip install Flask Flask-RESTful requests
```

3. Run the Flask application:

```bash
python app.py
```

4. Access the API:
   Open your web browser or use a tool like curl or Postman to access the following URL:
   [Endpoint](https://flask-api-project-seven.vercel.app/api/hello?visitor_name=Mark)
