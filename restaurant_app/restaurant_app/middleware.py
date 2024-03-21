from django.utils.deprecation import MiddlewareMixin


class AddUserToContextMiddleware(MiddlewareMixin):
    def process_template_response(self, request, response):
        response.context_data['user'] = request.user
        return response
