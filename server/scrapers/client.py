import os
from apify_client import ApifyClient


client = ApifyClient(os.getenv("APIFY_API_KEY"))
