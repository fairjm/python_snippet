import re
code  = """
  `name` varchar(10) DEFAULT NULL',
  `age` int NOT NULL DEFAULT ''
"""

def parse_field_name(s):
    return re.sub(r"_(.)", lambda x: x.group(1).upper(), s.replace("`",""))

def parse_field_type(t):
    tl = t.lower()
    if  t.startswith("int"):
        return "Long"
    elif t.startswith("varchar"):
        return "String"
    elif t.startswith("timestamp"):
        return "Timestamp"
    return t

lines = [(parse_field_name(a.split()[0]), parse_field_type(a.split()[1])) for a in code.splitlines() if len(a.strip()) > 0]

for name,type in lines:
    print("private {0} {1};".format(type, name))
