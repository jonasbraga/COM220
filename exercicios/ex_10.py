import math

def horaSeg(hora, min, seg):
  return hora * 60 * 60 + min * 60 + seg

def segHora(totalSeg):
  seg = totalSeg % 60 
  min = (totalSeg // 60) % 60
  hora = totalSeg // 3600
  return [ hora, min, seg ]

momentoEntrada = input('Digite o horário de entrada no formato HH:MM:SS -> ')

horaEntrada = int(momentoEntrada[0:2])
minEntrada = int(momentoEntrada[3:5])
segEntrada = int(momentoEntrada[6:8])

quantSegEntrada = horaSeg(horaEntrada, minEntrada, segEntrada)

momentoSaida = input('Digite o horário de saída no formato HH:MM:SS -> ')

horaSaida = int(momentoSaida[0:2])
minSaida = int(momentoSaida[3:5])
segSaida = int(momentoSaida[6:8])

quantSegSaida = horaSeg(horaSaida, minSaida, segSaida)

duracaoSeg = quantSegEntrada - quantSegSaida

hora, min, seg = segHora(duracaoSeg)

print('O usuário ficou conectado por {}:{}:{}'.format(hora, min, seg))