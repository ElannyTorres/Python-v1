class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class emojis:
  WINKING_FACE = '\N{winking face}'
  SMILE_FACE = '\U0001f600'

print('        _.-"\ ')
print('    _.-"     \ ')
print(' ,-"          \ ')
print('( \            \ ')
print(' \ \            \ ')
print('  \ \            \ ')
print('   \ \         _.-;')
print('    \ \    _.-"   :')
print('     \ \,-"    _.-"')
print(f'      \(   _.-"  Hi! {emojis.SMILE_FACE}')
user_name = input(f'       `--" Please write your name: ')
print(f'Hello {user_name.capitalize()}, let\'s start!')

print('=====================================================================')
print('A brief intro:')
print('Choose and option, which is colored and in caps. And write it!\nPlease pay attention to every answer, if you write a not available option you won\'t be able to continue.')
print('Best luck!')
print('=====================================================================')

error_msg = (f'{bcolors.FAIL}{bcolors.UNDERLINE}Option not available{bcolors.ENDC}')

def scenario():
  first_choice = input('Where do you want to go? ')
  if first_choice.lower() == 'home':
    print(f'\nYou are walking to your home. Thinking about what to cook. But maybe you can ask someone to join you. Maybe a {bcolors.OKBLUE}{bcolors.UNDERLINE}FRIEND{bcolors.ENDC} or {bcolors.OKBLUE}{bcolors.UNDERLINE}RELATIVE{bcolors.ENDC}.')
    scenarioA()
  elif first_choice.lower() == 'store':
    print(f'\nLet\'s go to the store. You arrive. Now is time to buy! What will you buy? There\'s many options. You need to choose, maybe something {bcolors.OKGREEN}{bcolors.UNDERLINE}SWEET?{bcolors.ENDC} Or something {bcolors.OKGREEN}{bcolors.UNDERLINE}SALT{bcolors.ENDC}? Or just something to {bcolors.OKGREEN}{bcolors.UNDERLINE}DRINK{bcolors.ENDC}?')
    scenarioB()
  else:
    print(error_msg)
    scenario()

def scenarioA():
  second_choice = input('What do you want to do? ')
  if second_choice.lower() == 'friend':
    print(f'\nA friend will be awesome! Let\'s see if someone is free. Maybe you can call {bcolors.OKBLUE}{bcolors.UNDERLINE}ANA{bcolors.ENDC}, {bcolors.OKBLUE}{bcolors.UNDERLINE}PETER{bcolors.ENDC} or {bcolors.OKBLUE}{bcolors.UNDERLINE}SARAH{bcolors.ENDC}.')
    scenarioA_A()
  elif second_choice.lower() == 'relative':
    print(f'\nYou love spending time with your family! Let\'s call someone. Your {bcolors.OKCYAN}{bcolors.UNDERLINE}MOM{bcolors.ENDC} or your {bcolors.OKCYAN}{bcolors.UNDERLINE}SISTER?{bcolors.ENDC}')
    scenarioA_B()
  else:
    print(error_msg)
    scenarioA()

def scenarioA_A():
  third_choice = input('Who will you call to? ')
  if third_choice.lower() == 'ana':
    print('\nYou call Ana, she doesn\'t have time, maybe next time.')
  elif third_choice.lower() == 'peter':
    print('\nYou call Peter. He is happy for the call. He was having a hard time. Good for both of you.')
  elif third_choice.lower() == 'sarah':
    print('\nYou call Sarah. You plan to meet in one hour more. She is bringing your favorite dessert!')
  else:
    print(error_msg)
    scenarioA_A()

def scenarioA_B():
  third_choice = input('Who will you call to? ')
  if third_choice.lower() == 'mom':
    print('\nShe is happy! And already going to your home! She is going to cook your favorte meal!')
  elif third_choice.lower() == 'sister':
    print('\nYour sister is a little bit busy, but she will be in an hour! Enjoy the time together!')
  else:
    print(error_msg)
    scenarioA_B()

def scenarioB():
  second_choice = input('What do you want to buy? Please choose just one. ')
  if second_choice.lower() == 'sweet':
    print(f'\nSomething sweet! It smells delicious! You turn and now you can see some {bcolors.WARNING}{bcolors.UNDERLINE}CINNAMON ROLLS{bcolors.ENDC}, {bcolors.WARNING}{bcolors.UNDERLINE}BUTTER COOKIES{bcolors.ENDC} and a {bcolors.WARNING}{bcolors.UNDERLINE}CHOCOLATE CAKE{bcolors.ENDC}. You touch your pocket and realize that you forgot it in your house! Oh no! You only have some coins, this mean you can buy just one.')
    scenarioB_A()
  elif second_choice.lower() == 'salt':
    print(f'\nYou\'ve seen a {bcolors.HEADER}{bcolors.UNDERLINE}PIZZA{bcolors.ENDC} and a {bcolors.HEADER}{bcolors.UNDERLINE}HAMBURGER{bcolors.ENDC}. Both seem so delicious.')
    scenarioB_B()
  elif second_choice.lower() == 'drink':
    print(f'You are thirsty. Maybe some {bcolors.OKBLUE}{bcolors.UNDERLINE}SODA{bcolors.ENDC}, or {bcolors.OKBLUE}{bcolors.UNDERLINE}JUICE{bcolors.ENDC} will help you.')
    scenarioB_C()
  else:
    print(error_msg)
    scenarioB()

def scenarioB_A():
  third_choice = input('What are you going to buy? ')
  if third_choice.lower() == 'cinnamon rolls':
    print('\nYou buy the cinnamon rolls. They smell and taste delicious. Enjoy them!')
  elif third_choice.lower() == 'butter cookies':
    print('\nButter cookies! They remember you your grandma. They bring you a special memory when you were young and spent time in the kitchen.')
  elif third_choice.lower() == 'chocolate cake':
    print('\nYumy yumy! They said that chocolate comes from a plant so it must count as a vegetable! Enjoy it!')
  else:
    print(error_msg)
    scenarioB_A()

def scenarioB_B():
  third_choice = input('What\'ll you choose? ')
  if third_choice.lower() == 'pizza':
    print('\nA pizza sound delicious. It a big one, you can take it home to share, too.')
  elif third_choice.lower() == 'hamburger':
    print('\nA hamburger. It delicious! Next time you will bring someone to enjoy together.')
  else:
    print(error_msg)
    scenarioB_B()

def scenarioB_C():
  third_choice = input('What\'s your choice? ')
  if third_choice.lower() == 'soda':
    print('\nMmmm. Not so healthy, but it helps. It tastes good. Are you planning to buy more?')
    print('Maybe next time!')
  elif third_choice.lower() == 'juice':
    print('\nA juice! A healthy choice! Your body will thank you. Now let\'s go home!')
  else:
    print(error_msg)
    scenarioB_C()


print(f'\nAs you\'re walking home, your stomach starts to rumble. You are hungry. You could keep walking {bcolors.HEADER}{bcolors.UNDERLINE}HOME{bcolors.ENDC} or stop by a {bcolors.HEADER}{bcolors.UNDERLINE}STORE{bcolors.ENDC} around the corner.')
scenario()

print('\nTHE END....')
print('just for now...')

print(' _._______')
print('| _______ |')
print('||,-----.||')
print('|||     |||')
print('|||_____|||')
print('|`-------\'| hjw')
print('| +     O | `97')
print('|      O  |')
print('| / /  ##,"')
print(' `------"')