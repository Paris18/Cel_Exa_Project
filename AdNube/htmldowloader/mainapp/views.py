
# django imports
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

# project level imports
# from libs.constants import (
# 		BAD_REQUEST,
# 		BAD_ACTION,
# )
# from libs.exceptions import ParseException
# from libs import redis_client
# from libs import ganeratepass
from libs.htmldowlnoader import runtask


from datetime import datetime




class UserViewSet(GenericViewSet):

	@action(methods=['post'], detail=False)
	def gethtmls(self, request):
		runtask.delay(request.data)
		print (datetime.now())
		return Response({"status":"mail has be sent u will receive shortly"}, status.HTTP_200_OK)