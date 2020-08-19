from flask import request
from flask_restplus import Namespace, Resource, fields
from model import db
from model.inquiry import Inquiry
from service.auth_service import authenticated_admin
from service.log_service import trace

api = Namespace(name='Travel Admin API', path='/api/inquiries', decorators=[trace])

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


@api.route('/')
class InquiryListResource(Resource):

    @api.doc(description='Get all inquiries', responses={200: 'Success', 403: 'Forbidden'}, security='Bearer Auth')
    @api.marshal_list_with(inquiry_dto)
    @api.param('title', description='Title', type='string')
    @api.param('message', description='Message', type='string')
    @authenticated_admin
    def get(current_user, self):
        
        title = request.args.get('title')
        message = request.args.get('message')
        
        inquiry = Inquiry.query

        if title:
            inquiry = inquiry.filter(Inquiry.title.ilike('%'+title+'%'))
        if message:
            inquiry = inquiry.filter(Inquiry.message.ilike('%'+message+'%'))

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

@api.route('/<id>')
@api.param('id', 'ID')
@api.response(404, 'Inquiry not found.')
class InquiryResource(Resource):
    @api.doc(description='Get inquiry', responses={200: 'Success', 403: 'Forbidden'}, security='Bearer Auth')
    @api.marshal_with(inquiry_dto)
    @authenticated_admin
    def get(current_user, self, id):
        inquiry = Inquiry.query.filter_by(id=id, user_id=current_user.id).first()
        if not inquiry:
            api.abort(404)
        else:
            return inquiry

    @api.doc(description='Delete inquiry', responses={200: 'Success', 403: 'Forbidden'}, security='Bearer Auth')
    @authenticated_admin
    def delete(current_user, self, id):
        inquiry = Inquiry.query.filter_by(id=id, user_id=current_user.id).first()
        if not inquiry:
            api.abort(404)
        else:
            db.session.delete(inquiry)
            db.session.commit()
            return {'message':'Inquiry has been deleted'}         