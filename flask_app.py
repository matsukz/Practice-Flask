#Flask main Module
from flask import Flask, redirect ,render_template
app = Flask(__name__)
app.debug = True

# Flask Get IP Addr
from flask import request

# User Addr
import datetime
import codecs

AccessCount = 0
BlankError = ""

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
        now = now,
        youbi = youbilist[now.weekday()],
        noon = noon,
        hour = hour
    )

@app.route("/task", methods=["GET","POST"])
def task():

    global BlankError

    KamokuList = []
    Kamokutxt = codecs.open("EtcTxt\\kamoku.txt","r","utf-8")
    for item in Kamokutxt.readlines():
        KamokuList.append(item.rstrip())

    file = codecs.open("EtcTxt\\task.txt","r","utf-8")
    lines = file.readlines()
    file.close()

    if request.method == "POST":
        date = request.form["Date"]
        Kamoku = request.form["Kamoku"]
        Naiyou = request.form["Naiyou"]

        if date != "" or Naiyou != "":
            
            file = codecs.open("EtcTxt\\task.txt","a","utf-8")
            file.write(date + "," + Kamoku + "," + Naiyou + "\n")
            file.close()
            BlankError = ""
        else:
            BlankError = "空欄があります"

        return redirect("/task")

    else:
        pass

    return render_template(
        "task.html",
        title = "タスク",
        KamokuList = KamokuList,
        lines = lines,
        BlankError = BlankError
    )
