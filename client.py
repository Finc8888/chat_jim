#Клиент чата который взаимодествует (отправляет запрос) с сервером чата по 
#протоколу JIM(JSON instant messaging)

import json
from time import ctime
from socket import *
import sys
# try:
# 	print()
# except:
# 	print("Неправильно определен модуль времени")

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
	presence_messaging = {
		"action" : action,
		"time" : ctime(),
		"type" : status,
		"user" : {
				"account_name" : account_name,
				"status" : "YEP, I AM HERE"
		}
	}
	presence_jim_messinging = json.dumps(presence_messaging)
	return presence_jim_messinging
#TODO Разобрать сообщение от сервера
def watch_messiging(mes):
	"""
	"""
	answer = json.loads(mes)
	return answer
#TODO Отправить сообщение серверу, получить ответ 
#Разбирает полученный ответ сервера от сервера
def client(ip = 'localhost', port = 7777, msg = None):
	"""
	Отправляет серверу precence-сообщение, получает от него ответ

	"""
	s = socket(AF_INET, SOCK_STREAM)#Создает сокет TCP
	s.connect((ip, port))
	s.send(make_pressence_messaging().encode())
	print("Send - Ok")
	answer_from_server_jim = s.recv(1024)
	print(answer_from_server_jim)
	#answer_from_server = watch_messiging(answer_from_server_jim)
	s.close()
	return answer_from_server_jim
if __name__ == '__main__':
	client()

	 
