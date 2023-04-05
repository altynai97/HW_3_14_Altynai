from . import app, db
from . import views

app.add_url_rule('/', view_func=views.index)

app.add_url_rule('/transactions/create', view_func=views.transactions_create, methods=['POST', 'GET'])
app.add_url_rule('/transactions/list', view_func=views.transactions_list)


app.add_url_rule('/transactions/<int:transactions_id>/update', view_func=views.transactions_update,
                 methods=['POST', 'GET'])
app.add_url_rule('/transactions/<int:transactions_id>/delete', view_func=views.transactions_delete,
                 methods=['POST', 'GET'])

app.add_url_rule('/account/register', view_func=views.user_register, methods=['POST', 'GET'])
app.add_url_rule('/account/login', view_func=views.user_login, methods=['POST', 'GET'])
app.add_url_rule('/account/logout', view_func=views.user_logout)
