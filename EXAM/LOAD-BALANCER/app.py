import os
import itertools
import requests
from flask import Flask, request, Response

app = Flask(__name__)

# Load hostnames from environment variables
hosts = os.getenv("LOAD_BALANCER_HOSTS", "").split(",")

if not hosts:
    raise RuntimeError("No hosts defined in the LOAD_BALANCER_HOSTS environment variable.")

# Create a round-robin iterator
hosts_iterator = itertools.cycle(hosts)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def load_balancer(path):
    # Get the next host in the round-robin sequence
    next_host = next(hosts_iterator)
    
    # Construct the target URL
    target_url = f"http://{next_host}/{path}"
    
    # Forward the incoming request to the target host
    try:
        response = requests.request(
            method=request.method,
            url=target_url,
            headers={key: value for key, value in request.headers},
            params=request.args,
            data=request.data,
            cookies=request.cookies,
            allow_redirects=False
        )
        
        # Relay the response back to the client
        return Response(
            response.content,
            status=response.status_code,
            headers=dict(response.headers)
        )
    except requests.RequestException as e:
        return {"error": str(e)}, 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
