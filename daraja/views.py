from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import logging
import os
import json

# Get logger instance
logger = logging.getLogger('daraja')

def index(request):
	page_context = {}
	return render(request, 'index.html', context=page_context)

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
	logs = {}
	with open(logs_path, 'r') as file:
		for line in file.readlines():
			timestamp = line[:23]
			message = line[24:]
			try:
				json_message = json.loads(message)
			except Exception as e:
				json_message = message.replace('\n', '')
			logs[timestamp] = json_message
	
	return JsonResponse(logs, safe=False)

@csrf_exempt
def c2b_validation(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'C2B Validation request'
	
	logger.info(message)
	logger.info(data)

	response = {
		'ResultCode': 0,
		'ResultDesc': 'Accepted'
	}

	return JsonResponse(response)

@csrf_exempt
def c2b_confirmation(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'C2B Confirmation request'
	
	logger.info(message)
	logger.info(data)
	
	response = {
		'ResultCode': 0,
		'ResultDesc': 'Accepted'
	}

	return JsonResponse(response)

@csrf_exempt
def b2b_result(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'B2B Payment Result'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def b2b_timeout(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'B2B Payment Timeout'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def express_payment(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'MPESA Express payment result'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def b2c_result(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'B2C Payment Result'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def b2c_timeout(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'B2C Payment Timeout'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def account_balance_result(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'Account Balance result'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def account_balance_timeout(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'Account Balance timeout'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def transaction_status_result(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'Transaction Status result'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def transaction_status_timeout(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'Transaction Status timeout'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def reversal_result(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'Reversal result'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)

@csrf_exempt
def reversal_timeout(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'Reversal timeout'
	
	logger.info(message)
	logger.info(data)

	return HttpResponse(message)
