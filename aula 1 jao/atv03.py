idade = int(input('digite sua idade: '))
habilitacao = (input('voce tem habilitacao [sim/não]: '))

if (idade >=18 and habilitacao in "sim"):
  print(f'voce é maior de idade e possui habilitação')

elif (idade >=18 and habilitacao in "não"):
  print(f'voce é maior de idade e não possui habilitação')

else:
  print(f"Você é menor de idade e não pode tirar habilitação!")