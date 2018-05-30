#!/usr/bin/python
import dota2api

salem_id="76561198043845061"
salem_key="0A73920A08DA99E72C610B005860B22D"

matches_ids =[]

api = dota2api.Initialise(salem_key)
history_request = api.get_match_history(account_id=salem_id)

for n in history_request:
   matches_ids.append(history_request.values['matches']['match_id']
print (matches_ids)