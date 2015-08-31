import praw, pprint, re
subDict = {
    }
user_agent = "Gilda" ##input("Please input your desired user agent to display to reddit: ")
r = praw.Reddit(user_agent=user_agent)
nsfwCheck = input("Allow NSFW subs to be displayed?(True or False): ")
subreddit = r.get_random_subreddit(nsfw=nsfwCheck)
pprint.pprint(subreddit)
##pls = pprint.pprint(subreddit)
##f = open('SOTD.txt','a')
##f.write(pls)
##f.close()
