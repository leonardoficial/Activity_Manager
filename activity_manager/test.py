import sys

options = {
    "--help":    "GET HELP",
    "--add":     "ADD ACTIVITY",
    "--update":  "UPDATE ACTIVITY",
}

try:
    option = options[sys.argv[1]]
    print(option)
except:
    print("OPTION NOT AVAILABLE!")
