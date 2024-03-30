from scrapers.models import Comment
from scrapers.client import client
from .sentiment import get_sentiment
from products.models import Product


def run_scraper(id_: int, serialized_name: str, type: str):
    run_input = {
        "debugMode": False,
        "includeNSFW": False,
        "maxComments": 21,
        "maxCommunitiesCount": 7,
        "maxItems": 1000,
        "maxPostCount": 1000,
        "maxUserCount": 0,
        "proxy": {
            "useApifyProxy": True,
            "apifyProxyGroups": [
                "RESIDENTIAL"
            ]
        },
        "scrollTimeout": 40,
        "searchComments": True,
        "searchCommunities": False,
        "searchPosts": True,
        "searchUsers": False,
        "searches": [
            serialized_name
        ],
        "skipComments": False,
        "time": "month" if type == "monthly" else "week"
    }

    run = client.actor("trudax/reddit-scraper").call(run_input=run_input)
    value = 0
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        if item["upVotes"] < 1:
            break

        product = Product.objects.get(id=id_)
        sentiment = get_sentiment(item["body"])

        comment = Comment(
            text_value=item["body"],
            product=product,
            value=sentiment,
            weight=item["upVotes"],
            weighted_value=sentiment * item["upVotes"]
        )

        Comment.save(comment)

        value += sentiment * item["upVotes"]

    return value
