import re
import logging
from django import http
from django.contrib.auth.models import AnonymousUser

REDIRECT_URI_REGEX = '(/accounts/login/)|(/admin/)|(/)'

class AuthenticationCheckMiddleware(object):

	def process_request(self, request):

		if (not request.user.is_authenticated() 
			and not re.match(REDIRECT_URI_REGEX, request.path)):
			logging.info('User not logged in. Redirected to Login page')
			return http.HttpResponseRedirect('/?next=%s' % request.path)
		#if not isinstance(request.user, AnonymousUser):
		return None