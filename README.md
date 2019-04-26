# Twitce

An easy to use python module that lets you gather user information from twitter

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Twitce.

```bash
pip install twitce
```

## Usage
To gather statistical information from a user, use the stats() method.

```python
import twitce

twitce.stats('user','followers') # Returns the amount of followers // e.g 59871542
twitce.stats('user','following') # Returns the amount of people the requested user is following // e.g 20
twitce.stats('user','tweets') # Returns the amount of tweets // e.g 4
```

To gather profile information from a user, use the profile() method.
```python
import twitce

twitce.profile('user','name') # Returns the name
twitce.profile('user','screenname') # Returns screenname
twitce.profile('user','bio') # Returns bio description
twitce.profile('user','location') # Returns fixed location
twitce.profile('user','url') # Returns the URL from a given website 
twitce.profile('user','join') # Returns the date when the account was created 
twitce.profile('user','birth') # Returns the birthdate
```

## Error handling
Twitce comes with simple error handling. Both methods, profile() and stats() should be provided with 2 arguments:

```python
twitce.profile('','bio') # Returns 'First argument must be provided'
twitce.stats('user','') # Returns 'Second argument must be provided' 
```
When a enumeration is not recognized: 
```python
twitce.stats('user','tweetssss') # Returns 'Does not recognize "tweetssss" as one of the enumerations'
```
When the requested user doesn't have any tweets (or another enum):
```python
twitce.stats('user','tweets') # Returns 'User doesnt have any tweets' 
```
If for example the birthdate is not specified:
```python
twitce.profile('user','birth') # Returns 'None specified' 
```
When the requested user does not exist:
```python
twitce.profile('userdoesnotexist','birth') # Returns 'User does not exist' 
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
