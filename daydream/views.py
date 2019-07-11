from flask import flash, redirect, url_for, render_template, session

from daydream import app, db

from daydream.forms import HelloForm, IndexForm

from daydream.models import Message, User


@app.route('/sayhello', methods=['GET', 'POST'])
def sayhello():
	# 加载所有记录
	messages = Message.query.order_by(Message.timestamp.desc()).all()
	form = HelloForm()

	if form.validate_on_submit():
		name = session['log_in']
		dream = Message(body=form.body.data)  # 实例化模型类，创建记录
		db.session.add(dream)  # 添加记录到数据库会话
		dream.user = User(nickname=name)
		db.session.commit()  # 提交会话
		return redirect(url_for('sayhello'))  # 重定向到sayhello视图

	return render_template('sayhello.html', form=form, messages=messages)


@app.route('/', methods=['GET', 'POST'])
def index():
	if 'log_in' in session:
		return redirect(url_for('sayhello'))

	form = IndexForm()
	if form.validate_on_submit():
		session['log_in'] = form.nickname.data
		name = form.nickname.data
		users = User(nickname=name)
		db.session.add(users)
		db.session.commit()
		flash('欢迎来到我的世界%s' % name)
		return redirect(url_for('sayhello'))

	return render_template('index.html', form=form)


@app.route('/logout')
def logout():
	if 'log_in' in session:
		session.pop('log_in')
	return redirect(url_for('index'))