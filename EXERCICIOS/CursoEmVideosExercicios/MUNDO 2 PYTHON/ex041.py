#categoria
from datetime import date
ano = int(input('Qual seu ano de nascimento: '))

print('\033[1;36mVOCÊ TEM: {} anos \033[m '.format(date.today().year - ano))
print('\033[1;36mLISTA DE CATEGORIA: \033[m ')
if ano < 9:
    ano = date.today().year
    print('\033[1;31mCATEGORIA: \033[m\033[1;35mMIRIM\033[m ')
elif 9 <= ano <= 14:
    ano = date.today().year
    print('\033[1;31mCATEGORIA: \033[m\033[1;35mINFANTIL\033[m ')
elif 14 <= ano < 19:
    ano = date.today().year
    print('\033[1;31mCATEGORIA: \033[m\033[1;35mJUNIOR\033[m ')
elif 19 <= ano < 25:
    ano = date.today().year
    print('\033[1;31mCATEGORIA: \033[m\033[1;35mADULTO\033[m ')
elif ano >= 25:
    ano = date.today().year
    print('\033[1;31mCATEGORIA: \033[m\033[1;35mMASTER\033[m ')
