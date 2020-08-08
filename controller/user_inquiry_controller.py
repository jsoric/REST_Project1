from flask_restplus import Namespace, Resource, fields
from model import db
from model.inquiry import Inquiry
from service.auth_service import authenticated

api = Namespace(name='User API', path='/api')

inquiry_create = api.model('CreateInquiry', {
    'title': fields.String(required=True, description='Title'),
    'message': fields.String(required=True, description='Message')
})

inquiry_dto = api.model('Inquiry', {
    'id': fields.Integer(required=True, description='ID'),
    'title': fields.String(required=True, description='Title'),
    'message': fields.String(required=True, description='Message'),
    'user_id': fields.Integer(required=True, description='User ID'),
    'created': fields.DateTime(required=True, description='Created'),
    'updated': fields.DateTime(required=True, description='Updated')
})

@api.route('/list-inquiries')
class Inquiries(Resource):
    @api.doc(description='List all inquiries', responses={200: 'Success', 401: 'Unauthorized'}, security='Bearer Auth')
    @api.marshal_list_with(inquiry_dto)
    @authenticated
    def get(current_user, self):
        inquiry = Inquiry.query.filter_by(user_id=current_user.id).all()
        output = []

        for inq in inquiry:
            inq_data = {}
            inq_data['id'] = inq.id
            inq_data['title'] = inq.title
            inq_data['message'] = inq.message
            inq_data['user_id'] = inq.user_id            
            inq_data['created'] = inq.created
            inq_data['updated'] = inq.updated
            output.append(inq_data)

        return output   

    @api.doc(description='Delete user', responses={200: 'Success', 401: 'Unauthorized'}, security='Bearer Auth')
    @api.param('email', description='Email', type='string')
    @authenticated
    def post(current_user, self):
        inquiry = Inquiry(title=api.payload['title'], message=api.payload['message'], user_id=current_user.id)
        db.session.add(inquiry)
        db.session.commit()

        return inquiry, 201  