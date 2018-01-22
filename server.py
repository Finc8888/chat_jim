#Сервер чата который взаимодествует (обрабатывает запросы) с клиентом чата по 
#протоколу JIM(JSON instant messaging)

import json
from time import ctime
from socket import *
import sys

#TODO Принять сообщение клиента


#TODO Принять сообщение клиента
def get_messaging(mes):
	"""
	Принять сообщение клиента в формате JSON. Возвращает декодированные данные
	JSON объекта

	"""
	reciving_data = json.dumps(mes)
	return reciving_data
def response():
	"""
	Формирует ответ клиенту в формате JSON. Возвращает ответ в виде
	JSON объекта:{
		"response" : 1xx/2xx,
		"time" : <unix timestamp>,
		"alert" : "message(optional for 2xx codes"
	}

	"""
	responce_list =["100 - базовое уведомление,\
	               200 - OK", "404 - пользователь отсутствует на сервере",\
	               "500 - ошибка сервера"]
	try:
		resp = {
		"response" : responce_list[1],
		"time" : ctime(),
		"alert" : "message(optional for 2xx codes)"
	}
	except:
		resp["response"] = responce_list[2]


def server(port = 7777, addr = ''):
	s = socket(AF_INET, SOCK_STREAM)#Создает сокет TCP
	if 1 < (len(sys.argv)) >= 3:
		port = sys.argv[1]
		addr = sys.argv[2]
	elif len(sys.argv) == 1:
		s.bind((addr, port))	
		s.listen(5)#Переходит в реж. ожид-я запросов одноврем-но обслуж. не более 5
		print("Сервер слушает {} порт...".format(port))
		while True:
			client, addr = s.accept()#Принять запрос на соединение
			print("Получен запрос на соединение от {}".format(addr))
			json_messaging = client.recv(1024)
			messaging = get_messaging(json_messaging)
			client.send(messaging.encode('utf-8'))
			client.close()
	else:
		print("Неверное количество переданных аргументов")

if __name__ == '__main__':
	server()