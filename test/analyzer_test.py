import logging
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")

from src.web_scrapper.sentiment_analyzer.analyzer import headlineAnalyzer
from src.web_scrapper.utils.utils import setup_logging

LOGGER = logging.getLogger(__name__)

def analyzer_test(headline, ticker, require_sentiment=True):
	a = headlineAnalyzer(headline, ticker, require_sentiment)
	result = a.analyze()
	return "headline: {}, direct: {}, rating: {}".format(headline, result.direct, result.score)

if __name__ == "__main__":
	setup_logging()
	headline_dict = {"Apple": 
						["Apple is acquired by Amazon",
					     "Amazon acquires Apple",
					     "Apple to be acquired by Amazon",
					     "Amazon to be acquired by Apple",
					     "Apple is acquiring Amazon",
					     "Apple acquired by Amazon",
					     "Apple wins pre-feed contract for 2019",
					     "Apple +4.6 as RBC raises to Outperform after summit",
					     "Citi Downgrades Apple To Sell On Increased Competition, Valuation",
					     "Apple misses on revenue",
					     "Amazon acquiring Apple, also an asteroid is coming to visit tomorrow",
					     "Apple acquiring Amazon, also an asteroid is coming to visit tomorrow",
					     "Apple won $1b in casino investment",
					     "Apple acquiring Amazon, in other news, I won a bet yesterday for $500"]
					 }

	for ticker in headline_dict:
		for headline in headline_dict[ticker]:
			LOGGER.info(analyzer_test(headline, ticker))