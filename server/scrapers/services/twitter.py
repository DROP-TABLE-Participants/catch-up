from datetime import datetime, timedelta
from scrapers.client import client
from scrapers.models import Comment
from products.models import Product

from .sentiment import get_sentiment


def run_scraper(id_: int, serialized_name: str, type: str):
    run_input = {
        "searchTerms": [
            serialized_name
        ],
        "maxItems": 500,
        "sort": "Top",
        "tweetLanguage": "en",
        "minimumFavorites": 5,
    }

    current_date = datetime.now()

    if type == "daily":
        run_input["start"] = (current_date - timedelta(days=1)).strftime("%Y-%m-%d")
        run_input["end"] = current_date.strftime("%Y-%m-%d")
    else:
        run_input["start"] = (current_date - timedelta(weeks=1)).strftime("%Y-%m-%d")
        run_input["end"] = current_date.strftime("%Y-%m-%d")

    run = client.actor("apidojo/tweet-scraper").call(run_input=run_input)

    value = 0
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        if item["likeCount"] < 1:
            break

        product = Product.objects.get(id=id_)
        sentiment = get_sentiment(item["text"])

        comment = Comment(
            text_value=item["text"],
            product=product,
            value=sentiment,
            weight=item["likeCount"],
            weighted_value=sentiment
        )

        Comment.save(comment)

        value += sentiment

    return value