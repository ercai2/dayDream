from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, TextAreaField

from wtforms.validators import DataRequired, Length, ValidationError


def nickname(form, field):
	if len(field.data) == 0 or len(field.data) >12:
		raise ValidationError('昵称长度在1到12之间')

def dream(form, field):
	if len(field.data) == 0:
		raise ValidationError('请输入你的星愿吧')
	if len(field.data) > 50:
		raise ValidationError('长度不能超过50 ~')

class HelloForm(FlaskForm):
	body = TextAreaField('Message', validators=[dream])
	submit = SubmitField('发送')


# 首页填写昵称并登录
class IndexForm(FlaskForm):
    nickname = StringField('昵称: ', validators=[nickname])
    submit = SubmitField('开始')