#!/usr/bin/python3

import praw

reddit = praw.Reddit(
    client_id='',
    client_secret='',
    user_agent='',
    username='',
    password=''
)

post_id = ''
submission = reddit.submission(id=post_id)

submission.comments.replace_more(limit=0)

test_list = ['key']

with open('test_comnt.txt', 'w', encoding='utf-8') as file:
    count = 0

    for comment in submission.comments.list():
        if any(i in comment.body.lower() for i in test_list):
            file.write(comment.body + '\n')
            count += 1
            if count >= 5:
                break

