from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired, URL, Length, InputRequired


class LinkForm(FlaskForm):
    link = TextAreaField('Ссылка:', validators=[DataRequired(), URL(message="Неправильный формат ссылки")])
    title = TextAreaField('Заголовок:', validators=[DataRequired()])
    comment = TextAreaField('Комментарий:')

    link_submit = SubmitField()

class LinkFormSearch(FlaskForm):
    link = StringField('Ссылка:')
    title = StringField('Заголовок:')
    comment = StringField('Комментарий:')
    category = StringField('Категория:')

    search_submit = SubmitField()
