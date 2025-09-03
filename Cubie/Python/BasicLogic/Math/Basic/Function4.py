def FormulaHard():
    x = int(input("Enter x: "))
    w = int(input("Enter w: "))
    z = int(input("Enter z: 5"))
    compile1 = 5*(3*x**2 + 5*x + 2)
    compile2 = 7*w - 1/z
    compile3 = 4*(3+x)/7
    compile4 = (compile1/compile2)-z
    compile5 = compile4 /compile3
    return print(f"{compile5:.2f}")

FormulaHard()