from flask import render_template, request, flash , session, redirect, url_for

from app.module_users import bp
from app.module_users.models import User
import app.module_users.tools as tools

from app.extensions import db

# 1: Kellner
# 2: Verwaltung
# 3: Admin


@bp.route('/login', methods=['POST', 'GET'])
def login():
    sessionUser = tools.getSessionUser()
    if sessionUser["permission"] > 0:
        return redirect(url_for('main.index'))

    else: 
        if request.method == 'POST':
            login = request.form
            userName = login['username']
            password = login['password']

            signedIn, permission, user= tools.verify(userName,password)
            if signedIn:
                session['logged_in'] = True
                session['permission'] = permission
                session['user_name'] = userName
                session['user_id'] = user.id
                return redirect(url_for('main.index'))

            else:
                flash('wrong password!')
                logout()
                return redirect(url_for('users.login'))
        else:
            
            return render_template('users/login.html')


@bp.route('/logout')
def logout():
    session['logged_in'] = False
    session['permission'] = 0
    session['user_name'] = None
    session['user_id'] = None
    return redirect(url_for('main.index'))


@bp.route('/addUser', methods=['POST','GET'])
def add_user():
    sessionUser = tools.getSessionUser()
    if sessionUser.get("permission") >= 3:
        if request.method == 'POST':
            login = request.form

            userName = login['username']
            password = login['password']
            email = login['email']
            permission = login['permission']
            if not tools.add_User(userName,password,permission,email):
                flash("Error creating User " + userName)

            return redirect(url_for('users.manageUsers'))

        elif request.method == 'GET':
            return redirect(url_for('users.manageUsers'))
    else:
        return redirect(url_for('main.index'))


@bp.route('/', methods=['GET'])
def manageUsers():
    sessionUser = tools.getSessionUser()
    if sessionUser.get("permission") >= 3:
        return render_template('users/manageUsers.html',users = tools.getUsers())
    else:
        return redirect(url_for('main.index'))

@bp.route('/deleteUser', methods=['POST'])
def deleteUser():
    sessionUser = tools.getSessionUser()
    if sessionUser.get("permission") >= 3:
        request_data = request.get_json()
        if 'id' in request_data:
            id = request_data["id"]
            tools.deleteUser(id)

        return redirect(url_for('user.manageUsers'))
    else:
        return redirect(url_for('user.login'))
