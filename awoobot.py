import praw, time, pyimgur, random

def uploadimage():
    clientid = '' #imgur client id
    path = '' #path to file you wish to reupload
    im = pyimgur.Imgur(clientid)
    image = im.upload_image(path, title='') #title for new posts
    return image.link

def main():
    user_agent = ('Awoo 1.0') #useragent
    r = praw.Reddit(user_agent=user_agent)
    r.login('','') #reddit account login
    while True:
        try:
            rtime = random.randint(60,600) #time to wait between new posts
            url = uploadimage()
            r.submit(subreddit='',title='',url=url) #subreddit and title
            print 'Post successful. Sleeping for',rtime
            time.sleep(rtime)
        except Exception as e:
            print 'Something fucked up:',e
            time.sleep(20)

if __name__ == '__main__':
    main()
