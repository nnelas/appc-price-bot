# appc-price-bot

A Discord bot to check AppCoins price, in Python. 

This bot also haves a task that periodically checks the price change on the 
last 24 hours of APPC (%) and sends a message if percentage >= 20% or percentage <= -10%.

Uses Binance API to get 24h percentage change (and also the volume, although it's not 
currently being used). Uses Catappult API to get current price in both USD and EUR.

## Installation instructions (Linux)

```shell
$ sudo apt install python3.7 pipenv
```

Also, you'll need to add the Discord Bot token into your environment variables.
```shell
$ vim ~/.zshrc
DISCORD_BOT_TOKEN='XXXX'

$ source ~/.zshrc
```

## Usage

To start the Discord Bot:
```shell
$ pipenv run python main.py
```

If you want to keep it running:
```shell
$ nohup pipenv run python main.py > ../logs/appc-price-bot.log &
```

## Supported commands

```shell
!price
Current price is: 0.13172865$ / 0.11123083€ 
Changed 24.32% in the last 24h

!ping
Pong! :ping_pong:
```