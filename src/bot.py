import twitter
from decouple import config


def main():
    api = twitter.Api(consumer_key=config('CONSUMER_KEY'),
                      consumer_secret=config('CONSUMER_SECRET'),
                      access_token_key=config('ACCESS_TOKEN'),
                      access_token_secret=config('ACCESS_TOKEN_SECRET'))

    hashtag = config('HASHTAG', 'wesmart') # The hashtag to search for in tweets
    status = config('STATUS_MSG') # The message content on the bot's reply
    img_link = config('IMG_LINK') # Must be a direct URL to an image

    tweets = api.GetSearch(raw_query='l=&q=%23{}'.format(hashtag))

    if tweets:
        target = tweets[0]

        params = {
            'status': status,
            'in_reply_to_status_id': target.id,
            'auto_populate_reply_metadata': True,
            'media': img_link
        }
        status = api.PostUpdate(**params)


if __name__ == "__main__":
    main()
