import json

class Main(object):
  
  def __init__(self, version, default):
  
    self.version  = version
    self.database = default
    
    
  def test(self):
    print(self.version)
    print(json.dumps(self.database, indent=2))




foo = Main("DEV 1.0", {
  "name": None,
      
  "today":   None,
  "weekday": None,
      
  "clockIn":  None,
  "clockOut": None,
      
  "restBreakIn":  None,
  "restBreakOut": None,
      
  "activities": [
    {
      "type":  "Suporte Técnico",
      "desc":  "Validadores da Rio Ouro não comunicam",
      "start": "11:00",
      "stop":  "12:30",
      "minutes":  None,
      "ststus":   True,
    }
  ]
})

foo.test()