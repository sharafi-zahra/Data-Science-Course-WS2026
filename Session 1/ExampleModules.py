# Example module used in Session 1 to demonstrate imports and classes.
# Keep this file in the same folder as the Session 1 notebook.

def squareIt(x):
    return float(x) ** 2


def sqrtIt(x):
    if x >= 0:
        return float(x) ** 0.5
    else:
        return None


class stockBeta():
    """
    Beta measures a stock's volatility compared to the market.
    beta = 1.0: moves like the market | beta > 1.0: more volatile | beta < 1.0: less volatile

    Raw beta (from historical data) can be unreliable long-term, so it is common to
    adjust it towards the market average of 1.0 (the "Blume adjustment").
    """

    def __init__(self, beta):
        self.beta = beta

    def adjustBeta(self):
        # Blume adjustment: a weighted average of the raw beta and the market average beta (1.0)
        return 0.66 * self.beta + 0.33 * 1

    def squareIt(self):
        return self.beta ** 2

    def __repr__(self):
        return f"stockBeta(beta={self.beta})"
