from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>🛒 My Secure E-Commerce Store</h1><p>Status: Live on GKE!</p>"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
