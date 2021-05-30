import serial
from turtle import *
import turtle as t

arduino = serial.Serial('COM6', 19200)
print('통신시작')

t.left(90)

while 1:
  left = int(int(arduino.readline().decode())/100)*100
  right = int(int(arduino.readline().decode())/100)*100
  print("left: ", left, " right:", right)
  move = (left+right)/100-30
  t.fd(move)
  if (left <= 1500 and right <= 1500):
    t.bk(-move)
  if (left>right):
    t.right(10)
  elif (left<right):
    t.left(10)