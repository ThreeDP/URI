input_days = int(input())
time = {'ano': 0, 'mes': 0, 'dia': 0,}
time['ano'] = int(input_days / 365)
time['mes'] = int((input_days - (time['ano'] * 365)) / 30)
time['dia'] = int((input_days - (time['ano'] * 365)) % 30)

print("{age} ano(s)\n{mouth} mes(es)\n{day} dia(s)".format(age = time['ano'], mouth = time['mes'], day = time['dia']))
