from flask import flash, redirect, url_for, render_template

from daydream import app, db

from daydream.forms import HelloForm

from daydream.models import Message


@app.route('/sayhello', methods=['GET', 'POST'])
def sayhello():
	# 加载所有记录
	messages = Message.query.order_by(Message.timestamp.desc()).all()
	form = HelloForm()

	if form.validate_on_submit():
		name = form.name.data
		body = form.body.data
		messages = Message(body=body, name=name)  # 实例化模型类，创建记录
		db.session.add(messages)  # 添加记录到数据库会话
		db.session.commit()  # 提交会话
		flash('留言成功！')
		return redirect(url_for('sayhello'))  # 重定向到sayhello视图

	return render_template('sayhello.html', form=form, messages=messages)

@app.route('/')
def index():
	return render_template('index.html')