# One Time Pad

This is a script that can be used to generate a random one time pad, encode the message, and encrypt the message. It can also be used to decode and decrypt the message.

For encoding and decoding, it makes use of a code book to shorten the message.

It's not intended to be used over the internet, just as an aid if one wants to create a one time pad using open source code.


## Setup

```
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```
