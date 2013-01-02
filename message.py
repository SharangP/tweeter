# direct message test
# pass authentication info in via command line

import sys
import time
import tweepy

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key=""
consumer_secret=""

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token=""
access_token_secret=""

if len(sys.argv) == 5:

    consumer_key = sys.argv[1]
    consumer_secret = sys.argv[2]
    access_token = sys.argv[3]
    access_token_secret = sys.argv[4]
#    if len(sys.argv) > 3:
#        if sys.argv[3] == 'R':
#            remove = True

#    if not os.path.isdir(rootMusicPath):
#        sys.exit("Incorrect root music directory")
#    else:
#        if not rootMusicPath.endswith('/'):
#            rootMusicPath += '/'
#
#    if not os.path.isdir(newMusicPath):
#        sys.exit("Incorrect new music directory")
#    else:
#        if not newMusicPath.endswith('/'):
#            newMusicPath += '/'
else:
    sys.exit("Error: not enough arguments")

print consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print api.me().name

# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
#api.update_status('Updating via Tweepy! @samthebrownman @csherland')

api.send_direct_message(screen_name = '@samthebrownman', text = 'Prepare.')

time.sleep(10)

i = 0

for tweet in tweepy.Cursor(api.search,
        q = "#tool",
        rpp=100,
        result_type="recent",
        include_entities=True,
        lang="en").items():
    if ++i > 100:
        break
    api.send_direct_message(screen_name = '@samthebrownman',text = tweet.text)
    print tweet.text
    time.sleep(2)

api.send_direct_message(screen_name = '@samthebrownman', text = 'I hope I dont get banned.')
