from datetime import datetime, timedelta
import io

class User: 
    intId :int = None
    strName : str = None
    bLoginState = False
    dtLastLoginTime = None
    intLoginSecsTotal = 0
    iDownloads :int = 0
    iUploads : int = 0
    iErrors : int = 0

    def __init__(self, intId:int , strName: str) -> None:
        self.intId = intId
        self.strName = strName

    def __str__(self) -> str:
        return f"ID: {self.intId} \n Name: {self.strName} \n Downloads: {self.iDownloads} \n Uploads: {self.iUploads} \n Errors: {self.iErrors} \n Total Login Time: {(self.intLoginSecsTotal/60):.2f} Minutes"
    
class LogLine:
    dtTimestamp : datetime = None
    intId : int = None
    strAction : str = None

    def __init__(self, timestamp : datetime , id : int , action : str) -> None:
        self.dtTimestamp = timestamp
        self.intId = id
        self.strAction = action

def find_user_by_id(id_lookup:int, userlist:list) -> int :
    
    for id, user in enumerate(userlist) :
        if user.intId == id_lookup :
            return id

def process_line(logline : str) :
    listLineBuffer = logline.split(" ")

    llCurrent = LogLine(datetime.strptime(listLineBuffer[0]+" "+listLineBuffer[1], "[%d.%m.%Y %H:%M:%S]"),int(listLineBuffer[3]),listLineBuffer[4].split(".")[0])

    intUserId = find_user_by_id(llCurrent.intId+1, listUsers)
    curUser = listUsers[intUserId]

    match llCurrent.strAction :
        case "LOGIN" :
            if curUser.bLoginState != False :
                curUser.iErrors+=1
            else :
                curUser.bLoginState = True
                curUser.dtLastLoginTime = llCurrent.dtTimestamp
        case "LOGOUT" :
            if curUser.bLoginState != True :
                curUser.iErrors+=1
            else :
                curUser.bLoginState = False
                intTimeDiff = (llCurrent.dtTimestamp - curUser.dtLastLoginTime).seconds
                curUser.intLoginSecsTotal += intTimeDiff
        case "DOWNLOAD" :
            if curUser.bLoginState != True :
                curUser.iErrors+=1
            else :
                curUser.iDownloads+=1
        case "UPLOAD" :
            if curUser.bLoginState != True :
                curUser.iErrors+=1
            else :
                curUser.iUploads+=1
    
listUsers : list[User] = []

fileUsers = io.open(r"C:\Users\cdirks\Documents\Python\Exercise Log\users.txt")

for line in fileUsers :
    strBuffer = line.strip().split(" ") 

    listUsers.append(User(int(strBuffer[0]),strBuffer[1]))

fileUsers.close()

fileLog = io.open(r"C:\Users\cdirks\Documents\Python\Exercise Log\log.txt")
listLog = []

for line in fileLog :
    listLog.append(line)

fileLog.close()

for line in listLog :
    process_line(line)

for user in listUsers :
    print(user)