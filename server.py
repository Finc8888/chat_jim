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
	reciving_data = json.loads(mes)
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
	responce_list =["100 - базовое уведомление",\
	               "Код ошибки: 200 - OK", "404 - пользователь отсутствует на сервере",\
	               "500 - ошибка сервера"]
	# try:
	resp = {
	"response" : responce_list[1],
	"time" : ctime(),
	"alert" : "message(optional for 2xx codes)"}
	resp = json.dumps(resp)
	return resp
	# except:
	# 	resp["response"] = responce_list[2]


def server(port = 7777, addr = ''):
	s = socket(AF_INET, SOCK_STREAM)#Создает сокет TCP
	if len(sys.argv)>1:
		# print(len(sys.argv))
		addr = sys.argv[1]
		# print(addr)
		port = int(sys.argv[2])
		# print(port, type(port))
	s.bind((addr, port))	
	s.listen(5)#Переходит в реж. ожид-я запросов одноврем-но обслуж. не более 5
	print("Сервер слушает {} порт...".format(port))
	while True:
		client, addr = s.accept()#Принять запрос на соединение
		print("Получен запрос на соединение от {}".format(addr))
		json_messaging = client.recv(1024)
		#print("json -catch")
		json_ms_decode = json_messaging.decode()
		#messaging = get_messaging(json_ms_decode)
		client.send(response().encode('utf-8'))
		client.close()
	

if __name__ == '__main__':
	server()