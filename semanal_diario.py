from datetime import datetime, timedelta

import pyautogui
import time

Tempo_ini = time.time()
pyautogui.PAUSE = 3

# DETERMINANDO A DATA MENOS UM DIA
data = datetime.today() - timedelta(days=1)
data_hoje = (data.strftime('%d-%m-%Y' + '-00:00:00'))
pyautogui.press("enter")

# Abrir o Mentor PCP
pyautogui.hotkey("win", "r")
pyautogui.write(r"C:\Mentor_PCP\start_mentor_SN.bat")
pyautogui.press("enter")

# Aguardar 60 segundos
time.sleep(40)

# CLICAR E ALTERAR O NOME E DIGITAR A SENHA
pyautogui.click(x=612, y=430)
pyautogui.write("RODRIGOD")
pyautogui.click(x=569, y=477)
pyautogui.write("Rodr160D")
pyautogui.press("enter")
time.sleep(30)
pyautogui.press("enter")


# SELECIONAR O 253
time.sleep(3)
pyautogui.write("RELATORIO_FATURAMENTO_FECHAMENTO")
pyautogui.press("enter")
pyautogui.doubleClick(x=451, y=252)
pyautogui.doubleClick(x=484, y=278)
pyautogui.click(x=517, y=299)
pyautogui.click(x=807, y=401)
pyautogui.write("01")
pyautogui.press("enter")

# GERAR O RELATORIO
pyautogui.click(x=598, y=202)
time.sleep(20)
pyautogui.getWindowsWithTitle('Touch Comp ERP')[0].maximize()
time.sleep(0.5)
pyautogui.getWindowsWithTitle('Touch Comp ERP')[0].minimize()
time.sleep(2)
pyautogui.getWindowsWithTitle('business_inteligence')[0].maximize()

# SALVAR PLANILHA COMO
pyautogui.hotkey("f12")
pyautogui.click(x=586, y=55)
pyautogui.write(r"Z:\005-FINANCEIRO\01-BI_FECH_DIARIO_MENSAL")
pyautogui.press("enter")
pyautogui.click(x=573, y=569)
pyautogui.write("BASE_BI_253_FATURAMENTO.xls")
pyautogui.press("enter")
pyautogui.press("s")
pyautogui.hotkey("alt", "f4")
# FECHAR O MENTOR
pyautogui.hotkey("alt", "f4")
pyautogui.press("enter")

# Abrir o Mentor PCP
pyautogui.hotkey("win", "r")
pyautogui.write(r"C:\Mentor_FISC\start_mentor_SN.bat")
pyautogui.press("enter")
#
# # Aguardar 60 segundos
time.sleep(60)
#
# CLICAR E ALTERAR O NOME E DIGITAR A SENHA
pyautogui.click(x=664, y=433)
pyautogui.write("RODRIGOD")
pyautogui.click(x=582, y=476)
pyautogui.write("Rodr160D")
pyautogui.click(x=656, y=572)
pyautogui.press("enter")

# # SELECIONAR O BI 102
time.sleep(10)
pyautogui.write("102_NOTA_FISCAL_PROPRIA")
pyautogui.press("enter")
pyautogui.doubleClick(x=437, y=267)
pyautogui.doubleClick(x=483, y=293)
pyautogui.click(x=523, y=313)
pyautogui.click(x=808, y=419)
pyautogui.write("01/01/2022")
pyautogui.press("enter")

# # DETERMINANDO A DATA MENOS UM DIA
data = datetime.today() - timedelta(days=1)
pyautogui.write(data.strftime('%d-%m-%Y' + '-00:00:00'))
pyautogui.press("enter")

# # GERAR O RELATORIO
pyautogui.click(x=599, y=213)
time.sleep(20)
pyautogui.getWindowsWithTitle('Touch Comp ERP')[0].maximize()
time.sleep(0.5)
pyautogui.getWindowsWithTitle('Touch Comp ERP')[0].minimize()
time.sleep(2)
pyautogui.getWindowsWithTitle('business_inteligence')[0].maximize()

# # SALVAR PLANILHA COMO
pyautogui.hotkey("f12")
pyautogui.click(x=586, y=55)
pyautogui.write(r"Z:\005-FINANCEIRO\01-BI_FECH_DIARIO_MENSAL")
pyautogui.press("enter")
pyautogui.click(x=529, y=564)
pyautogui.write("BASE_BI_102_NF_PROPRIA.xls")
pyautogui.press("enter")
pyautogui.press("s")
pyautogui.hotkey("alt", "f4")
pyautogui.click(x=76, y=102)
pyautogui.click(x=186, y=50)

# # SELECIONAR O BI 105
time.sleep(10)
pyautogui.write("105_NOTA_FISCAL_TERCEIRO")
pyautogui.press("enter")
pyautogui.doubleClick(x=446, y=265)
pyautogui.doubleClick(x=502, y=288)
pyautogui.click(x=513, y=311)
pyautogui.click(x=801, y=415)
pyautogui.write("01/01/2022")
pyautogui.press("enter")

# DETERMINANDO A DATA MENOS UM DIA
data = datetime.today() - timedelta(days=1)
pyautogui.write(data.strftime('%d-%m-%Y' + '-00:00:00'))
pyautogui.press("enter")

# GERAR O RELATORIO
pyautogui.click(x=596, y=211)
time.sleep(20)
pyautogui.getWindowsWithTitle('Touch Comp ERP')[0].maximize()
time.sleep(0.5)
pyautogui.getWindowsWithTitle('Touch Comp ERP')[0].minimize()
time.sleep(2)
pyautogui.getWindowsWithTitle('business_inteligence')[0].maximize()

# SALVAR PLANILHA COMO
pyautogui.hotkey("f12")
pyautogui.click(x=618, y=46)
pyautogui.write(r"Z:\005-FINANCEIRO\01-BI_FECH_DIARIO_MENSAL")
pyautogui.press("enter")
pyautogui.click(x=587, y=565)
pyautogui.write("BASE_BI_105_NF_TERCEIRO.xls")
pyautogui.press("enter")
pyautogui.press("s")
pyautogui.hotkey("alt", "f4")

# FECHAR O MENTOR
pyautogui.hotkey("alt", "f4")
pyautogui.press("enter")

# ABRIR A PLANNILHA DIARIO
pyautogui.hotkey("win", "r")
pyautogui.write(r"Z:\005-FINANCEIRO\01-BI_FECH_DIARIO_MENSAL\RELATORIO_DIARIO.xlsm")
pyautogui.press("enter")
pyautogui.click(x=541, y=168)
time.sleep(25)
pyautogui.click(x=292, y=239)
pyautogui.press("enter")
pyautogui.press("alt")
pyautogui.press("s")
pyautogui.press("g")
pyautogui.press("z")
pyautogui.click(x=160, y=472)
pyautogui.press("alt")
pyautogui.press("s")
pyautogui.press("g")
pyautogui.press("z")
time.sleep(15)
pyautogui.click(x=1010, y=234)
time.sleep(4)
pyautogui.hotkey("alt", "f4")
pyautogui.hotkey("alt", "f4")
pyautogui.press("l")

Tempo_fin = time.time()


print(int(Tempo_fin - Tempo_ini) / 60)
