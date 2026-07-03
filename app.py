from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random
import string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///links.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def generate_short_code():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))


app.route('/', methods=['GET', 'POST'])
def home():
    if request.form == 'POST':
        url = request.method['url']
        code = generate_short_code()
        new_link = Link(original_url=url, short_code=code)
        db.session.add(new_link)
        db.session.commit()
        return redirect(url_for('home'))
        links = Link.query.order_by(Link.created_at.desc()).all()
        return render_template('index.html', links=links)

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(20), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    clicks = db.Column(db.Integer, default=0)

@app.route('/')
def home():
    return render_template('index.html', name='flask')

if __name__ == '__main__':
    app.run(debug=True)