import requests

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth('YP11F3gRha6joEHslP--zw', 'ZBE0nS65pmbu_7z3iY_1jY3fvIQpxw')

# here we pass our login method (password), username, and password
data = {
    'grant_type': 'password',
    'username': 'TheColdLemonade',
    'password': 'TheCold123'
}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'MyBot/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

def getData():
    try:
        title = ""
        post_name = ""
        res = requests.get('https://oauth.reddit.com/r/AskReddit/random', headers=headers).json()
        title = res[0]['data']['children'][0]['data']['title']
        post_name = res[0]['data']['children'][0]['data']['author']
        res = requests.get('https://oauth.reddit.com'+res[0]['data']['children'][0]['data']['permalink'], headers=headers).json()
        commentName = [res[1]['data']['children'][0]['data']['author'],res[1]['data']['children'][1]['data']['author'],res[1]['data']['children'][2]['data']['author'],res[1]['data']['children'][3]['data']['author']]
        commentPost = [res[1]['data']['children'][0]['data']['body'],res[1]['data']['children'][1]['data']['body'],res[1]['data']['children'][2]['data']['body'],res[1]['data']['children'][3]['data']['body']]
    except:
        try:
            title = ""
            post_name = ""
            res = requests.get('https://oauth.reddit.com/r/AskReddit/random', headers=headers).json()
            title = res[0]['data']['children'][0]['data']['title']
            post_name = res[0]['data']['children'][0]['data']['author']
            res = requests.get('https://oauth.reddit.com' + res[0]['data']['children'][0]['data']['permalink'],
                               headers=headers).json()
            commentName = [res[1]['data']['children'][0]['data']['author'],
                           res[1]['data']['children'][1]['data']['author'],
                           res[1]['data']['children'][2]['data']['author'],
                           res[1]['data']['children'][3]['data']['author']]
            commentPost = [res[1]['data']['children'][0]['data']['body'], res[1]['data']['children'][1]['data']['body'],
                           res[1]['data']['children'][2]['data']['body'], res[1]['data']['children'][3]['data']['body']]
        except:
            try:
                title = ""
                post_name = ""
                res = requests.get('https://oauth.reddit.com/r/AskReddit/random', headers=headers).json()
                title = res[0]['data']['children'][0]['data']['title']
                post_name = res[0]['data']['children'][0]['data']['author']
                res = requests.get('https://oauth.reddit.com' + res[0]['data']['children'][0]['data']['permalink'],
                                   headers=headers).json()
                commentName = [res[1]['data']['children'][0]['data']['author'],
                               res[1]['data']['children'][1]['data']['author'],
                               res[1]['data']['children'][2]['data']['author'],
                               res[1]['data']['children'][3]['data']['author']]
                commentPost = [res[1]['data']['children'][0]['data']['body'],
                               res[1]['data']['children'][1]['data']['body'],
                               res[1]['data']['children'][2]['data']['body'],
                               res[1]['data']['children'][3]['data']['body']]
            except:
                title = ""
                post_name = ""
                res = requests.get('https://oauth.reddit.com/r/AskReddit/random', headers=headers).json()
                title = res[0]['data']['children'][0]['data']['title']
                post_name = res[0]['data']['children'][0]['data']['author']
                res = requests.get('https://oauth.reddit.com' + res[0]['data']['children'][0]['data']['permalink'],
                                   headers=headers).json()
                commentName = [res[1]['data']['children'][0]['data']['author'],
                               res[1]['data']['children'][1]['data']['author'],
                               res[1]['data']['children'][2]['data']['author'],
                               res[1]['data']['children'][3]['data']['author']]
                commentPost = [res[1]['data']['children'][0]['data']['body'],
                               res[1]['data']['children'][1]['data']['body'],
                               res[1]['data']['children'][2]['data']['body'],
                               res[1]['data']['children'][3]['data']['body']]

    return title, post_name, commentPost, commentName