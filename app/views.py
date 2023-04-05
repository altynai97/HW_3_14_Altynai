import os

from flask import request, render_template, url_for, redirect, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.utils import secure_filename

from . import app, db
from .models import Transactions, User
from .forms import UserForm, TransactionsForm, TransactionsUpdateForm, UserLoginForm, UserRegisterForm



def index():
    title = 'Онлайн Банкинг'
    transactions = Transactions.query.all()
    return render_template('index.html', title=title, transactions=transactions)


@login_required
def transactions_create():
    form = TransactionsForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_transactions = Transactions(
                period=form.period.data,
                value=form.value.data,
                status=form.value.data,
                unit=form.unit.data,
                subject=form.subject.data
            )
            db.session.add(new_transactions)
            db.session.commit()
            flash('Транзакция успешно сохранена', 'Успешно!')
            return redirect(url_for('index'))
        else:
            print(form.errors)
            text_list = []
            for field, errors in form.errors.items():
                text_list.append(f'{field} : {", ".join(errors)}')
            flash(f'При сохранении категории произошла ошибка{". ".join(text_list)}', 'Ошибка!')
    return render_template('transactions.html', form=form)


@login_required
def transactions_list():
    transaction_list = Transactions.query.all()
    return render_template('transactions_list.html', transaction_list=transaction_list)


@login_required
def transactions_update(transactions_id):
    transactions = Transactions.query.get(transactions_id)
    form = TransactionsUpdateForm(meta={'csrf': False}, obj=transactions)
    if request.method == 'POST':
        form.populate_obj(transactions)
        db.session.add(transactions)
        db.session.commit()
        return redirect(url_for('transactions_list'))
    else:
        print(form.errors)
    return render_template('transactions_delete.html', form=form)


@login_required
def transactions_delete(transactions_id):
    transaction = Transactions.query.get(transactions_id)
    if request.method == 'POST':
        db.session.delete(transaction)
        db.session.commit()
        return redirect(url_for('transaction_list'))
    return render_template('transactions_delete.html', transaction=transaction)


def user_register():
    form = UserRegisterForm()
    title = 'Регистрация'
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User()
            form.populate_obj(new_user)
            db.session.add(new_user)
            db.session.commit()
            flash(f'Пользователь {new_user.username} успешно зарегистрирован!', 'Успех!')
            return redirect(url_for('user_login'))
        else:
            text_list = []
            for field, errors in form.errors.items():
                text_list.append(f'{field} : {", ".join(errors)}')
            flash(f'При регистрации произошла ошибка{". ".join(text_list)}', 'Ошибка!')

    return render_template('accounts/index.html', form=form, title=title)


def user_login():
    form = UserLoginForm()
    title = 'Авторизация'
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                login_user(user)
                flash('Вы успешно вошли в систему', 'Успех!')
                return redirect(url_for('index'))
            else:
                flash('Неверные логин и пароль', 'Ошибка!')

    return render_template('accounts/index.html', form=form, title=title)


def user_logout():
    logout_user()
    return redirect(url_for('user_login'))














