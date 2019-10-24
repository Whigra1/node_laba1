from flask import Flask, request, abort
from json import loads
from telegram_bot import bot
import csvhandler
app = Flask(__name__)


@app.route("/", methods=['POST'])
def index():
    print("success")
    ids = csvhandler.read()
    data = ""
    [bot.send_message(int(chat_id),"File was comitted") for chat_id in ids]
    try:
        payload = loads(request.data)
        for i in payload['commits']:
            data += f"Commit{i + 1}"
            data += "Login: " + payload['pusher']['name'] + '\n'
            data += "Message: " + payload['commits'][i]['message'] +"\n"
            data += "Timestamp: " + payload['commits'][i]['timestamp'] + '\n'
            data += "Modified files: " + str(payload['commits'][i]['modified'])
            data += "Modified files: " + str(payload['commits'][i]['added'])
            data += "Modified files: " + str(payload['commits'][i]['removed'])
            data += "-"*25
            [bot.send_message(int(chat_id), data) for chat_id in ids]
    except Exception as e:        
        [bot.send_message(int(chat_id),"Can't get data.") for chat_id in ids]

    return "Ok!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4567)
    