segundos_str = input("Porfavor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

dias =  total_segs // 86400
horas = dias %
seg_restantes = total_segs % 3600
minutos = seg_restantes // 60
segs_restantes_final = seg_restantes % 60

print(dias, "dias, ",horas, "horas, ", minutos, "minutos e", segs_restantes_final, "segundos.")
