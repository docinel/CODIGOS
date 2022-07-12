import pyautogui as pyt
"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        if not self.find( "mentor", matching=0.97, waiting_time=10000):
            self.not_found("mentor")
        self.click()

        if not self.find( "inicio", matching=0.97, waiting_time=10000):
            self.not_found("inicio")
        self.click_relative(160, 25)
        
        self.paste("BI_264_RELATORIO")
        self.enter(3000)
        
        if not self.find( "filtro", matching=0.97, waiting_time=10000):
            self.not_found("filtro")
        self.double_click()
        
        if not self.find( "juncao", matching=0.97, waiting_time=10000):
            self.not_found("juncao")
        self.double_click()
        
        if not self.find( "data_emissao", matching=0.97, waiting_time=10000):
            self.not_found("data_emissao")
        self.click()
        
        if not self.find( "data_2", matching=0.97, waiting_time=10000):
            self.not_found("data_2")
        self.click_relative(61, 23)
        
        self.paste("31/07/2022-00:00:00")
        
        self.enter(1000)
        
        if not self.find( "gerar_bi", matching=0.97, waiting_time=10000):
            self.not_found("gerar_bi")
        self.click()
        
        if not self.find( "select_A", matching=0.97, waiting_time=20000):
            self.not_found("select_A")
        self.click()
        
        if not self.find( "geral", matching=0.97, waiting_time=10000):
            self.not_found("geral")
        self.click()

        self.paste("d"); self.enter(1000)

        if not self.find( "select_A_2", matching=0.97, waiting_time=10000):
           self.not_found("select_A_2")
        self.click_relative(-8, 44)

        # pyt.keyDown("ctrl")
        # pyt.keyDown("shift")
        # pyt.press("right")
        
        # pyt.keyUp("ctrl")
        # pyt.keyUp("shift")

        pyt.hotkey("ctrl","shift","right")


        



       
       

        
        
        
        

        

        
        


        
        


        
        
        
        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
