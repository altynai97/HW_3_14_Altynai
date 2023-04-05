from flask_wtf import FlaskForm
import wtforms as wf

from . import app
from .models import Transactions, User


def transactions_choices():
    choices = []
    with app.app_context():
        transactions = Transactions.query.all()
        for transaction in transactions:
            choices.append((transaction.id, transaction.name))
    return choices


class TransactionsForm(FlaskForm):
    period = wf.StringField(label=' Период', validators=[
        wf.validators.DataRequired()
    ])
    value = wf.IntegerField(label='Сумма', validators=[
        wf.validators.DataRequired()
    ])
    status = wf.StringField(label='Статус', validators=[
        wf.validators.DataRequired()
    ])
    unit = wf.StringField(label='Тип валюты', validators=[
        wf.validators.DataRequired()
    ])
    subject = wf.StringField(label='Комментарии проводки', validators=[
        wf.validators.DataRequired()
    ])


class TransactionsUpdateForm(FlaskForm):
    period = wf.StringField(label=' Период', validators=[
        wf.validators.DataRequired()
    ])
    value = wf.IntegerField(label='Сумма', validators=[
        wf.validators.DataRequired()
    ])
    status = wf.StringField(label='Статус', validators=[
        wf.validators.DataRequired()
    ])
    unit = wf.StringField(label='Тип валюты', validators=[
        wf.validators.DataRequired()
    ])
    subject = wf.StringField(label='Комментарии проводки', validators=[
        wf.validators.DataRequired()
    ])


class UserForm(FlaskForm):
    username = wf.StringField(label='Логин', validators=[
        wf.validators.DataRequired()
    ])
    password = wf.PasswordField(label='Пароль', validators=[
        wf.validators.DataRequired(),
    ])


class UserLoginForm(FlaskForm):
    username = wf.StringField(label='Логин', validators=[
        wf.validators.DataRequired(),
        wf.validators.Length(min=3, max=20)
    ])
    password = wf.PasswordField(label='Пароль', validators=[
        wf.validators.DataRequired(),
    ])


class UserRegisterForm(UserLoginForm):
    password_2 = wf.PasswordField(label='Пароль', validators=[
        wf.validators.DataRequired(),
    ])

    def validate(self, *args, **kwargs):
        if not super().validate(*args, **kwargs):
            return False
        if self.password.data != self.password_2.data:
            self.password_2.errors.append('Пароли должны совпадать')
            return False
        return True

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).count() > 0:
            raise wf.ValidationError('Пользователь с таким username уже существует')
