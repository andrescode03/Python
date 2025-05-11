# ESTO LO QUE HACE ES QUE EJECUTA TODA LA LISTA Y A SU VEZ ME OMITE LO QUE YO QUIERO QUE OMITA, EJECUTA Y CONTINUA

frutas = ["banano", "manzana", "pera", "mango"]

for fruta in frutas:
    if fruta == 'banano':
        continue
    print(f'me voy a comer {fruta}')
    
# SI LO QUE QUEREMOS ES QUE CUANDO LLEGUE A DETERMINADO MOMENTO SE DETENGA LA EJECUCIÓN ES CON 'BREAR'

for fruta in frutas:
    if fruta == 'manzana':
        break
    print(f'me voy a comer {fruta}')