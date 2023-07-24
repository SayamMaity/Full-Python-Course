s=set()
s.add(20)
s.add(20.0)#even though it is float but the value is same as 20 so it will take it only once
s.add('20')
print(s)
print(len(s))