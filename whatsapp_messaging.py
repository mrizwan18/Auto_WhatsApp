import praw
from twilio.rest import Client

reddit = praw.Reddit(client_id='NI8XvqPAjb31Zw', client_secret='-cBaigpGIUOGmoSFcq6CfEQsWsU', user_agent='AutoWhatsapp')
posts = {}
subreddits = ['oddlysatisfying', 'dankmemes', 'PewdiepieSubmissions', 'wholesomememes', 'madlads']


def scrap_reddit():
    for subreddit in subreddits:
        hot_posts = reddit.subreddit(subreddit).hot(limit=1)
        for post in hot_posts:
            posts[subreddit] = post.url


def send_message(event=None, context=None):
    try:
        scrap_reddit()
    except:
        print("Something went wrong")
    # sid and auth token from twilio
    twilio_sid = 'AC91e2e304f48902f052e47d23a5ee894b'
    auth_token = '13bc910c663fff31ec20b3bd28ad5bd9'
    try:
        whatsapp_client = Client(twilio_sid, auth_token)
    except:
        print("Something went wrong")

    # Contact list to send messages to
    contact_directory = {'Hamza Anjum': '+923206080396'}

    for key, value in contact_directory.items():
        for name, post in posts.items():
            try:
                message = whatsapp_client.messages.create(
                    body='Top Post from *' + name + '* ' + post + '!',
                    from_='whatsapp:+14155238886',
                    to='whatsapp:' + value,
                )
                print(message.body)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    send_message()
