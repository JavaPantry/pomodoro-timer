# from utils.functions import calcPercentage

def calcPercentage(total, part):
    percent = 0.0
    if(total != 0 ):
        percent = (part * 100.0) / total
    # percent = 100 - percent
    return "{:10.2f}".format(percent)


print("Hello Percentage")
print("calcPercentage(100, 10)" + calcPercentage(100., 10.) + "%")
print("calcPercentage(100, 20)" + calcPercentage(100., 20.) + "%")
print("calcPercentage(100, 50)" + calcPercentage(100., 50.) + "%")
print("calcPercentage(100, 60)" + calcPercentage(100., 60.) + "%")
print("calcPercentage(100, 70)" + calcPercentage(100., 70.) + "%")
print("calcPercentage(100, 80)" + calcPercentage(100., 80.) + "%")
print("calcPercentage(100, 90)" + calcPercentage(100., 90.) + "%")
