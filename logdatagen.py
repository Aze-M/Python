from datetime import datetime as dt, timedelta as td
import random
import time
import io

def make_log_entry(user_id : int, action : str) -> str : 
    dtInsertTime = dt.now()+td(seconds=intTimeOffset)
    return f"[{dtInsertTime.strftime("%d.%m.%Y %H:%M:%S")}] ID: {user_id} {action}."

listActions = ["LOGIN", "LOGOUT", "DOWNLOAD", "UPLOAD"]

listLog = []
intTimeOffset=0

fileLog = io.open("./Exercise Log/log.txt", 'a')

while len(listLog) < 5000 :
    intCurUserID = int(random.random()*5)
    intActionID = int(random.random()*4)
    intTimeOffset+=int(random.random()*10)

    listLog.append(make_log_entry(intCurUserID,listActions[intActionID]))

for line in listLog :
    fileLog.write(line + "\n")
