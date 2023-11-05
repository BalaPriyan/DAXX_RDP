import os

import time

import json

from pyngrok import ngrok

NGROK_APIKEY = os.environ.get("NGROK_APIKEY", "2XkAUddYPQojhFIQx7y3Cm1uVcm_49ixL3maCmU81X9v5ks9V")

ngrok.set_auth_token(NGROK_APIKEY)

uri=ngrok.connect(5900, "tcp")

open("/railway/noVNC/ngrok.txt", "w").write(uri.public_url)

open("/railway/noVNC/ngrok.json", "w").write(json.dumps(uri.data))

while True:

    time.sleep(60*60*24)
