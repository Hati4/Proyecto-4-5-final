"""
user :admin
password : admin123!
url: http://127.0.0.1:58000

{
Required: password,username
password:
string

password
username:
string

username
}
"""
import requests
import json
import conf

url = "http://127.0.0.1:58000/api/v1/ticket"
dato = {
    "password": conf.clave,
    "username": conf.usuario
}

cabecera = {"content-type":"application/json"}
respuesta = requests.post(url, json.dumps(dato), headers=cabecera)
respuesta_json = respuesta.json()
print("API-Token: "+respuesta_json['response']['serviceTicket'])
API_Token = respuesta_json['response']['serviceTicket']

urlinventario = "http://127.0.0.1:58000/api/v1/network-device"
cabecerainventario = {"content.type":"application/json","X-Auth-Token":API_Token }

respuesta_del_inventario = requests.get(urlinventario, headers=cabecerainventario)
respuesta_del_inventario_json = respuesta_del_inventario.json()
print(respuesta_del_inventario_json)