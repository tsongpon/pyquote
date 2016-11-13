from flask import Flask

app = Flask('pyquote')

def start_app():
    app.run(host='0.0.0.0', port=5000, threaded=True)

if __name__ == '__main__':
    start_app()
