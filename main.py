from bottle import route, run, template, error, abort, redirect, request, post, get, response, view, static_file

@route('/')
def index():
    return template('index')

@route('/testing_base')
def testing_base():
    return template('testing_base')

@route('/alerts')
def alerts():
    return template('alerts')


@error(404)
def error404(error):
    return 'Opa, página não encontrada!'

@error(401)
def error401(error):
    return 'Error: 401 Unauthorized (Não autorizado, chulezento!)'

@route('/restricted')
def restricted():
    abort(401, "Sorry, access denied.")

@route('/wrong/url')
def wrong():
    redirect("/right/url")

@route('/hello')
@route('/hello/<name>')
@view('hello_template')
def hello(name='Marlon'):
    return dict(name=name)

@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')

# @route('/login')
# def do_login():
#     username = request.forms.get('username')
#     password = request.forms.get('password')
#     if check_login(username, password):
#         response.set_cookie("account", username, secret='some-secret-key')
#         return template("<p>Welcome {{name}}! You are now logged in.</p>", name=username)
#     else:
#         return "<p>Login failed.</p>"

@route('/restricted')
def restricted_area():
    username = request.get_cookie("account", secret='some-secret-key')
    if username:
        return template("Hello {{name}}. Welcome back.", name=username)
    else:
        return "You are not logged in. Access denied."




run(host='localhost', port=8080)