from user_controller import post_new_hash, post_login, get_all_hashs
from dotenv import load_dotenv

load_dotenv()

print('bem vindo ao sistema de login em python')
print('1. Cadastro')
print('2. Login')

user_input = input('Escolha: ')

if user_input == '1':
    post_new_hash()
elif user_input == '2':
    post_login()
