# ipchecker

The ipchecker is a tool to track floating ips of machines. The software is composed of the following parts:

- server: `server.py` is a simple web server supported by `web.py`. It should be run on a secured machine with accessable and stable address.

- client: `client.py` is run on the machines with floating ips which will continuously send posts with information about the machine's ip to the server. The configuration about the server is set in `config.json`.

- hostmaintainer: `hostmaintainer.py` is run on personal computer where you want to easily access client machines. It should update host file according to server in a setup timeout. Need sudo to execute.

For now there are 3 fields of internet informations that server keeps for each machine:

- `ip`: the auto selected ip from ifconfig
- `ipo`: outer ip got from [www.baidu.com/s?wd=ip](http://www.baidu.com/s?wd=ip)
- `ifconfig`: whole ifconfig output

Some features are to be added to this software, including:

- Automatic launch of clients on portable machines.

- change log of ip of each machine

- Security issues.

___Warning: For now the software is just a prototype without any security measure. Use it at your own risk!___
