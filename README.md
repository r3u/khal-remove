# KHAL | REMOVE | 2.0

## Prerequisites
The following software packages are required to run the khal-remove virtual machine:
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* For development, it's recommended to also install the rsync tool (installed by default on most \*NIX systems)

## Running the VM (development mode)
* In a terminal window, cd to the khal-remove project root and run ```vagrant up```.
* To have the project files automatically synced with the VM (convenience when developing), run ```vagrant vagrant rsync-auto``` in the project root (from a separate terminal window).
* SSH to the VM by running ```vagrant ssh```.
* In the VM, run ```cd /workspace/webapp```, then ```./run``` to start the web server.
* Head to http://192.168.50.42:8000 to use the application.

## Appendix
### Useful sox commands

sox infile outfile reverse

sox hunter.mp3 hunter-L.wav remix 1
sox hunter.mp3 hunter-R.wav remix 2
