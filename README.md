apay
====
A revolutionary (old-school) way to pay. No NFC, no internet, just good old fashioned mics & speakers.

## Tested On 
- GNURadio 3.8.2
- Python 3.9.1 (>3.8)
- Windows & Linux

## Project Layout
`apay.grc` : GNURadio byte encoding & decoding using BPSK or QPSK

`IGnuRadio.py` : Generate random bytestream to send to ZMQ socket.

`ZmqByteSource.py` : "Embedded Python Block" for GNURadio - to parse bytes from ZMQ into a stream that GNU radio can interpret.

`ZmqConsumerDebug.py` : A ZMQ sink in GNURadio to recieve bytes for decoding.
