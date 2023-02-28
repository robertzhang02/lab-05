import flask 

app = flask.Flask(__name__)

# TODO: create a route for the delay endpoint.
#      The route should accept POST requests and return the same message that was sent to it.
@app.route('/delay_endpoint', methods = ['POST'])
def add_route():
    return flask.request.data


if __name__ == "__main__":
    app.run(port = 5000, debug = True)
