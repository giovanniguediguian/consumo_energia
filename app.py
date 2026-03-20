#Entrada de dados
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts: "))
uso_diario = float(input("Digite o tempo de uso diário do aparelho em horas: "))
cobrança_por_kWh = float(input("Digite o valor da cobrança por kWh: "))

#Processamento
consumoMensal = (potencia * uso_diario * 30) / 1000 #Convertendo para kWh
valor_estimado = consumoMensal * cobrança_por_kWh #Calculando o valor estimado da conta de energia

#Saída de dados
print(f"Aparelho: {aparelho}")
print (f"Consumo estimado: {consumoMensal:.2f} kWh/mês")
print(f"Valor estimado da conta de energia: R${valor_estimado:.2f}")