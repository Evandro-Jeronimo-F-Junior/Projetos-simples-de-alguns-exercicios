def maior(* a):
    if a == ():
        print(f"Foram informados {0} valores ao todo.\nO maior não existe")
    else:
        b = 0
        for i in a:
            if i == 0:
                b = i
            else:
                if i > b:
                    b = i
        print("analisando os valores passados...")
        for i, y in enumerate(a):
            print(y, end=', ')
        print(f"Foram informados {i+1} valores ao todo.\nO maior é {b}")


maior(1, 5)
