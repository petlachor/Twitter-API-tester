import tweepy

print("*** Twitter API tester ***")

while True:
	try:
		print("Please enter the Consumer Key")
		CK = input(">>")
		if CK == "exit":
			break
			sys.exit()
		print("Please enter the Consumer Secret")
		CS = input(">>")
		if CS == "exit":
			break
			sys.exit()
		print("Please enter the Access Token")
		AT = input(">>")
		if AT == "exit":
			break
			sys.exit()
		print("Please enter the Access Secret")
		AS = input(">>")
		if AS == "exit":
			break
			sys.exit()

		auth = tweepy.OAuthHandler(CK, CS)
		auth.set_access_token(AT, AS)
		api = tweepy.API(auth)

		print("Please enter the content to tweet")
		tweet = input(">>")
		api.update_status(tweet)
		
	except:
		print("An error has occurred! Please try again.")
		print("Tip: Type [exit] to exit the program.")
		
	else:
		break
