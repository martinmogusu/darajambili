from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
		path('logs/view', views.view_logs, name='view_logs'),
	path('logs/clear', views.clear_logs, name='clear_logs'),
	path('callback', views.callback, name='callback'),
	path('c2b/validation', views.c2b_validation, name='c2b_validation'),
	path('c2b/confirmation', views.c2b_confirmation, name='c2b_confirmation'),
	path('express-payment', views.express_payment, name='express_payment'),
	path('b2b/result', views.b2b_result, name='b2b_result'),
	path('b2b/timeout', views.b2b_timeout, name='b2b_timeout'),
	path('b2c/result', views.b2c_result, name='b2c_result'),
	path('b2c/timeout', views.b2c_timeout, name='b2c_timeout'),
	path('account-balance/result', views.account_balance_result, name='account_balance_result'),
	path('account-balance/timeout', views.account_balance_timeout, name='account_balance_timeout'),
	path('transaction-status/result', views.transaction_status_result, name='transaction_status_result'),
	path('transaction-status/timeout', views.transaction_status_timeout, name='transaction_status_timeout'),
	path('reversal/result', views.reversal_result, name='reversal_result'),
	path('reversal/timeout', views.reversal_timeout, name='reversal_timeout'),
]