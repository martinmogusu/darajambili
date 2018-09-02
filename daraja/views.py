from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import logging
import os

# Get logger instance
logger = logging.getLogger('daraja')

def index(request):
	return HttpResponse('Daraja listener')

def clear_logs(request):
	'''
	Clear application logs
	'''

	logs_path = os.path.join(settings.BASE_DIR, 'daraja.log')
	with open(logs_path, 'w'):
		pass
	
	return HttpResponse('Logs cleared')

def view_logs(request):
	'''
	View application logs
	'''
	
	logs_path = os.path.join(settings.BASE_DIR, 'daraja.log')
	with open(logs_path, 'r') as file:
		logs = file.read()
	
	# Format logs
	logs = logs.replace('\n', '<br>')
	logs = logs.replace('\\n', '<br>')

	return HttpResponse(logs)

@csrf_exempt
def c2b_validation(request):
	data = {'body': request.body.decode()}
	message = 'Validation request'
	
	logger.info(message)
	logger.info(data)

	response = {
		'ResultCode': 0,
		'ResultDesc': 'Validation Accepted'
	}

	return JsonResponse(response)

@csrf_exempt
def c2b_confirmation(request):
	data = {'body': request.body.decode()}
	message = 'Confirmation request'
	
	logger.info(message)
	logger.info(data)
	
	response = {
		'ResultCode': 0,
		'ResultDesc': 'Accepted'
	}

	return JsonResponse(response)

@csrf_exempt
def b2b_result(request):
	data = {'body': request.body.decode()}
	message = 'B2B Payment Result'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def b2b_timeout(request):
	data = {'body': request.body.decode()}
	message = 'B2B Payment Timeout'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def express_payment(request):
	data = {'body': request.body.decode()}
	message = 'MPESA Express payment result'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def b2c_result(request):
	data = {'body': request.body.decode()}
	message = 'B2C Payment Result'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def b2c_timeout(request):
	data = {'body': request.body.decode()}
	message = 'B2C Payment Timeout'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def account_balance_result(request):
	data = {'body': request.body.decode()}
	message = 'Account Balance result'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def account_balance_timeout(request):
	data = {'body': request.body.decode()}
	message = 'Account Balance timeout'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def transaction_status_result(request):
	data = {'body': request.body.decode()}
	message = 'Transaction Status result'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def transaction_status_timeout(request):
	data = {'body': request.body.decode()}
	message = 'Transaction Status timeout'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def reversal_result(request):
	data = {'body': request.body.decode()}
	message = 'Reversal result'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def reversal_timeout(request):
	data = {'body': request.body.decode()}
	message = 'Reversal timeout'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)
