def calcular_salario(horas_trabalhadas, valor_hora, dias_trabalhados):
    """
    Calcular o calor a se pago, considerando horas trabalhadas,valor por hora e dias trabalhados.
    """

    salario_bruto = horas_trabalhadas * valor_hora
    valor_dias = dias_trabalhados * valor_hora * 2
    valor_total = salario_bruto + valor_dias
    return valor_total

#Solicitar dados ao usuario
horas = float(input("Digite o numero de horas trabalhadas: "))
valor_hora = float(input("Digite o valor por hora: "))
dias = int(input("Digite o numero de dias trabalhados: "))

#Calcular o salario total
salario_total = calcular_salario(horas, valor_hora, dias)

#Exibir o resultado
print(f"O valor total a ser pago é: R${salario_total:.2f}")
