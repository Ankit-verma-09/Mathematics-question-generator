import random
a=random.randint(10000,99999)
b=random.randint(10000,99999)
c=random.randint(10000,99999)
d=random.randint(10000,99999)
e=random.randint(10000,99999)
operators=['+','-']
ope1=random.choice(operators)
ope2=random.choice(operators)
ope3=random.choice(operators)
ope4=random.choice(operators)
que=f"{a}{ope1}{b}{ope2}{c}{ope3}{d}{ope4}{e}"
inp=int(input(f"calculate the answer of {que}:"))
q=eval(que)
if inp==q:
    print("your answer is correct!!")
else:
    print("your answer is wrong")
    print("correct answer is",q)
