from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///links.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class link(db.Model):
    id = db.сolumn(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable = False)
    short_code = db.Column(db.String(20), unique=True, nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    clicks = db.column(db.Integer, default=0)


@app.route('/')
def home():
    return 'Hello flask'

if __name__ == "__main__":
    app.run(debug=True)