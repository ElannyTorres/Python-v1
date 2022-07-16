with open('hr_system.txt') as hr_system:
  #the file is open

  for line in hr_system:
    parts = line.split(" ")

    name = parts[0]
    id = parts[1]
    title = parts[2]
    salary = float(parts[3])
    
    pay_amount = salary / 24

    if title.lower() == 'engineer':
      pay_amount += 1000

    print(f'{name.capitalize()} (ID: {id}), {title} - ${pay_amount:.2f}')