#!/usr/bin/python
import dota2api
import psycopg2
import auth

user_id = auth.user_id "76561198043845061"
api_key = auth.api_key "0A73920A08DA99E72C610B005860B22D"

api = dota2api.Initialise(api_key)
history_request = api.get_match_history(account_id=user_id)

my_matches = history_request['matches'][1]['match_id']

conn = psycopg2.connect(host="localhost", database="doto2", user="postgress", password="dbpass2")

print(my_matches)