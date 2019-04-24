import urllib.request
from bs4 import BeautifulSoup

twitter_url = 'https://twitter.com/'

def request_url(url, user):
    # Query the website (url) and return the html
    try:
        url += user
        page = urllib.request.urlopen(url)
        # Parse the html
        return BeautifulSoup(page, 'html.parser')
    except:
        return 'No response from Twitter.com'

# Get statistics from a given username: (amount of followers, amount of following, amount of tweets)
def stats(user_name, stat):
    requests = ['followers','following','tweets is-active']

    if user_name == '': return 'First argument must be provided' 
    elif stat == '': return 'Second argument must be provided'

    if stat in requests:
        stat_request = stat
    elif stat == 'tweets':
        stat_request = requests[2]          
    else:
        return f'Does not recognize "{stat}" as one of the enumerations'    

    response = request_url(twitter_url, user_name)
    nav_item = response.find(class_='ProfileNav-item ProfileNav-item--' + stat_request)

    if nav_item is not None: 
        return nav_item.find(class_='ProfileNav-value').get_text().strip()
    else:
        return f'User doesnt have any {stat}'    
    

print(stats('realdonaldtrump','followers'))