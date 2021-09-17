#!/usr/bin/python
import praw
import random
import os
import time
import re
from praw.models import Comment
# Reddit login/app info
userAgent = ''
cID = ''
cSC= ''
userN = ''
userP =''
reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)

# Words the bot replies to
bot_calls = ["markovbaj", "mr fors", "bot", "xqcl", "e-aeolian"]
banned = ["hitler", "heil","u/donuts4thewin","meme11211"]
emotes = ["pepeLaugh", "OMEGALUL", "OMEGALULiguess", "Copesen", "amongE", ':tf:', "PagMan", "MEGALUL", "gachiHYPER", "monkaOMEGA", "forsenInsane", "Clueless", "monkaLaugh", "forsenDespair", "TrollDespair", "FeelsStrongMan", "gachiAPPROVE", "ZULUL", "LULW", "LULE"]
used = []

usedfile = open("used","a")

# Main loop
subreddit = reddit.subreddit("forsen")
for comment in subreddit.stream.comments():
    # Dictionary file
    dictfix = open("dict","r")
    line = dictfix.readline()
    newline = ""
    while True:
        newline += line
        line = dictfix.readline()
        if not line:
            break
    # Put comments into a list
    bot_quotes = list(newline.split(";++;++;++;"))
    quotefile = open("quotes","r")
    quotefile.readline()
    qline = quotefile.readline()
    qnewline = ""
    while qline != "":
        qline = quotefile.readline()
        qnewline = qnewline+qline
    # Put comments into a list
    quotes = list(qnewline.split(";++;++;++;"))
    cuotefile = open("comments","r")
    cline = cuotefile.readline()
    cnewline = ""
    clines = []
    while True:
        cline = cuotefile.readline()
        if not cline:
            break
        while "\n" in cline:
            cline = cline.replace("\n","")
        clines.append(cline)
    while '' in clines:
        clines.remove('')
    while ' ' in clines:
        clines.remove(' ')
    while '  ' in clines:
        clines.remove('  ')
    
    # If comments is saved, it has already been replied to
    if not comment.saved and comment.author.name != userN and comment.author.name != "YEPCOCKroach" and comment.author.name != "qrado":
        reply_set = 0
        called = 0
        # Checks if bot was called
        for call in bot_calls:
            if (call in comment.body.lower()):
                bot_reply = random.choice(bot_quotes)
#                # Prevents recursion
#                while re.compile('|'.join(banned),re.IGNORECASE).search(bot_reply.lower()):
#                    bot_reply = random.choice(bot_quotes)
#                    time.sleep(0.1)
                called = 1
                if call == bot_calls[-1]:
                    break
        if called == 0:
            if random.randint(1,100) == 1:
                called = 1
            for emote in emotes:
                if emote.lower() in comment.body.lower() and random.randint(1,25) == 1:
                    bot_reply = emote
                    reply_set = 1
                    called = 1
                    break
        # Reply to the post (only if the bot was called) 
        if called == 1 and reply_set == 0:
            search = "NULL"
            bot_reply = "NULL"
            splitlist = comment.body.split(" ")
            splitlist.reverse()
            breakdo = 0
            for word in splitlist:
                if breakdo == 1:
                    break
                if word == splitlist[-1]:
                    breakdo = 1
                if word == splitlist[0]:
                    continue
                word2 = splitlist[splitlist.index(word)-1]
                if reply_set == 1:
                    break
                for emote in emotes:
                   if str(emote.lower()) in str(comment.body.lower()):
                        bot_reply = emote
                        reply_set = 1
                        break
                n = 0
                while True:
                    search = bot_quotes[n]
                    n += 1
                    if str(" "+word.lower()+" "+word2.lower()+" ") in search.lower() and search not in used:
                        bot_reply = search
                        reply_set = 1
                        used.append(bot_reply)
                        usedfile.write(bot_reply)
                        break
                    if not search:
                        break
            if bot_reply == "NULL":
                if (random.randint(1,75)) == 1:
                   bot_reply = random.choice(quotes)
                   reply_set = 1
                else:
                   bot_reply = random.choice(clines)
                   reply_set = 1
            comment.reply(bot_reply)
            comment.save()
            print("------------vvvvvvvv")
            print(comment.body)
            print("vvvvvvvvvvvvvvvvvvvv")
            print(bot_reply)
            print("------------\nReply Sent\n------------")
            time.sleep(2)
        elif called == 1:
            comment.reply(bot_reply)
            comment.save()
            print("------------vvvvvvvv")
            print(comment.body)
            print("vvvvvvvvvvvvvvvvvvvv")
            print(bot_reply)
            print("------------\nReply Sent\n------------")
    dictfix.close()
    quotefile.close()
    cuotefile.close()
