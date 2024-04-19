from flask import Flask, request, redirect, render_template
import docker

app = Flask(__name__)
client = docker.from_env()

ip = None  # Define ip and port globally
port = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connect', methods=['POST'])
def connect():
    global ip, port  # Access the global variables
    ip = request.form['ip']
    port = request.form['port']
    # Start the OpenVPN container using Docker SDK
    container = client.containers.run('openvpn/openvpn-as', detach=True, name='openvpn-as', ports={'1194/udp': ('0.0.0.0', 1194)})
    # You can add more configuration options for the container here
    return redirect('/connected')

@app.route('/redirect', methods=['POST'])
def redirect_url():
    global ip, port  # Access the global variables
    url = request.form['url']
    # Redirect the user using Docker VPN
    return redirect(url)

@app.route('/connected', methods=['GET'])
def connected():
    return render_template('connected.html')

if __name__ == '__main__':
    app.run(debug=True)
