from sqlite3 import Cursor
from application import cur
from flask import Blueprint, request, jsonify
from app.lib.bd import *

from application import cur
user_bp=Blueprint('user_bp',__name__)
@user_bp.route('/lister_user',method='GET')
def list_user():
    query = "select * from utilisateur"
    cur.execute(query)
    list=cur.fetchall()
    return jsonify(list)

