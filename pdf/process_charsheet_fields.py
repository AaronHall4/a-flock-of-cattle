import re

fields_file = open("character_sheet_fields.txt","r")
lines = fields_file.readlines()
count = 1
for i in range(len(lines)):
    if lines[i].rstrip() == "FieldType: Text":
        attr_line = lines[i + 1].strip("\n")
        match = re.search("FieldName: (.*)", attr_line)
        if match:
            print("          ('" + match.group(1) + "','Hello" + str(count) + "'),")
            count = count + 1
