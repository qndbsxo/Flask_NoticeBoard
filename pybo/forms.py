from typing import Text
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):
    subject = StringField(label="제목", validators=[DataRequired("제목은 필수입력 항목입니다")])
    content = TextAreaField(label="내용", validators=[DataRequired("내용은 필수입력 항목입니다.")])


class AnswerForm(FlaskForm):
    content = TextAreaField(
        label="내용", validators=[DataRequired(message="내용은 필수입력 항목입니다.")]
    )
