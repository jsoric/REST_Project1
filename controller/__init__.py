from flask_restplus import Api

from .first_admin_controller import api as first
from .auth_controller import api as auth
from .admin_inquiry_controller import api as admin_inquiry
from .user_inquiry_controller import api as inquiry
from .user_controller import api as user

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
    'Basic Auth': {
        'type': 'basic',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    title='Travel API',
    version='1.0.0',
    description='Sveučilište u Zadru - Studij informacijskih tehnologija - Razvoj web aplikacija',
    contact='josipsoric98@gmail.com',
    authorizations=authorizations,
    serve_challenge_on_401=False
)

api.add_namespace(first)
api.add_namespace(auth)
api.add_namespace(admin_inquiry)
api.add_namespace(inquiry)
api.add_namespace(user)