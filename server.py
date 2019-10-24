from flask import Flask, request, abort
from json import loads
from telegram_bot import bot
import csvhandler
app = Flask(__name__)


@app.route("/", methods=['POST'])
def index():
    print("success")
    ids = csvhandler.read()
    [bot.send_message(int(chat_id),"File was comitted") for chat_id in ids]
    try:
        payload = loads(request.data)
        print(payload['pusher']['name'])
        print(payload['pusher']['message'])
        print(payload['pusher']['timestamp'])
        print(payload['pusher']['modified'])
        
    except Exception as e:        
        [bot.send_message(int(chat_id),"Can't get data.") for chat_id in ids]

    return "Ok!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4567)
    