import random
mens = ['Ganaste🥳🥳🥳', 'Perdiste😤😤😤', 'Empate😐😐😐']
opciones = ('piedra', 'papel', 'tijera')

usuario_w = 0
computadora_w = 0
rondas = 1

while True:

  print('*' * 10)
  print('RONDA ', rondas)
  print('*' * 10)
  
  computadora_o = random.choice(opciones)

  user_o = input('piedra, papel o tijera => ')
  user_o = user_o.lower()
  
  if user_o == computadora_o:
    print(mens[2])
  
  elif user_o == 'piedra':
    if computadora_o == 'tijera':
      print(mens[0])
      usuario_w += 1
    else:
      print(mens[1])
      computadora_w += 1
  
  elif user_o == 'papel':
    if computadora_o == 'piedra':
      print(mens[0])
      usuario_w += 1
    else:
      print(mens[1])
      computadora_w += 1
  
  elif user_o == 'tijera':
    if computadora_o == 'papel':
      print(mens[0])
      usuario_w += 1
    else:
      print(mens[1])
      computadora_w += 1
  else:
    print('Error, intentalo de nuevo')
    continue


  if usuario_w == 2:
    print('-' * 10)
    print('Ganaste la partida🏆🏆🏆')
    break
    
  elif computadora_w == 2:
    print('-' * 10)
    print('Perdiste la partida😞😞😞')
    break
    
  rondas += 1