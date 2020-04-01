from wise import app


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # app.run(port=5000, host='0.0.0.0', debug=True, static_files = {'/static': '/path/to/static'})
    app.run(port=5000, host='0.0.0.0', debug=True)
