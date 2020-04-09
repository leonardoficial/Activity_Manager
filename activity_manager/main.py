import os, sys, json

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


  # CLEAR CONSOLE
  def clear_console(self):
    os.system("clear")


  # MAIN DECORATOR
  def wrapper(func):

      def wrap(self, *args, **kwargs):
          self.clear_console()
          func(self, *args, **kwargs)
          self.calculate()
      return wrap


  # BUILD TEMPLATE
  def build(self, type, export=False):
    time = self.datetime
    data = self.database["activities"]

    temp = self.template.build(type, data, {
      "time": time
    })
    
    if export:
      fname = "Export/{0} {1}.txt".format(type, self.database["today"])
      with open(fname, "w", encoding="utf-8") as txtfile:
        txtfile.write(temp)
    else:
      print(temp)

    
    

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
  @wrapper
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
  @wrapper
  def save_data(self):
    with open("data.json", "w", encoding="utf-8") as jsonfile:
      json.dump(self.database, jsonfile, ensure_ascii=False, indent=4)


if __name__ == "__main__":

  # GET DATA
  with open("data.json", "r") as jsonfile:
    data = json.load(jsonfile)

  # INIT MAIN PROCESS
  main = Main(data, TemplateManager, InputManager)

  # OPTIONS FUNCTION
  def option_add():
      main.add_activity()
      main.save_data()

  def option_help():
      pass

  def option_update():
      arg1 = int(sys.argv[2])
      arg2 = str(sys.argv[3])
      arg3 = str(sys.argv[4])

      main.update_activity(arg1, arg2, arg3)
      main.save_data()
  
  def option_export():
    arg1 = str(sys.argv[2])
    
    main.build(arg1, True)

  options = {
    "--add":    option_add,
    "--help":   option_help,
    "--update": option_update,
    "--export": option_export
  }

  try:
      option = options[sys.argv[1]]()
  except:
      print("OPTION NOT AVAILABLE!")


#main.add_activity()
#main.build("DAILY")
#main.update_activity(3, "desc", "AAAAAAAA")
#main.save_data()
