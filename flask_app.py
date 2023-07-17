#Flask main Module
from flask import Flask, render_template
app = Flask(__name__)

# Flask Get IP Addr
from flask import request

# User Addr
import datetime

AccessCount = 0

@app.route("/")
def route():

    global AccessCount

    now = datetime.datetime.now()

    if now.hour < 4:
        Aisatsu = "こんばんは"
    elif now.hour < 9:
        Aisatsu = "おはようございます"
    elif now.hour < 18:
        Aisatsu = "こんにちは"
    else:
        Aisatsu = "こんばんは"

    AccessCount = AccessCount + 1

    return render_template(
                        "index.html",
                        title = "ようこそ",
                        Aisatsu = Aisatsu,
                        UserIP = request.environ.get('HTTP_X_REAL_IP', request.remote_addr),
                        AccessCount = AccessCount
    )

@app.route("/time")
def comment():
    now = datetime.datetime.now()

    # 曜日出力
    youbilist = ["（月）","（火）","（水）","（木）","（金）","（土）","（日）"]

    # 時間計算
    if now.hour < 12:
        noon = "午前"
        hour = now.hour
    elif now.hour == 12:
        noon = "正午"
        hour = now.hour
    else:
        noon = "午後"
        hour = now.hour - 12

    return render_template(
        "time.html",
        title = "現在の時間は？",
        toshi = now.year - 2018,
        month = now.month,
        day = now.day,
        youbi = youbilist[now.weekday()],
        noon = noon,
        hour = hour,
        hour_ex = now.hour,
        min = now.minute
    )



