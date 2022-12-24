import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

#Ex https://123njjakhar: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@github.com/Itz-zaid/anything
os.system("git clone https://123njjakhar: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@github.com/123njjakhar/moge2 ok && cd ok && pip3 install -U -r requirements.txt && nohup python3 -m RomeoBot &")
