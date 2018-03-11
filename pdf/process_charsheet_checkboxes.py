import re

fields_file = open("character_sheet_fields.txt","r")
lines = fields_file.readlines()
for i in range(len(lines)):
    if lines[i].rstrip() == "FieldType: Button":
        attr_line = lines[i + 1].strip("\n")
        match = re.search("Check (.*)", attr_line)
        if match:
            print("          ('" + match.group(0) + "','Yes'),")
