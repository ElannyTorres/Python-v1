user_friend = ''
user_friends = []

while user_friend != 'end':
  user_friend = input('Type the name of a friend: ')
  
  if user_friend != 'end':
    user_friends.append(user_friend)

print('Your friends are:')
for friend in user_friends:
  print(friend)