from time import sleep

def horas_sol (estado) :
  sleep (2)
 
  while estado != "ES" and estado != "MG" and estado != "SP" and estado != "RJ":
    estado = input("Opção inválida! Digite novamente: ").upper()

  if estado == "ES" :
    horas = 4.96
  elif estado == "MG" :
    horas = 5.13
  elif estado == "SP" :
    horas = 4.45 
  elif estado == "RJ" :
    horas = 4.73

  return horas


def tarifas (estado) :
  sleep (2)
      
  while estado != "ES" and estado != "MG" and estado != "SP" and estado != "RJ":
    estado = input("Opção inválida! Digite novamente: ").upper()

  if estado == "ES" :
    tarifa = 0.56
  elif estado == "MG" :
    tarifa = 0.62
  elif estado == "SP" :
    tarifa = 0.72
  elif estado == "RJ" :
    tarifa = 0.58

  return tarifa


def Consumo () :
  consumo_kWh_mensal = float(input("\nQual seu consumo mensal em kWh em sua residência? (Valor encontrado em sua conta de luz): "))
  consumo_kWh_diario = consumo_kWh_mensal / 30
  sleep (2)
  print(f"\nO seu consumo em Kwh por mês é de {consumo_kWh_mensal} kWh e o consumo diário é de {consumo_kWh_diario:.2f} kWh.\n")
  return consumo_kWh_diario


def opção1_quantidade () :
  consumo_kWh_diario = Consumo ()
  estado = input("Escolha o estado em que você mora (ES - MG - SP - RJ): ").upper()
  horas = horas_sol (estado)
  
  kWh_pico = consumo_kWh_diario / horas
  quantidade_de_placas = (kWh_pico * 1000) / 335
    
  x = round (quantidade_de_placas) # Arredondar a quantidade de placas.
  print(f"\nVocê precisará de {x} placas solares de 335 Watts de potência.")
  sleep (2)

  return quantidade_de_placas


def opção1_valor_placas () : 
  
  quantidade_de_placas = opção1_quantidade ()
  valor_total_placas = quantidade_de_placas * 849 # R$849,00 é o valor médio de 1 placa solar.
  print(f"\nVocê gastará {valor_total_placas:.2f} reais na compra das placas.")
  return valor_total_placas


def opção2_mensal () :
  estado = input("Escolha o estado em que você mora (ES - MG - SP - RJ): ").upper()
  tarifa = tarifas (estado)
  consumo_kWh_diario = Consumo ()
  horas = horas_sol (estado)
  
  kWh_pico = consumo_kWh_diario / horas
  quantidade_de_placas = (kWh_pico * 1000) / 335

  EconomiaMensal = 1.60 * tarifa * 30 * quantidade_de_placas
  return EconomiaMensal


def opção2_anual () :
  EconomiaMensal =  opção2_mensal ()
  EconomiaAnual = EconomiaMensal * 12
  print (f"Você terá uma economia mensal de {EconomiaMensal:.2f} reais e anual de {EconomiaAnual:.2f} reais.")

  return EconomiaAnual











    