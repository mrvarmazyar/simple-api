from bottle import default_app

from . import controllers

app = default_app()


app.route('/hello/<username>', method=['GET'], callback=controllers.get_user)
app.route('/hello', method=['POST'], callback=controllers.create_user)
app.route('/hello/<username>', method=['PUT'], callback=controllers.update_user)
app.route('/hello/<username>', method=['DELETE'], callback=controllers.delete_user)
