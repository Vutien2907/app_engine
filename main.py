from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from App Engine Ver1.1!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

#update at Fri Jun 27 08:59:56 AM UTC 2025
