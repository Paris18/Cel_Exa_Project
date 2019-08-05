
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




class UserViewSet(GenericViewSet):

	@action(methods=['post'], detail=False)
	def register(self, request):
		runtask.delay(request.data)
		return Response({}, status.HTTP_200_OK)