points = 0

tasks = {
      'train': 2,
      'to work': 4,
      'study': 5,
      'sleep': 0,
   }
ways = {
      'left': 5,
      'right': 6,
   }


while True:
    user = input('Enter your player name: ')
    if user == 'exit':
       print('Game finished.')
       break
    elif user == '':
       print('Empty input.')
    elif len(user) > 12 or len(user) <5:
       print('You can just type ultil 12 characters.')      
    else:
       print(f'Player name: {user}') # a área de login encerra quando o usuário digita o nome conforme os pré requisitos.
       break
    
while True:

   p = input('Choice what do you want to do: ').lower().strip() # the player make your choise
   if p == 'exit':
      print('Game finished.')
      print(f'{user} score: {points}')
      break

   elif p == 'tasks':
      op = input('Choice your task: ').lower().strip()
      if op in tasks:
         do = tasks[op]
         points += do
         print(f'{user} chose {op}')
         print(f'Actual score of {user}: {points}')

   elif p == 'go out':

      print('Left side')
      print('Right side')

      way = input('').lower().strip()
      if way in ways:
         choice = ways[way]