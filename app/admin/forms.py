from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired


class NewBlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    slug = StringField('Slug', validators=[DataRequired()])
    tags = SelectMultipleField('Tags', validators=[DataRequired()], choices=[
        ('swim', 'Swimming'),
        ('skate', 'Skating'),
        ('hike', 'Hiking')
    ])
    publish = SubmitField('发布')


class NewTagForm(FlaskForm):
    name = StringField('Tag Name', validators=[DataRequired()])
    save = SubmitField('保存')
