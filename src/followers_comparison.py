import sys
import json

def load_followers(followers_filename: str):
    with open(followers_filename, 'r') as file:
        followers = json.load(file)

    followers_set = set()
    for account in followers:
        followers_set.add(account['string_list_data'][0]['value'])

    return followers_set

def load_following(following_filename: str):
    with open(following_filename, 'r') as file:
        following = json.load(file)

    following_set = set()
    for account in following['relationships_following']:
        following_set.add(account['string_list_data'][0]['value'])

    return following_set

def compare_followers(following_set: set, followers_set: set):
    return following_set.difference(followers_set)

if __name__ == '__main__':
    following_filename = sys.argv[1]
    followers_filename = sys.argv[2]
    
    following_set = load_following(following_filename)
    followers_set = load_followers(followers_filename)
    
    no_follow_back = compare_followers(following_set, followers_set)

    for account in no_follow_back:
        print(account)