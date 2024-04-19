# Docker VPN with Flask

## Overview

This project is a comprehensive guide and implementation for setting up a Docker-based Virtual Private Network (VPN) using OpenVPN and Flask, enabling users to connect to a VPN server through a user-friendly web interface and browse the internet anonymously. It leverages OpenVPN for secure communication, Flask for web interface development, and Docker for streamlined deployment and management. Users can clone the repository, set up dependencies including Docker and Python 3.x, start the Flask server to access the VPN interface, enter the VPN server's IP address and port, establish a connection, and then browse the web anonymously through the VPN, enhancing their online privacy and security significantly.
## Prerequisites

Before running this project, make sure you have the following installed:

- Docker: [Installation Guide](https://docs.docker.com/get-docker/)
- Python 3.x: [Installation Guide](https://www.python.org/downloads/)

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/docker-vpn-flask.git
# Navigate to the project directory:
    ``` bash
      cd docker-vpn-flask
# Set up a virtual environment (optional but recommended):
    ``` bash
      python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
# Install the required Python packages:
    ``` bash
      pip install -r requirements.txt
# Start the Flask server:
    ``` bash
      python main.py
Open your web browser and go to http://127.0.0.1:5000/ to access the VPN interface.
# Usage
Enter the IP address and port of the VPN server in the form on the homepage and click "Connect" to start the VPN container.
Once connected, navigate to http://127.0.0.1:5000/connected to access the connected interface.
Use the search bar to enter a URL and browse the web anonymously through the VPN.
# Contributing
Contributions are welcome! Please fork this repository and create a pull request with your changes.

# License
This project is licensed under the MIT License.
# Acknowledgements
Flask - Web framework for Python
Docker - Containerization platform
OpenVPN - VPN software
