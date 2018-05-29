# KHAL | REMOVE | 2.0

## Prerequisites
The following software packages are required to build and run the khal-remove virtual machine:
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* For development, it's also recommended to install the [rsync](https://rsync.samba.org/) tool (installed by default on most \*NIX systems)

## Running the VM (development mode)
The easiest way to install and run _KHAL | REMOVE_ for local development is to build a VM (Virtual Machine) image using Vagrant and VirtualBox:
* In a terminal window, cd to the khal-remove project root and run ```vagrant up```.
* To have the project files automatically synced with the VM (convenient when developing), run ```vagrant rsync-auto``` in the project root (preferably from a separate terminal window).
* SSH to the VM by running ```vagrant ssh```.
* In the VM, run ```cd /workspace/app```, then ```./run``` to start the web server.
* Head to http://192.168.50.42:8000 to use the application.

## Dependencies
All software packages dependent on by _KHAL | REMOVE_ are automatically installed during the VM setup (see Prerequsites and [vm_setup.sh](config/vm_setup.sh)). More information about individual applications and libraries can be found here:
* [Python 3](https://www.python.org/)
* [SoX](http://sox.sourceforge.net/Main/HomePage)
* [pysox](https://github.com/rabitt/pysox)
* [Flask](http://flask.pocoo.org/)
* [Celery](http://www.celeryproject.org/)
* [Redis](https://redis.io/)
* [Gunicorn](http://gunicorn.org/)
* [jQuery](https://jquery.com/)

The Virtual Machine version of _KHAL | REMOVE_ is based on the [https://www.debian.org/](Debian) GNU/Linux distribution.
