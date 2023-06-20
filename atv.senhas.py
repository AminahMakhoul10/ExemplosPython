import time

print('SISTEMA DE LOGIN')
print('')
time.sleep(1)

possiveis_senhas = ['batata123', 'cenoura123', '123Mamao123#', 'casagrande', '123amelhorsenha123', 'narutouzumaki', 'iphonedolucas', 'senhasegura4584', '123vcnaosabekkk','nemtentedescobrir' ]

print('Você tem 1 tentativa, caso erre a sua conta será bloqueada.')
time.sleep(2)

digita_senha = input('Digite sua senha: ')
time.sleep(1.5)
if digita_senha in possiveis_senhas:
  print("Senha correta, logado com sucesso!")
else:
  print("Senha incorreta, conta bloqueada.")