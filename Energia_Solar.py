from time import sleep
from Módulos_Solar import horas_sol, tarifas, Consumo, opção1_valor_placas, opção2_anual

menu_1 = """
O Simulador Solar é um programa que auxiliará na aquisição de um sistema de energia solar na sua casa. Ele abrange os estados da região Sudeste do Brasil e dimensiona uma média de um sistema ideal para você, 
que trará um maior retorno financeiro, baseado no seu consumo energético e na área disponível para instalação das placas fotovoltaicas.
"""
menu_2 = """
=-=-=-=-=-=-=-=-=-=-=-=-=-=
         MENU:
=-=-=-=-=-=-=-=-=-=-=-=-=-=
[ 1 ] - Análise de custos das placas solares.
[ 2 ] - Economia gerada pelas placas solares.
[ 3 ] - Tempo de retorno do investimento.
[ 4 ] - Previsão de manutenção das placas.  
[ 5 ] - Curiosidades sobre a energia solar.
[ 6 ] - Sair.
"""

print(menu_1)
sleep (3)

# consumo por dia (em kWh) / pico = kwhpico
# kWhPICO * 1000 / 330 = QUANTIDADE DE PLACAS (Multiplicar por 1000 para transformar KW em Watt)

# Horas de Sol Pleno por Estado (kWh/m²), com base nas capitais:
# ES - 4.96
# MG - 5.13 
# SP - 4.45
# RJ - 4.73

while True:
  
  print(menu_2)
  opção = float(input("Digite uma opção acima: "))
  while opção != 1 and opção != 2 and opção != 3 and opção != 4 and opção != 5 and opção != 6:
    opção = float(input("Opção inválida! Digite novamente: "))
  sleep(1)
    
  if opção == 1:
    print ("\nVocê escolheu avaliar seus custos das placas solares.")
    sleep(2)
    print ("Para isso, precisaremos de alguns dados de sua conta de luz.")
    sleep (2)
    opção1_valor_placas ()

    sleep(2)
    
  elif opção == 2:
    print("\nVocê escolheu saber a economia gerada pela instalação das placas fotovoltaicas.")
    sleep(2)
    print ("\nPara isso, precisaremos de alguns dados:")
    sleep (2)
    
    # Média de energia por horas:
    # Atlas solamétrico: ES, RJ, SP, MG = 6 horas

    # Cenario Ideal:
    # 335 * 6 = 2.010W
    # 20% de perda = 2.010 * 0,80 = 1.608w ou 1.60kWh

    opção2_anual ()
    sleep (2)
    
  elif opção == 3:
    print("\nAqui, você saberá o tempo de retorno do investimento que fez ao instalar as placas.")
    estado = input("\nEscolha o estado em que você mora (ES - MG - SP - RJ): ").upper()
    
    horas = horas_sol (estado)
    consumo_kWh_diario = Consumo ()
    kWh_pico = consumo_kWh_diario / horas #Calcular o Kwh_pico para determinar a quantidade de placas solares.
    quantidade_de_placas = (kWh_pico * 1000) / 335
    valor_total_placas = quantidade_de_placas * 849
    tarifa = tarifas (estado)
    
    EconomiaMensal = 1.60 * tarifa * 30 * quantidade_de_placas
    EconomiaAnual = EconomiaMensal * 12
    
    anos_retorno = valor_total_placas / EconomiaAnual
    y = round (anos_retorno)
    print (f"\nO tempo de retorno do seu investimento é de {y} anos.")
  
  elif opção == 4:
    print ("Aqui, você saberá após quanto tempo se deve fazer a manutenção de suas placas solares.")
    sleep (2)
    print ("\nPara isso, precisaremos de algumas informações: ")
    sleep(2)
    ano_instalação_placas = int(input("\nQual foi o ano que você instalou ou pretende instalar as placas solares? "))
    ano_manutenção_placas = ano_instalação_placas + 25
    sleep(2)
    print("\nOs paineis solares tendem a durar no mínimo 25 anos, perdendo, em média, 0,5% em eficiência de geração por ano.")
    sleep(4)
    print(f"\nAssim, você precisará fazer a manutenção das suas placas no ano de {ano_manutenção_placas}.")
    sleep(3)
    
  elif opção == 5:
    print("\nAqui estão algumas curiosidades sobre a Energia Solar: \n")
        
    Curiosidade1 = """
    * A energia solar funciona normalmente durante o dia todo e também nos dias nublados.
        
    * Nos períodos com luz solar, a energia é captada, distribuída e também armazenada. Dessa forma, também é possível utilizá-la durante a noite sem nenhum tipo de falha.
        
    * Já nos dias fechados, também é possível gerar energia, mas em menor escala. Por esse motivo você precisa contar com especialistas na hora de desenvolver o seu projeto de energia solar. 
    """
    Curiosidade2 = """
    * O Brasil é um dos países do mundo com maior potencial para geração de energia solar.

    * Segundo o Instituto Nacional de Pesquisas Espaciais (INPE), o Brasil é capaz de gerar 15 trilhões de megawatts por ano.

    * Na prática, isso representa quatro vezes mais do que uma usina hidrelétrica é capaz de produzir no mesmo período.
    """
    Curiosidade3 = """
    * Alguns meios de transporte também podem utilizar a energia solar. Até o momento, já foram feitos experimentos em motos, carros, barcos e aviões, por exemplo.
    """
    sleep (2)
    print (Curiosidade1)
    sleep (10)
    print (Curiosidade2)
    sleep (10)
    print (Curiosidade3)
    sleep (5)
    
  elif opção == 6:
    print("\nVocê clicou em sair do programa. Até mais!")
    break

  sleep (1)
  print ("\n/// Obrigado por participar! Você retornará ao Menu inicial. /// \n")
  sleep (2)