import praw
import pprint

user_agent = "Karma_Grabber_Test v1 by /u/Gilda_Griffon"
r = praw.Reddit(user_agent=user_agent)
user = input("Enter the user you wish to view a karma breakdown of: ")
user = r.get_redditor(user)

thing_limit = 10
gen = user.get_submitted(limit=thing_limit)

karma_by_subreddit = {}
for thing in gen:
    subreddit = thing.subreddit.display_name
    karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0)
                                     + thing.score)

pprint.pprint(karma_by_subreddit)

