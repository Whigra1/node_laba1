from flask import Flask, request, abort
from json import loads
from telegram_bot import bot
import csvhandler
app = Flask(__name__)


@app.route("/", methods=['POST'])
def index():
    ids = csvhandler.read()
    data = ""
    [bot.send_message(int(chat_id),"File was comitted") for chat_id in ids]
    try:
        payload = loads(request.data)
        for commit_num, data_dict in enumerate(payload['commits']):
            data += f"Commit{commit_num + 1}\n"
            data += "Login: " + payload['pusher']['name'] + '\n'
            data += "Message: " + data_dict['message'] +"\n"
            data += "Timestamp: " + data_dict['timestamp'] + '\n'
            data += "Modified files: " + str(data_dict['modified']) + '\n'
            data += "Added files: " + str(data_dict['added'])+ '\n'
            data += "Removed files: " + str(data_dict['removed'])+ '\n'
            data += "-" * 25 + '\n'
            [bot.send_message(int(chat_id), data) for chat_id in ids]
    except Exception as e:        
        [bot.send_message(int(chat_id),"Can't get data.") for chat_id in ids]
        print(e)
    return "Ok!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4567)
    