# Docker VPN with Flask

## Overview

This project demonstrates how to set up a Docker VPN using OpenVPN and Flask. It allows users to connect to a VPN server through a web interface and browse the internet anonymously.

## Prerequisites

Before running this project, make sure you have the following installed:

- Docker: [Installation Guide](https://docs.docker.com/get-docker/)
- Python 3.x: [Installation Guide](https://www.python.org/downloads/)

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/docker-vpn-flask.git
Navigate to the project directory:
bash
Copy code
cd docker-vpn-flask
Set up a virtual environment (optional but recommended):
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install the required Python packages:
bash
Copy code
pip install -r requirements.txt
Start the Flask server:
bash
Copy code
python main.py
Open your web browser and go to http://127.0.0.1:5000/ to access the VPN interface.
Usage
Enter the IP address and port of the VPN server in the form on the homepage and click "Connect" to start the VPN container.
Once connected, navigate to http://127.0.0.1:5000/connected to access the connected interface.
Use the search bar to enter a URL and browse the web anonymously through the VPN.
Contributing
Contributions are welcome! Please fork this repository and create a pull request with your changes.

License
This project is licensed under the MIT License.

Acknowledgements
Flask - Web framework for Python
Docker - Containerization platform
OpenVPN - VPN software
