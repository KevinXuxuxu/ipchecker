# ipchecker

The ipchecker is a tool to track floating ips of machines. The software is composed of two parts:

- server: `server.py` is a simple web server supported by `web.py`. It should be run on a secured machine with accessable and stable address.

- client: `client.py` is run on the machines with floating ips which will continuously send posts with information about the machine's ip to the server. The configuration about the server is set in `config.json`.

Some features are to be added to this software, including

- Automatic launch of clients on portable machines.

- Maintainer of host file which should update host file according to server.

- Security issues.

___Warning: For now the software is just a prototype without any security measure. Use it at your own risk!___