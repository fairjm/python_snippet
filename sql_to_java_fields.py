import re
code  = """
  `name` varchar(10) DEFAULT NULL',
  `age` int NOT NULL DEFAULT ''
"""

def parse_field_name(s):
    return re.sub(r"_(.)", lambda x: x.group(1).upper(), s.replace("`",""))

def insert_sql(fields):
    """
    generate mybatis insert sql
    :param fields: column * javaField list
    :return: mybatis insert sql
    """
    r = []
    r.append("INSERT INTO table")
    r.append("(")
    for f,jf in fields:
        r.append(f'\t<if test="{jf} != null">')
        r.append(f"\t\t{f},")
        r.append("\t</if>")
    r.append(")")
    r.append("VALUES")
    r.append("(")
    for f,jf in fields:
        r.append(f'\t<if test="{jf} != null">')
        r.append(f"\t\t#{{{jf}}},")
        r.append("\t</if>")
    r.append(")")
    return "\r\n".join(r)

def update_sql(fields):
    """
    generate mybatis update sql
    :param fields: column * javaField list
    :return:  mybatis update sql
    """
    r = []
    r.append("UPDATE table")
    r.append("<set>")
    for f,jf in fields:
        r.append(f'\t<if test="{jf} != null">')
        r.append(f"\t\t{f}=#{{{jf}}},")
        r.append("\t</if>")
    r.append("</set>")
    return "\r\n".join(r)

def update_sql(fields):
    r = []
    r.append("UPDATE table")
    r.append("<set>")
    for f,jf in fields:
        r.append(f'\t<if test="{jf} != null">')
        r.append(f"\t\t{f}=#{{{jf}}},")
        r.append("\t</if>")
    r.append("</set>")
    return "\r\n".join(r)

  
lines = [(parse_field_name(a.split()[0]), parse_field_type(a.split()[1])) for a in code.splitlines() if len(a.strip()) > 0]

for name,type in lines:
    print("private {0} {1};".format(type, name))
    
fields = [a.split()[0] for a in code.splitlines() if len(a.strip()) > 0]
fields = [(a, parse_field_name(a)) for a in fields]
print("#######################################################")
print(insert_sql(fields))
print("#######################################################")
print(update_sql(fields))
