def voto(ano):
    from datetime import datetime
    if ano+18 <= int(str(datetime.now()).split('-')[0]) and ano+65 >= int(str(datetime.now()).split('-')[0]):
        return f"Você tem {int(str(datetime.now()).split('-')[0]) - ano}, Voto obrigatório"
    elif ano+16 <= int(str(datetime.now()).split('-')[0]) or ano +65 <= int(str(datetime.now()).split('-')[0]):
        return f"Você tem {int(str(datetime.now()).split('-')[0]) - ano}, Voto opcional"
    else:
        return f"Você tem {int(str(datetime.now()).split('-')[0]) - ano}, Voto negado"


print(voto(int(input('Em que ano vocẽ nasceu? '))))
