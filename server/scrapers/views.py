from datetime import datetime

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request

from products.models import Product

from .models import History

from .services.reddit import run_scraper as run_reddit_scraper
from .services.twitter import run_scraper as run_twitter_scraper


class ScraperViewSet(ViewSet):
    def update(self, request: Request, pk=None):
        if pk is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        product = Product.objects.get(pk=pk)
        type_run = request.data.get("type")
        history_reddit = History.objects.filter(product=product, source="reddit")
        history_twitter = History.objects.filter(product=product, source="twitter")

        if not history_reddit.exists():
            reddit = run_reddit_scraper(product.id, product.serialized_name, type_run)
            history_reddit = History(
                product=product,
                value=reddit,
                source="reddit",
                date=datetime.now(),
            )
            History.save(history_reddit)
        else:
            history_reddit = history_reddit.get()

        if not history_twitter.exists():
            reddit = run_twitter_scraper(product.id, product.serialized_name, type_run)
            history_twitter = History(
                product=product,
                value=reddit,
                source="twitter",
                date=datetime.now(),
            )
            History.save(history_twitter)
        else:
            history_twitter = history_twitter.get()

        print(history_reddit.value, history_twitter.value)

        return Response((history_twitter.value + history_reddit.value) / 2)
