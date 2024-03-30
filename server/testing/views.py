from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from gpt.services.name_serializer import name_serializer

import os
from apify_client import ApifyClient
from scrapers.services.sentiment import get_sentiment

client = ApifyClient(os.getenv("APIFY_API_KEY"))


class TestViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        if pk is None or pk == "":
            return Response(status=400)

        title = name_serializer(pk)

        return Response(title)

    def create(self, request):
        title = request.data.get("title")

        if title is None or title == "":
            return Response(status=400)

        run_input = {
            "debugMode": False,
            "includeNSFW": False,
            "maxComments": 0,
            "maxCommunitiesCount": 0,
            "maxItems": 10,
            "maxPostCount": 10,
            "maxUserCount": 0,
            "proxy": {
                "useApifyProxy": True,
                "apifyProxyGroups": [
                    "RESIDENTIAL"
                ]
            },
            "scrollTimeout": 40,
            "searches": [
                title
            ],
            "skipComments": False,
            "time": "month" if type == "monthly" else "week"
        }

        run = client.actor("trudax/reddit-scraper").call(run_input=run_input)
        value = 0
        for item in client.dataset(run["defaultDatasetId"]).iterate_items():
            sentiment = get_sentiment(item["body"])

            value += sentiment * item["upVotes"]

        return Response(value)