import praw
from os.path import isfile
import praw,requests,re
from time import sleep
import array


reddit = praw.Reddit(client_id='#input your bot client id',
                     client_secret='#input your bot client secret',
                     user_agent='#input the name of your bot name')

posts = []

nons = []


for submission in reddit.subreddit('dogpictures').hot(limit=500):
    posts.append(submission)

for idx, post in enumerate(posts):
    if(not post.is_reddit_media_domain):
        nons.append(post)
        print('non ' + str(idx))

for non in nons:
    posts.remove(non)


urls = []
filenames = []

for idx, post in enumerate(posts):
    url = (post.url)
    file_name = url.split("/")
    if len(file_name) == 0:
        file_name = re.findall("/(.*?)", url)
    file_name = file_name[-1]
    if "." not in file_name:
        file_name += ".jpg"
    filenames.append(file_name + ".jpg")
    urls.append(url)
    print(file_name)

for idx, filenames in enumerate(filenames, start=0):
    r = requests.get(urls[idx])
    with open("#directory for the output images" + str(idx) + ".jpg","wb") as f:
        f.write(r.content)
