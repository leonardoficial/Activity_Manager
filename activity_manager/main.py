import os, json

from copy     import deepcopy
from datetime import datetime

from inputManager    import InputManager
from templateManager import TemplateManager


class Main(object):
  
  def __init__(self, data, TemplateManager, InputManager):
  
    # DEVELOPMENT VERSION
    self.version  = "DEV 1.0"
    # INPUT COLLECTOR
    self.sysinput = InputManager()
    # TEMPLATE BUILDER
    self.template = TemplateManager()
    # FULL DATABASE
    self.database = deepcopy(data)
    # CURRENT TIME
    self.datetime = datetime.today().strftime("%d-%m-%Y")
    
  
  # PRINT SYSTEM DATA
  def test(self):
    print(json.dumps(self.database, indent=2))
  
  # BUILD TEMPLATE
  def build(self, type):
    time = self.datetime
    data = self.database["activities"]
  
    self.template.build(type, data, {
      "time": time
    })
  
  # ADD NEW ACTIVITY
  def add_activity(self):
    activity = self.sysinput.get_activity()
    
    self.database["activities"].append(activity)
  
  # CHANGE EXISTING ACTIVITY
  def update_activity(self, activity_id, key, value):
    activities = self.database["activities"]
    
    for activity in activities:
      if activity["id"] == activity_id:
        activity[key] = value




# ROUTINE DATA
with open("data.json", "r") as jsonfile:
  data = json.load(jsonfile)

# INIT MAIN PROCESS
main = Main(data, TemplateManager, InputManager)


#main.add_activity()

main.build("DAILY")

main.update_activity(3, "desc", "AAAAAAAA")

main.build("DAILY")


