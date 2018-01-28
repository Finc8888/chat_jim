#Клиент чата который взаимодествует (отправляет запрос) с сервером чата по 
#протоколу JIM(JSON instant messaging)

import json
from time import ctime
from socket import *
import sys
import argparse
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
def cmd_parser():
	"""
	Парсит именнованные аргументы командной строки
	с помшощью модуля argparse.
	При этом аргументы передается в командной строке
	в виде: python client.py -port 7777 -addr localhost
	или python client.py -p 7777 -a localhost

	"""
	parser = argparse.ArgumentParser()
	parser.add_argument('-addr')
	parser.add_argument('-port', type = int)
	return parser

def client(ip = 'localhost', port = 7777, msg = None):
	"""
	Отправляет серверу precence-сообщение, получает от него ответ

	"""
	# if len(sys.argv)>1:
	# 	# print(len(sys.argv))
	# 	ip = sys.argv[1]
	# 	# print(addr)
	# 	port = int(sys.argv[2])
	# 	# print(port, type(port))
	#Парсим командную строку на наличие аргументов
	parser = cmd_parser()
	namespace = parser.parse_args(sys.argv[1:])
	print(namespace) 
	if namespace.addr:
		ip = namespace.addr
	if namespace.port:
		port = namespace.port	
	#Создаем сокет
	s = socket(AF_INET, SOCK_STREAM)#Создает сокет TCP
	s.connect((ip, port))
	s.send(make_pressence_messaging().encode('utf-8'))
	#print("Send - Ok")
	answer_from_server_jim = s.recv(1024)
	#print(answer_from_server_jim.decode('utf-8'))
	answer_from_server = watch_messiging(answer_from_server_jim)
	#print(answer_from_server['response'])
	s.close()
	return answer_from_server['response']
if __name__ == '__main__':
	print(client())

	 
