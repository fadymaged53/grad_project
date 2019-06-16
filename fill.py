from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from setup import Message, UserGroups, Group, User,Base

engine = create_engine('sqlite:///database.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# Create dummy user
User1 = User(name="fady maged",id=1,username="fadyimaged",password="fadyfady",phone="0128038833")
session.add(User1)
session.commit()

User2 = User(name="ahmed",id=2,username="hmada",password="ahmedhamada",phone="013438833")
session.add(User2)
session.commit()

# create dummy Group
group = Group(name="project group",id=1)
session.add(group)
session.commit()

usergroup1 = UserGroups(user_id=1,group_id=1)
session.add(usergroup1)
session.commit()

usergroup2 = UserGroups(user_id=2,group_id=1)
session.add(usergroup2)
session.commit()

message = Message(text="hello",sender_id=1,group_id=1)


print ("added menu items!")
