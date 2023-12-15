verdade = True
falso = False

print(type(verdade), type(falso))

if falso == False:
    print("A variavel é falso", type(falso))
    while falso == False:
        print("Agora falso vai ser true")
        falso == True
        break
if falso == True:
    print("Agora falso é true")