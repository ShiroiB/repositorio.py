import random
n1=int (input('''digite :
    0 para pedra
    1 para papel
    2 para tesoura\n'''))

n2=0
n3=1
n4=2

n5 = random.choice([n2,n3,n4])

print('JOKENNPOOO!!!!!!!')
if n5==0:
    if n1==0:
        print('vc jogou pedra e a cpu jogou pedra')
        print('EMPATE')
    if n1==1:
        print('vc jogou papel e a cpu jogou papel')
        print('VC VENCEU')
    if n1==2:
        print('vc jogou tesoura e a cpu jogou pedra')
        print('A CPU VENCEU')
                
elif n5==1:
    if n1==0:
        print('vc jogou pedra e A CPU jogou papel ')
        print('A CPU VENCEU')
    if n1==1:
        print('vc jogou papel e a cpu jogou papel ')
        print('EMPATE')
    if n1==2:
        print('vc jogou tesoura e A cpu jogou papel' )
        print('VC VENCEU')
elif n5==2:
    if n1==0:
        print('vc jogou pedra e a CPU jogou tesoura ')
        print('VC VENCEU')    
    if n1==1:
        print('vc jogou papel e a cpu jogou tesoura ')
        print('A CPU VENCEU') 
    if n1==2:
        print('vc jogou tesoura e a cpu jogou tesoura')
        print('EMPATE')

