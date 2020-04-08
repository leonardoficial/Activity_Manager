import json, re

class InputManager(object):
  
  def __init__(self):
    pass
  
  def get_activity(self):
    
    comp  = input("Empresa: ")
    type  = input("Tipo de operação: ")
    start = input("Horário de início: ")
    stop  = input("Horário de término: ")
    desc  = input("Atividade realizada: ")
    
    # If status equals PEND, system cannot do any time calculation
    # This behavior avoids negative time or unexpected results
    status = "PEND"
    
    # TIME TEST
    
    start_test1 = re.match("\d\d:\d\d", start)
    stop_test1  = re.match("\d\d:\d\d", stop)
      
    if start_test1 and stop_test1:
      status = "OKAY"
    
    
    return {
      "type":    type,
      "desc":    desc,
      "status":  status,
      "start":   start,
      "stop":    stop,
      "company": comp
    }