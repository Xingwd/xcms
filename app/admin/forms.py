from flask import g
from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Post, Tag


class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    slug = StringField('Slug', validators=[DataRequired()])
    tags = SelectMultipleField('Tags', validators=[DataRequired()], choices=[])
    outline = TextAreaField('Outline', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    post_submit = SubmitField('发布')

    def validate_title(self, title):
        post = Post.query.filter_by(title=title.data).first()
        if post is not None:
            if g.post_id:
                if post.id != int(g.post_id):
                    raise ValidationError('Title already exists.')
            else:
                raise ValidationError('Title already exists.')

    def validate_slug(self, slug):
        post = Post.query.filter_by(slug=slug.data).first()
        if post is not None:
            if g.post_id:
                if post.id != int(g.post_id):
                    raise ValidationError('Slug already exists.')
            else:
                raise ValidationError('Slug already exists.')


class NewTagForm(FlaskForm):
    tag_name = StringField('Tag Name', validators=[DataRequired()])
    tag_submit = SubmitField('Add')

    def validate_tag_name(self, tag_name):
        tag = Tag.query.filter_by(name=tag_name.data).first()
        if tag is not None:
            if g.tag_id:
                if tag.id != int(g.tag_id):
                    raise ValidationError('Tag already exists.')
            else:
                raise ValidationError('Tag already exists.')


