# lazyme

It's a simple remote control application which allows you to change sound volume and turn off your device.

The current version supports GNU/Linux backend only.

You can use any device to
- Change sound volume from 0 to 100% with 5% precision
- Set 30 min shutdown timer
- Cancel shutdown
- Shut down the remote host immediately

![UI](/ui.png?raw=true)

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
## UI

- Tap the red button to set shutdown timer to 30 minutes
- Tap one more time to cancel shudown
- Press and hold the red button for 5 seconds to shut down your remote host immediately
- Use slider to change sound volume
