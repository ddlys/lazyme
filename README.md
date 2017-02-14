# lazyme

It's a simple remote control application which allows you to change sound volume and turn off your device.

The current version supports GNU/Linux only.

Abilities:
- Changing sound volume from 0 to 100% with 5% precision
- Setting 30 min shutdown timer
- Cancelling shutdown

## Prerequisites

- python >= 2.7
- pactl
- any modern webkit based browser

Make sure that you have enough permissions to use /sbin/shutdown

## Usage

Clone this repo
```
git clone https://github.com/ddlys/lazyme
```

Type from the cloned directory to start server
```
./lazyme.py -i 0.0.0.0 -p 12345
```

Connect to the server

```
http://localhost:12345
```

