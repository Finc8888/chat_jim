#Клиент чата который взаимодествует (отправляет запрос) с сервером чата по 
#протоколу JIM(JSON instant messaging)

import json
from time import ctime
try:
	print(ctime())
except:
	print("Неправильно определен модуль времени")

#TODO Сформировать presence-сообщение
def make_pressence_messaging(action = "presence", time = "ctime()", status =
 "YEP, I AM HERE", account_name = "Gavroche"):
	"""
	Функция которая формирует сервисное presence-сообщение о присутсвии, 
	которое отсылается серверу когда клиент пытается к нему подключиться.
	Возвращает JSON объект
	Формат сообщения  по протоколу JIM:{
		"action" : "presence",
		"time" : <unix timestamp>,
		"type" : "status",
		"user" : {
				"account_name" : "Gavroche",
				"status" : "YEP, I AM HERE"
		}
	}

	""" 
	pass