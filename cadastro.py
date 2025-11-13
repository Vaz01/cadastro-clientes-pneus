print("-" * 50)
print("CADASTRO DE CLIENTES")
print("-" * 50)

cliente = input("Digite Seu Login De Acesso : ") 
senha = input("Digite Sua Senha : ")

cliente_acesso = "Felipe Vaz"
acesso =  "10203040"

# Verificando Login

if senha ==  acesso and cliente == cliente_acesso:
    print(f"Login Feito Com Sucesso")
else:
    print("Usuário Ou Senha Incorreta. Por Favor , Tente Novamente ❌")
    exit("Programa Encerrado")

print("-" * 50)
print("ESTOQUE DE PNEUS")
print("-" * 50)

try:
    quantidade_pneus = int(input("Digite a quantidade de pneus: "))
    preco_unitario = 99.90
    total = quantidade_pneus * preco_unitario
    print(f"💰 Valor total da compra: R$ {total:.2f}")
except ValueError:
    print("Por favor, digite apenas números.")

