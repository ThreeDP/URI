time_seconds = int(input())
time = {'horas': 0, 'minutos': 0, 'segundos': 0}

time['horas'] = int(time_seconds / 3600)
time['minutos'] = int((time_seconds - (time['horas'] * 3600))/60)
time['segundos'] = int(time_seconds % 60)

print("{hour}:{minute}:{second}".format(hour = time['horas'], minute = time['minutos'], second = time['segundos']))
