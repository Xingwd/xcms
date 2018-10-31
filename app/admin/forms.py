from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired


class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    slug = StringField('Slug', validators=[DataRequired()])
    tags = SelectMultipleField('Tags', validators=[DataRequired()], choices=[])
    publish = SubmitField('发布')


class NewTagForm(FlaskForm):
    name = StringField('Tag Name', validators=[DataRequired()])

