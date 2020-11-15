from main import send

user_name = input('Enter your name:')

print('hello, ' + user_name)

while True:
    message = input(' > ')
    if message == 'exit':
        break
    send(routing_key=user_name, message=message)

print('Goodby!')