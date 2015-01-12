from flask import Flask, render_template, jsonify
from flask import make_response

service = Flask(__name__)


@service.route('/')
def index():
    return render_template('index.html')


@service.route('/manifest')
def manifest():
    res = make_response(render_template('offline.appcache'), 200)
    res.headers["Content-Type"] = "text/cache-manifest"
    return res


@service.route('/fallback')
def fallback():
    res = make_response(render_template('fallback.html'), 201)
    return res


@service.route('/xxx')
def test():
    return render_template('index.html')


@service.route('/landing')
def landing():
    return render_template('landing.html')


@service.route('/landing1')
def landing1():
    return render_template('landing1.html')


@service.route('/landing2')
def landing2():
    return render_template('landing2.html')


@service.route('/deeds/userid/<userid>')
def get_deeds(userid):
    lst = [
        {'userid': userid, 'deed': {'a': 66, 'b': 222}},
        {'userid': userid, 'deed': {'a': 33, 'b': 111}},
        ]
    return jsonify(result=lst)


@service.route('/info/user/<userid>/<roomid>')
def set_info(userid, roomid):
    info = "Server received information for user "+userid+" for room " + roomid \
        + "."
    return jsonify(result=info)


if __name__ == '__main__':
    service.run(
        host="0.0.0.0",
        port=int("8001"),
        debug=True
    )
