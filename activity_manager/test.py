import json

from main import Main

from inputManager    import InputManager
from templateManager import TemplateManager

with open("data.json", "r") as jsonfile:
    data = json.load(jsonfile)

main = Main(data, TemplateManager, InputManager)

main.calculate(1)
main.save_data()