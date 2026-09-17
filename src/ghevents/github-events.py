#!/usr/bin/env python3
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events(url):
    '''Retrieves users' events from GitHub API'''
    response = requests.get(url)
    return json.loads(response.text)

def print_events(events,n):
    '''prints the last n events'''
    for x in events[:n]:
        event = x['type'] + ' :: ' + x['repo']['name']
        print(event)

def main():
    print(f"Github user: {GHUSER}")
    print(f"Retrieving events from: {url}")
    print_events(retrieve_events(url), 5)

if __name__ == "__main__":
    main()