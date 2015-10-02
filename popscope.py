import ephem
from flask import Flask, Response, request, render_template, json, g
app = Flask(__name__)
app.debug = True

CATALOG = {
    'moon': ephem.Moon,
    'saturn': ephem.Saturn,
    'jupiter': ephem.Jupiter,
}
# from http://www.themcdonalds.net/richard/index.php?title=Recommended_Beginner_Astronomy_Targets
# M37
# M38
# M45
# M31
# M42
# M35
# M3
# Mizar
# M11
# M13
# M92
# M27
# M57
# M8
# Epsilon Lyrae
# Albireo
# NGC 457
# NGC 869 & 884 (h and χ Persei)
from functools import wraps

def json_view(callable_to_wrap):
    """
    Wraps a function that returns a tuple with an HTTP status code and a
    dict-like object to serialize, and makes it return a JSON response through
    Flask
    """
    @wraps(callable_to_wrap)
    def new_callable(*args, **kwargs):
        status_code, object_to_serialize = callable_to_wrap(*args, **kwargs)
        jsonresponse = json.dumps(jsonobj)
        res = Response(jsonresponse, status=200, mimetype='application/json')
        return res

    return new_callable

@app.route('/sky/<float:latitude>/<float:longitude>')
@json_view
def sky(latitude, longitude):
    # each object should have a rise and set time for an observer at the current location
    # and maybe alt/az? cardinal directions?
    return

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
