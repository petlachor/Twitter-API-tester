import tweepy

print("*** Twitter API tester ***")

print("Please enter the Consumer Key")
CK = input("CK >>")
print("Please enter the Consumer Secret")
CS = input("CS >>")
print("Please enter the Access Token")
AT = input("AT >>")
print("Please enter the Access Secret")
AS = input("AS >>")

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

print("Please enter the content to tweet")
tweet = input("Tweet >>")
api.update_status(tweet)
