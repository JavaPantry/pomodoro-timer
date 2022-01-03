def calcPercentage(total, part):
    percent = 0.0
    if(total != 0 ):
        percent = (part * 100.0) / total
    # percent = 100 - percent
    return "{:10.2f}".format(percent)

def convertSec(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    # return str(hours) + ":" + str(mins) + ":" + str(sec)
    return "{0:02}:{1:02}:{2:02}".format(int(hours),int(mins),int(sec))
