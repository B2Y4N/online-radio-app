# Online Radio App
Final Year Project for "Online Radio App Using Socket Programming"

A simple WebRTC video and audio radio room with signaling server made using Python's Flask framework.

Create and join radio rooms. The users get connected directly to each other in a peer to peer mesh network using WebRTC. They share their audio and video directly with each other without going through a centralized server. However, a centralized server is needed to initiate the connections at first using a process called signaling. This, signaling server is made using Flask in Python and data is shared between server and clients using SocketIO.

## Installation
To run this on your machine, install the following:
#### Requirements:
* python 3.x
* Flask
* Flask-SocketIO
* eventlet (for websocket support while using SocketIO)

Install requirements using pip:
```
pip install Flask Flask-SocketIO eventlet
```

To setup the database:
```
python database.py
```

To start a server on localhost:
```
python app.py
```
