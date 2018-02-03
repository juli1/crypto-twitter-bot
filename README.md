# Twitter bot for crypto currency

This is a bot that get crypto-currencies values
and post them on twitter.

Example of how it works: https://twitter.com/crypt_analyst

# How to use

1. Checkout the code
2. Build your virtual environment ```python3 -m venv venv```
3. Active your virtual environment ```source venv/bin/activate```
4. Install dependencies ```pip3 install -r requirements.txt```
5. Put your keys in ```config.json```
6. Run it ```./src/crypto-bot.py```


# Configuration
The configuration file is like this:
```
{
  "CONSUMER_KEY": "<YOUR-VALUE>",
  "CONSUMER_SECRET": "<YOUR-VALUE>",
  "ACCESS_KEY": "<YOUR-VALUE>",
  "ACCESS_SECRET": "<YOUR-VALUE>",
  "currencies" : ["BTC","LTC","ETH", "DASH", "ZEC", "XRP"],
  "interval" : 1800
}
```

The ```*_KEY``` and ```*_SECRET``` are the values from your twitter dev account.

The ```currencies``` configuration directive is the list of crypto-currencies
to follow. The bot will monitor these crypto-currencies.

The ```interval``` directive is the interval at which your bot posts. The unit
is the second.
