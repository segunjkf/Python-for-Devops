import re

cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,
 ...: Rostam Batmanglij <rostam@vpwk.com>,
 ...: Chris Tomson <ctomson@vpwk.com,
 ...: Bobbi Baio <bbaio@vpwk.com'''
'''
matched = re.search(r'(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)', cc_list)
matched.group("name")
print(f"""name:{matched.group("name")} 
secondry level domain: {matched.group("SLD")}
Top Level Domian: {matched.group("TLD")}""")


#find all

matched = re.findall(r'\w+\@\w+\.\w+', cc_list)
matched2 = re.findall(r"(\w+)\@(\w+)\.(\w+)", cc_list)
print(matched)
print(matched2)

names = [x[0] for x in matched2]
print(names)

#find iterator
matched3 = re.finditer(r'\w+\@\w+\.\w+', cc_list)
print(matched3)
match = next(matched3)
print(match)
match4 = next(matched3)
print(match4)
#find match and group
match = re.finditer('(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)', cc_list)
print(match)
for m in match:
    print(m.groupdict())
'''
#substitution
#segun = re.sub('\d', '#', "The password you have enter was 098867")
#print(segun)

#regex = re.compile(r'\w+\@\w+\.\w+')
#segun = regex.search(cc_list)
#print(segun)

def fib():
    first =  0
    last = 1
    while True:
        first,last = last, first + last
        yield first
f = fib()

for x in f:
    print(x)
    if x > 12:
        break
list_o_nums = (x for x in range(100))

print(list_o_nums)
