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
    
    self.calculate()
    
  
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
  
  # CALCULATE ACTIVITY TIME IN MINUTES
  def calculate(self):
    activities = self.database["activities"]
    
    for activity in activities:
    
      # IF ITS NOT DONE, SKIP
      if activity["status"] == "PEND":
        continue
    
      start = datetime.strptime(activity["start"], "%H:%M")
      stop  = datetime.strptime(activity["stop"],  "%H:%M")
      
      # UPDATE EACH ACTICITY WITH ITS WORK TIME  
      activity["minutes"] = ( (abs(stop - start)).seconds / 60 )
      
  
  # ADD NEW ACTIVITY
  def add_activity(self):
    activities = self.database["activities"]
    activity   = self.sysinput.get_activity()
    
    activity.update({
      "id": len(activities) + 1
    })
    
    activities.append(activity)
  
  # CHANGE EXISTING ACTIVITY
  def update_activity(self, activity_id, key, value):
    activities = self.database["activities"]
    
    for activity in activities:
      if activity["id"] == activity_id:
        activity[key] = value
  
  # EXPORT DATA
  def save_data(self):
    with open("Export/data.json", "w", encoding="utf-8") as jsonfile:
      json.dump(self.database, jsonfile, ensure_ascii=False, indent=4)




# ROUTINE DATA
with open("data.json", "r") as jsonfile:
  data = json.load(jsonfile)

# INIT MAIN PROCESS
main = Main(data, TemplateManager, InputManager)


main.add_activity()

#main.build("DAILY")

#main.update_activity(3, "desc", "AAAAAAAA")

main.save_data()

