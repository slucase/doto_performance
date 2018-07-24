#!/usr/bin/python
import dota2api
import json
import my_auth
from collections import namedtuple

user_id = my_auth.user_id
api_key = my_auth.api_key

api = dota2api.Initialise(api_key)
history = api.get_match_history(account_id=user_id)

#Loop for getting the matches ids
my_matches = []
n_results = history['num_results']

for i in range(n_results):
   my_matches.append(history['matches'][i]['match_id'])

#Loop for getting the friends and nemesis data
for i in range(n_results):
   m = api.get_match_details(match_id = my_matches[i])
   player[i] = m['players'][i]['player_slot']
   print(player)

#print(api.get_heroes())
#print(my_matches)
