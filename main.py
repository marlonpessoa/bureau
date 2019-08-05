from bottle import debug, route, run, template, error, abort, redirect, request, post, get, response, view, static_file

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

@route('/login')
def login():
    return template('login')

@route('/dashboard')
def dashboard():
    return template('v-1')

@route('/login2')
def login2():
    return template('extended')



@route('/restricted')
def restricted_area():
    username = request.get_cookie("account", secret='some-secret-key')
    if username:
        return template("Hello {{name}}. Welcome back.", name=username)
    else:
        return "You are not logged in. Access denied."
debug(True)

run(host='localhost', reloader = True,port=8080)