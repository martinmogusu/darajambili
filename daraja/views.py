from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import logging
import os
import json
from django.urls import reverse
from .models import Log

# Get logger instance
logger = logging.getLogger('daraja')

def index(request):
	logs = Log.objects.all()[:50]
	page_context = {
		'logs': logs
	}

	return render(request, 'index.html', context=page_context)

def clear_logs(request):
	'''
	Clear application logs
	'''

	# logs_path = os.path.join(settings.BASE_DIR, 'daraja.log')
	# with open(logs_path, 'w'):
	# 	pass
	
	Log.objects.all().delete()

	home_url = reverse('index')
	response = '<p>Logs cleared.</p> <a href="' + home_url + '">Back Home</a>'

	return HttpResponse(response)

def view_logs(request):
	'''
	View application logs
	'''

	# logs_path = os.path.join(settings.BASE_DIR, 'daraja.log')
	# logs = {}
	# with open(logs_path, 'r') as file:
	# 	for line in file.readlines():
	# 		timestamp = line[:23]
	# 		message = line[24:]
	# 		try:
	# 			json_message = json.loads(message)
	# 		except Exception as e:
	# 			json_message = message.replace('\n', '')
	# 		logs[timestamp] = json_message
	
	# # View newest logs first
	# log_items = list(logs.items())
	# log_items.reverse()
	# logs = dict(log_items)

	# Select 50 most recent logs
	log_items = Log.objects.all()[:50]

	logs = []
	for log in log_items:
		description = '{}' if log.description == "" else log.description
		description = json.loads(description)
		
		l = {
			'title': log.title,
			'description': description
		}
		logs.append(l)

	return JsonResponse(logs, safe=False)

@csrf_exempt
def callback(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'General callback'
	
	logger.info(data)
	logger.info(message)

	Log.objects.create(
		title=message,
		description = data
	)

	response = {
		'ResultCode': 0,
		'ResultDesc': 'Accepted'
	}

	return JsonResponse(response)

@csrf_exempt
def c2b_validation(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'C2B Validation request'
	
	logger.info(data)
	logger.info(message)

	Log.objects.create(
		title=message,
		description = data
	)

	response = {
		'ResultCode': 0,
		'ResultDesc': 'Accepted'
	}

	return JsonResponse(response)

@csrf_exempt
def c2b_confirmation(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'C2B Confirmation request'
	
	logger.info(data)
	logger.info(message)

	Log.objects.create(
		title=message,
		description = data
	)
	
	response = {
		'ResultCode': 0,
		'ResultDesc': 'Accepted'
	}

	return JsonResponse(response)

@csrf_exempt
def b2b_result(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'B2B Payment Result'
	
	logger.info(data)
	logger.info(message)

	Log.objects.create(
		title=message,
		description = data
	)

	return HttpResponse(message)

@csrf_exempt
def b2b_timeout(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'B2B Payment Timeout'
	
	logger.info(data)
	logger.info(message)

	Log.objects.create(
		title=message,
		description = data
	)

	return HttpResponse(message)

@csrf_exempt
def express_payment(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'MPESA Express payment result'
	
	logger.info(data)
	logger.info(message)

	Log.objects.create(
		title=message,
		description = data
	)

	return HttpResponse(message)

@csrf_exempt
def b2c_result(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'B2C Payment Result'
	
	logger.info(data)
	logger.info(message)

	Log.objects.create(
		title=message,
		description = data
	)

	return HttpResponse(message)

@csrf_exempt
def b2c_timeout(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'B2C Payment Timeout'
	
	logger.info(data)
	logger.info(message)

	Log.objects.create(
		title=message,
		description = data
	)

	return HttpResponse(message)

@csrf_exempt
def account_balance_result(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'Account Balance result'
	
	logger.info(data)
	logger.info(message)

	Log.objects.create(
		title=message,
		description = data
	)

	return HttpResponse(message)

@csrf_exempt
def account_balance_timeout(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'Account Balance timeout'
	
	logger.info(data)
	logger.info(message)

	Log.objects.create(
		title=message,
		description = data
	)

	return HttpResponse(message)

@csrf_exempt
def transaction_status_result(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'Transaction Status result'
	
	logger.info(data)
	logger.info(message)

	Log.objects.create(
		title=message,
		description = data
	)

	return HttpResponse(message)

@csrf_exempt
def transaction_status_timeout(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'Transaction Status timeout'
	
	logger.info(data)
	logger.info(message)

	Log.objects.create(
		title=message,
		description = data
	)

	return HttpResponse(message)

@csrf_exempt
def reversal_result(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'Reversal result'
	
	logger.info(data)
	logger.info(message)

	Log.objects.create(
		title=message,
		description = data
	)

	return HttpResponse(message)

@csrf_exempt
def reversal_timeout(request):
	data = request.body.decode().replace('\n', ' ')
	message = 'Reversal timeout'
	
	logger.info(data)
	logger.info(message)

	Log.objects.create(
		title=message,
		description = data
	)

	return HttpResponse(message)
