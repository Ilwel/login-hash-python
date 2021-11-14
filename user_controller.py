from pypika import Query, Table, Field
from connection import cursor, connection
from hash_generator import create_hash, verify_hash


def post_new_hash():
    print('Cadastro:')
    name = input('insira o usuário: ')
    password = input('insira a senha: ')
    hash = create_hash(password)
    passwords = Table('passwords')

    q = Query.from_(passwords).select('name').where(passwords.name == name)
    cursor.execute(str(q))
    result = cursor.fetchall()
    if result:
        raise 'Já tem um usuário com este login'

    q = Query.into(passwords).columns(
        "name", "password").insert(name, hash)
    cursor.execute(str(q))
    connection.commit()
    post_login()


def post_login():
    print('Login:')
    name = input('insira o usuário: ')
    password = input('insira a senha: ')
    passwords = Table('passwords')

    q = Query.from_(passwords).select('password').where(passwords.name == name)
    cursor.execute(str(q))
    result = cursor.fetchall()
    if not result:
        raise 'Email ou Senha errados'
    result = map(lambda item: item[0], result)
    [result] = result

    if verify_hash(password, result):
        print(f'Bem vindo {name}')
    else:
        raise 'Email ou Senha errados'


def get_all_hashs():
    q = Query.from_('passwords').select('password', 'name')
    cursor.execute(str(q))
    result = cursor.fetchall()
    result = map(lambda item: {'name': item[1], 'hash': item[0]}, result)
    result = list(result)
    return result
