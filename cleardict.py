dictfix = open("dict","r")
line = dictfix.readline()
newline = ""
while True:
    line = dictfix.readline()
    if not line:
        break
    else:
        newline = newline+line
# Put comments into a list
bot_quotes = list(newline.split(";++;++;++;"))
