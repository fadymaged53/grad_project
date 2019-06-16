from flask import Flask, render_template, request
from flask import redirect, jsonify, url_for,escape,request, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from setup import Base, Group,Message,UserGroups , User
from flask import session as lsession
import random
import string
from flask import make_response
import requests



app = Flask(__name__)
app.secret_key = "super secret key"


engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/signup',methods=['GET','POST'])
def signup ():
    if request.method == 'POST':
        newuser = User(name=request.form['name'],username=request.form['username'],password=request.form['password']
                       ,phone=request.form['phone'],address=request.form['address'])
        session.add(newuser)
        session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('signup.html')

#
# @app.route('/try')
# def home ():
#     one="one"
#     two="two"
#     three
#     return three



@app.route('/')
@app.route('/home')
def home ():
    return render_template('start.html')




@app.route('/signin',methods=['GET','POST'])
def signin ():
    if request.method == 'POST':
        user = session.query(User).filter_by(username=request.form['username']).one()
        password = request.form['password']
        userName=user.id
        if user.password == password:
            lsession['username'] = userName

            return render_template('userloggedinhome.html', user=user)




        else:
            #return "password doesnt match"
            return redirect(url_for('home'))
    else:
        return render_template('signin.html')




@app.route('/in')
def i():
    if 'username' not in lsession:
        return "not in"
    else:
        return " not in "


@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   lsession.pop('username', None)
   return redirect(url_for('home'))



@app.route('/add/<int:user_id>')
def add(user_id):
    if 'username' not in lsession:
        return "not in"
    else:
        users = session.query(User).order_by(asc(User.name))
        one=session.query(User).filter_by(id=user_id).one()

        return render_template('users.html',Allusers=users,user=one)


@app.route('/add/<int:user_id>/<int:seconduser_id>')
def addfriend(user_id,seconduser_id):
    if 'username' not in lsession:
        return "not in"
    else:
        one=session.query(User).filter_by(id=user_id).one()
        second=session.query(User).filter_by(id=seconduser_id).one()
        newGroup = Group(name="single-chat")
        session.add(newGroup)
        session.commit()
        usergroup1=UserGroups(user_id=user_id,group_id=newGroup.id)
        session.add(usergroup1)
        session.commit()
        usergroup2=UserGroups(user_id=user_id,group_id=newGroup.id)
        session.add(usergroup2)
        session.commit()

        return (one.name+" "+second.name)


@app.route('/chat')
def chat():
    return "chat"



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
