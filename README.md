# WeSmart

WeSmart Twitterbot

# Installation

1. `$ pip install -r requirements.txt`

2. Running the periodic tweet checks require a bit of knowledge on using [Celery](http://docs.celeryproject.org/en/latest/index.html).

- Broker setup: [RabbitMQ](http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html)

# Running

- Just running the bot once:

`$ make bot-run`

- Run bot every interval

`$ make periodic-run`

# The Bot's Goals

- [x] Send a reply on a tweet containing a hashtag `#wesmart`
- [x] Reply must have a "roll safe" image
- [x] Check for tweets every [interval] minutes

![wesmart image](./docs/wesmart.jpg)

# License

This software is licensed under the [MIT License](./LICENSE).
