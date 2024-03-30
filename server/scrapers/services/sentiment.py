from finvader import finvader


def get_sentiment(text: str):
    scores = finvader(text,
                      use_sentibignomics=True,
                      use_henry=True,
                      indicator='compound')

    return scores
