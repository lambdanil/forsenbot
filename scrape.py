#!/usr/bin/python
import praw
from praw.models import Comment
# Reddit login/app info
userAgent = ''
cID = ''
cSC= ''
userN = ''
userP =''
reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)

scraped = []

# Output file for comments
save = open("comments", "a")
quotes = open("quotes","a")

subreddit = reddit.subreddit("forsen")
i = 0
for comment in subreddit.stream.comments():
    # Make sure comment is not empty (probably unnecessary)
    if not (comment.body.strip()) == "" or (comment.body.strip()) == "  " or (comment.body.strip()) == " ":
        if comment.author.name.lower() == "forsenbot":
            quotes.write(str(comment.body+";++;++;++;"))
        # Output comments to file
        commentn = str(comment.body.replace("\n",""))
        save.write(str(commentn+"\n"))
        i += 1
        print(i)
