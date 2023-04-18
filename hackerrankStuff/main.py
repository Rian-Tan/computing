'''
a = []
while True:
    b = input()
    if b != "":
        a.append(b)
    else:
        break
print(a)
'''
'''
while True:
    (lambda password1: (lambda password2: ((print("Valid"), exit()) if password1 == password2 else print(),))(input()))(input())
'''
'''
a =0 
while True:
    b = int(input())
    a = a +b if b > 0 else (print(a), exit())
'''
'''
a = input()
for i in range(len(a)):
    print(a[0:i+1])
'''
'''
print(f"e detected\nNumber of e's: {s.count('e')}"if"e"in(s:=input().lower())else"e not detected")
'''

list = [106, 185, 147, 74, 14, 166, 105]
smallest = list[0]
for i in list:
    if i < smallest:
        smallest = i
    else: 
        pass
print(smallest)

#smallest = list[0]
#(lambda list: [[print(smallest), globals().__setitem__("smallest", i)] if i < smallest else None for i in list])([106, 185, 147, 74, 14, 166, 105])
