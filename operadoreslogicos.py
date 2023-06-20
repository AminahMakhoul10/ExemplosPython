#True or False
#7 != 3 and 2 > 3

# Tabela verdade do 'AND'
# EXEMPLO P IR P SHOPPING PRECISA DE 2 CONDIÇOES EX; se esta ensolarado e ter dinheiro na conta vc vai no shopping = true,se tiver ensolarado e nao tiver dinheiro na conta vc nao vai= falso

#TRUE AND TRUE = TRUE
#TRUE AND FALSE = FALSE
#FALSE AND TRUE = FALSE
#FALSE AND FALSE = FALSE
#TRUE AND TRUE AND TRUE AND FALSE AND TRUE AND TRUE = FALSO

#Tabela Verdade do 'OR'
# EXEMPLO: vc vai pro shopping ou se tiver ensolarado OU se vc tiver dinheiro na conta,

#TRUE OR TRUE = TRUE
#TRUE OR FALSE = TRUE
#FALSE OR TRUE = TRUE
#FALSE OR FALSE = FALSE
# FALSE OR FALSE FALSE OR FALSE FALSE OR TRUE FALSE OR FALSE = TRUE

# TABELA VERDADE DO 'XOR' = excluisvamente tem que ser um ou outro
#TRUE != TRUE = FALSE
#TRUE != FALSE = TRUE
#FALSE != TRUE = TRUE
#FALSE != FALSE = FALSE   != significa : ' diferente de '

# OPERAÇÃO DE 'NEGAÇÃO' (UNÁRIO)
# not True = False
# not False = True
# not 0 = TRUE
# not 1 = FALSE 
# not -1 = TRUE
# not not -1 = TRUE
# not True = FALSE
# not not True = True

# CUIDADO 'operadores bit a bit
# True & True = bit a bit
# False | True = pype
# True ^ False = xor

# REALIDADE

saldo = 1000
salario = 4000
despesas = 2967

meta = saldo > 0 and salario - despesas >= 0.2  * salario 
meta 
