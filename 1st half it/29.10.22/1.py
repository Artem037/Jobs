from flask import Flask, render_template, url_for, request
import sqlalchemy

from forms.link_forms import LinkForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'strong_protection'
app.config['SQALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres@localhost:5439/my_app"

engine = sqlalchemy.create_engine(app.config['SQALCHEMY_DATABASE_URI'], echo=False)
print(engine)
