# -*- coding: utf-8 -*-

import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import wikipedia
import picamera
from time import sleep
TOKEN = 'Aquí va el tokken' # Nuestro tokken del bot (el que @BotFather nos dió).

bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
@bot.message_handler(commands=['hora']) # Indicamos que lo siguiente va a controlar el comando '/hora'.
def command_hora(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message( cid, time.strftime("%H:%M:%S")) # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
@bot.message_handler(commands=['prueba']) # Indicamos que lo siguiente va a controlar el comando '/prueba'
def command_prueba(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message( cid, 'probando') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
@bot.message_handler(commands=['wiki'])
def command_wiki(m):
    cid = m.chat.id
    msg = m.text[6:]
    if msg =='':
        bot.send_message(cid, "Escribe algo despues de /wiki")
    else :
        try:
            bot.send_message(cid,wikipedia.summary(msg, sentences=6))
        except wikipedia.exceptions.DisambiguationError as e:
            bot.send_message(cid, e)
@bot.message_handler(commands=['picamera'])
def command_picamera(m):
    cid = m.chat.id
    msg = m.text[6:]
    try:
        with picamera.PiCamera() as camera:
#           camera.hflip = True
#           camera.vflip = True
            camera.capture("imagen.jpg")
        sleep(1)
        photo = open('imagen.jpg', 'rb')
        bot.send_photo(cid, photo)
    except :
        bot.send_message(cid, "Fallo al  arrancar la camara, prueba mas tarde")

bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.
