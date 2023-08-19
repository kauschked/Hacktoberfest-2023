## Lokal docker Pixelflut

To set up a local Pixelflut server for testing use this `docker-compose.yaml` file.
The only __requirement__ is a functional installation of docker and docker-compose or another OCI / docker-compose compatible software.

Be warned that this will take some performance on you machine.

## Setup

To start the stack simply execute `docker-compose up -d` or `podman-compose up -d` at this folder.
Confirm the running container afterward with `docker ps` or `podman ps`.

## Usage

When started the canvas can be viewed by any [VNC viewer](https://www.realvnc.com/de/connect/download/viewer/) software by connecting to `localhost:5900`.

Or you use the included HTML5 VNC viewer under http://localhost:8088 (Warning, there is a long delay)
