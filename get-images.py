import json
import os
import pathlib
import requests

from datetime import datetime
from datetime import timedelta

# Do manual curl to register and get client_id and client_secret
secretsFile = 'secrets.json'
secrets = {}

# Store bearer token
tokensFile = 'tokens.json'
tokens = {}

# Query configuration
queryFile = 'queries.json'
queries = {}

# Load secrets, check if bearer token valid, get new if expired.
def getAndLoadTokens():
    currTime = datetime.now()
    getTokens = True

    # Load secrets
    if os.path.isfile(secretsFile):
        with open(secretsFile, 'r') as f:
            secrets = json.load(f)

    # Load token, check if new token needed
    if os.path.isfile(tokensFile):
        with open(tokensFile, 'r') as f:
            tokens = json.load(f)
            if 'expiry_time' in tokens:
                if currTime < datetime.fromtimestamp(tokens['expiry_time']):
                    getTokens = False

    # Get new token if necessary
    if getTokens == True:
        response = requests.post('https://api.creativecommons.engineering/v1/auth_tokens/token/',
                                 data={'client_id': secrets['client_id'], 'client_secret': secrets['client_secret'], 'grant_type': 'client_credentials'})
        tokens = json.loads(response.text)
        expiryTime = currTime + timedelta(seconds=int(tokens['expires_in']))
        tokens['expiry_time'] = int(expiryTime.timestamp())
        with open(tokensFile, 'w') as f:
            json.dump(tokens, f)    
    print(tokens)
    return tokens['access_token']

# Given access token, run each query, capture images to local folder
def findAndDownloadImages(accessToken):
    # Load query configuration
    with open(queryFile, 'r') as f:
        queries = json.load(f)
    
    # foreach query
    for query in queries:
        # create a folder for images
        cloudType = query['type']
        if not os.path.exists(cloudType):
            os.mkdir(cloudType)

        # get images for a given search params
        params = {'q': query['query']['q'], 'extension': query['query']['extension'], 'page_size':200}
        headers = {'Authorization': 'Bearer ' + accessToken}
        response = requests.get('http://api.creativecommons.engineering/v1/images', params=params, headers=headers)
        results = json.loads(response.text)
        
        # for each result in results list
        count = 1
        if 'results' in results:
            for result in results['results']:

                # get url, filename and file extension
                url = result['url']
                _ , ext = os.path.splitext(url) 
                imgFile = "%s-%d%s" % (cloudType, count, ext)
                count += 1

                # grab image content and store it in the file
                imgData = requests.get(url).content
                with open(os.path.join(cloudType, imgFile), 'wb') as handler:
                    handler.write(imgData)

def main():
    accessToken = getAndLoadTokens()
    findAndDownloadImages(accessToken)

main()
