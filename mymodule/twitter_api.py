import tweepy
import json

def json_reader(user_dict):
	'''
	(dict) ->
	This functions prints certain inf from users dict, which was
	formed from json.
	'''
	print("List of accessible information \n\n <><><><><><><><><>")
	for inf in ['id', 'id_str', 'name', 'screen_name', 'location',
				'profile_location', 'description', 'url', 'entities',
				'protected', 'followers_count', 'friends_count',
				'listed_count', 'created_at', 'favourites_count',
				'utc_offset', 'time_zone', 'geo_enabled',
				'verified', 'statuses_count', 'lang', 'status',
				'contributors_enabled', 'is_translator',
				'is_translation_enabled', 'profile_background_color',
				'profile_background_image_url',
				'profile_background_image_url_https',
				'profile_background_tile', 'profile_image_url',
				'profile_image_url_https', 'profile_banner_url',
				'profile_link_color', 'profile_sidebar_border_color',
				'profile_sidebar_fill_color', 'profile_text_color',
				'profile_use_background_image', 'has_extended_profile',
				'default_profile', 'default_profile_image',
				'following', 'follow_request_sent', 'notifications',
				'translator_type']:
		print(inf, "\n"*2)
	print('<><><><><><><><><>' + "\n")
	key = input("Enter The Information You Need: ")
	print(user[key])


if __name__ == "__main__":
	consumer_key = '0PlKlKMbNYWL9UeVuC6DPxX4B'
	consumer_secret = "dpvpCGjA9udpjsPkCVfdxZhmAOLMXFeZcZEVLbH3usRiv8fHfN"
	access_token = "963011359737774080-mYiiiIGOarKbuYGVdVTJBPcYC39RkqC"
	access_token_secret = "f8031GVQo6dJXX35RRVbDlGxMcitrAt7uyAUVgKuO1E0R"
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
	# acc is the name of twitter account
	acc =""
	while len(acc) < 1:
		acc = input("Enter Twitter Account:")
	user = api.get_user(screen_name=acc, count=100)
	json_reader(user)

