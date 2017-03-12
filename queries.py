from data import *
from parser import *

def insert_users(Id, Reputation, Location, Views, UpVotes, DownVotes, Age):
	Session.execute(insert(Users).values(Id = Id, Reputation = Reputation, Location= Location, Views= Views, UpVotes = UpVotes, DownVotes = DowbVotes, Age = Age))
	Session.commit()
	return "User information successfully inserted"

