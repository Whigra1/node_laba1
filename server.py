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
        print(payload)
    except Exception as e:        
        print(e)

    return "Ok!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4567)
    