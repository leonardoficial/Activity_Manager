

class TemplateManager(object):

    def __init__(self):
        pass

    def build(self, type, activities, config):
      # TEMPLATE HEADER
      result = TEMPLATES["DAILY"]["START"]
      
      for data in activities:
        # TEMPLATE DATA
        vector =  (data["status"], data["company"], data["desc"])
        result += TEMPLATES["DAILY"]["DATA"].format(*vector)
      
      #TEMPLATE FOOTER
      result += TEMPLATES["DAILY"]["STOP"]
      
      print(result)
      


TEMPLATES = {
    "DAILY": {
        "START": "+" + ("-" * 6) + "+" + ("-" * 44) + "+",
        "DATA":  "\n| {0} | {1} - {2}",
        "STOP":  "\n+" + ("-" * 6) + "+" + ("-" * 44) + "+",
        
        "FNAME": ["DIÁRIO - {0}.txt", "ddmmyy"]
    }
}