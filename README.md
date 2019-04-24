# Twitce 
An easy to use python module that lets you gather user information from twitter

## Install
You can install Twitce with pip:
`pip install twitce`

## Usage
To gather statistics from a user, use the `twitce.stats('username','statistic')` method. 
It takes an username (string) as the first argument and a statistic as the second argument (string).

Statistics: 'tweets', 'followers', 'following'

To get the amount of followers from a requested user:

`twitce.stats('user','followers')`

To get the amount of people who the requested user is following:

`twitce.stats('user','following')`

To get the amount of tweets the requested user has posted:

`twitce.stats('user','tweets')`

`twitce.stats('realdonaldtrump','tweets')
    # Returns 41.414
`
