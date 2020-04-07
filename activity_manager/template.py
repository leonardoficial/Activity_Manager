

class Template(object):

    def __init__():
        pass

    def build(type, data):



TEMPLATES = {
    "DAILY": {
        "START": "+" + ("-" * 30) + "+"
        "DATA":  "| {0} - {1} | {2}"
        "STOP":  "+" + ("-" * 30) + "+"
}


temp = Template()

temp.build("DAILY", {
    "activities": [
        {
            "status":  "OK",
            "desc":    "Validadores sem comunicar",
            "company": "VNS AMPARO",
        }
    ]
})
