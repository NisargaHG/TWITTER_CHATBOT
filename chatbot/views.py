from django.shortcuts import render
from django.conf import settings
import tweepy

def chatbot_ui(request):
    tweets = []
    error = None

    if request.method == "POST":
        query = request.POST.get("query")

        try:
            client = tweepy.Client(
                bearer_token=settings.TWITTER_BEARER_TOKEN
            )

            response = client.search_recent_tweets(
                query=query,
                max_results=10
            )

            if response.data:
                tweets = [tweet.text for tweet in response.data]
            else:
                tweets = ["No tweets found"]

        except tweepy.TooManyRequests:
            error = "Rate limit reached. Please wait 15 minutes and try again."

        except Exception as e:
            error = str(e)

    return render(request, "chatbot/chatbot_ui.html", {
        "tweets": tweets,
        "error": error
    })
