#distancia viagem em km
import emoji

dis = float(input('Qual a distancia de sua viagem: '))
print('Você vai iniciar uma viagem de {}km.'.format(dis))
if dis <= 200:
    pres = dis*0.50
    print('O valor da sua viagem irá ficar R${:.2f}!'.format(pres))
else:
    pres = dis*0.45
    print('O valor da sua viagem irá ficar R${:.2f}!'.format(pres))
print(emoji.emojize('Tenha uma ótima viagem :smiling_face_with_open_hands:'))
