from flask import Blueprint, render_template, abort
from simpledu.models import User, Course

user = Blueprint('user', __name__, url_prefix="/user")

@user.route('/<name>')
def index(name):
    try:
        user = User.query.filter(User.username == name).first()
        data = {}
        data['id'] = user.id
        data['username'] = user.username
        data['courses'] = []
        courses = Course.query.filter(Course.author_id == data['id']).all()
        for i in courses:
            data['courses'].append(i.name)
        return render_template('user/detail.html', data=data)

    except Exception as e:
        abort(404)

@user.errorhandler(404)
def handle_bad_request(e):
    return 'Bad Request!', 404

