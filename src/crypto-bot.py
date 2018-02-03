#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, json, urllib, logging

with open("config.json") as json_data:
    config = json.load(json_data)

auth = tweepy.OAuthHandler(config['CONSUMER_KEY'], config['CONSUMER_SECRET'])
auth.set_access_token(config['ACCESS_KEY'], config['ACCESS_SECRET'])
api = tweepy.API(auth)
period_in_minutes = config["interval"] / 60
logger = logging.getLogger("tweetbot")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))

def get_prices():
    prices = dict()
    for currency in config["currencies"]:
        url="https://min-api.cryptocompare.com/data/price?fsym={0}&tsyms=USD,EUR".format(currency)
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        prices[currency] = dict()
        prices[currency]["USD"] = data["USD"]
        prices[currency]["EUR"] = data["EUR"]
    return prices


def main():
    logger.info("Bot started")
    old_prices = get_prices()
    while True:
        try:
            prices = get_prices()
            message = ""
            for key in prices.keys():
                message += "#" + str(key) + ": $" + str(prices[key]["USD"]) + "/" + str(prices[key]["EUR"]) + "€\n"
                diff = old_prices[key]["USD"] - prices[key]["USD"]
                if diff > 0:
                    ten_percent = old_prices[key]["USD"] * 0.05
                    if prices[key]["USD"] < old_prices[key]["USD"] - ten_percent:
                        api.update_status("WARNING: #{0} is falling fast, previous price {3} mins ago: ${1} current price: ${2}".format(key,old_prices[key]["USD"],prices[key]["USD"], period_in_minutes))
            api.update_status(message)
            logger.info("Status posted")
            old_prices = prices
            time.sleep(config["interval"])
        except Exception as e:
            logger.exception("exception")

if __name__ == "__main__":
    main()