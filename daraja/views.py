from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import time

# Get logger instance
logger = logging.getLogger('daraja')

def index(request):
	return HttpResponse('Daraja listener')

@csrf_exempt
def c2b_validation(request):
	data = {'body': request.body}
	logger.info(data)

	response = {
		'ResultCode': 0,
		'ResultDesc': 'Validation Accepted'
	}

	return JsonResponse(response)


def c2b_confirmation(request):
	data = {'body': request.body}
	logger.info(data)
	
	response = {
		'ResultCode': 0,
		'ResultDesc': 'Accepted'
	}

	return JsonResponse(response)

