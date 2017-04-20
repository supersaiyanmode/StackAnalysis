import sys
sys.path.insert(0, '../models')
from data import session_factory as session, ViewUserSkills as Skills, Users, Tags

def get_users():
	res = session.query(Users).filter(Users.upvotes>200)
	return [int(x.id) for x in res]

def get_top_skills(user_id):
	base_query = session.query(Skills)
	filtered_query = base_query.filter(Skills.user_id == user_id).filter(Skills.total_score > 20)
	res = filtered_query.order_by(Skills.total_score.desc()).limit(4)
	return [get_tag_name(x.user_skill_id) for x in res]

def get_tag_name(tag_id):
	res = session.query(Tags).filter(Tags.id == tag_id)
	#print [x.name for x in res]
	return [x.name for x in res][0]

def write_transactions():
	f = open('../../data/skill_transactions_4','w')
	for i in get_users():
		skillset = get_top_skills(i)
		for j in skillset:
			f.write(j+" ")
		f.write("\n")
	f.close()
	return "success"

write_transactions()
