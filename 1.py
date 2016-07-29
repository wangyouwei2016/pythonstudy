"""
#隐藏号码位
phone_number = '1386-666-0006'
hiding_number = phone_number.replace(phone_number[:9],'*' * 9)
print(hiding_number)
#重量转换
c = int(input('Enter a weigth''(g):'))
def weight_converter(c):
    weight = c/1000
    return (str(weight)+ 'KG')
print(weight_converter(c))

file = open(r"e:\1.txt",'w')
file.write("WangYouwei")

def text_create(name, msg):
    desktop_path = 'E:'
    full_path = desktop_path + name + '.txt'
    file = open(full_path,'w')
    file.write(msg)
    file.close()
    print('Done')
text_create('hello','hello world') # 调用函数

#密码登录更换密码
password_list = ['333','12345']
def account_login():
    password = input('Password:')
    password_correct = password == password_list[-1]
    password_reset = password == password_list[0]
    if password_correct:
        print('Login success!')
    elif password_reset:
        new_password = input('Enter a new password:')
        password_list.append(new_password)
        print('Your password has changed successfully!')
        account_login()
    else:
        print('Wrong password or invalid input!')
        account_login()
account_login()
"""

"""
songslist = ['Holy Diver', 'Thunderstruck', 'Rebel Rebel']
for song in songslist:
    if song == 'Holy Diver':
        print(song,' - Dio')
    elif song == 'Thunderstruck':
        print(song,' - AC/DC')
    elif song == 'Rebel Rebel':
        print(song,' - David Bowie')

for i in range(1,10):
    for j in range(1,10):
        print('{} X {} = {}'.format(i,j,i*j))

while 1 < 3:
    print('1 is smaller than 3')
"""
"""
count = 0
while True:
    print('Repeat this line !')
    count = count + 1
    if count == 5:
        break
"""
"""
password_list = ['*#*#','12345']

def account_login():
    tries = 3
    while tries > 0:
        password = input('Password:')
        password_correct = password == password_list[-1]
        password_reset = password == password_list[0]

        if password_correct:
            print('Login success!')
        elif password_reset:
            new_password = input('Enter a new password :')
            password_list.append(new_password)
            print('Password has changed successfully!')
            account_login()
        else:
            print('Wrong password or invalid input!')
            tries = tries - 1
            print( tries, 'times left')

    else:
        print('Your account has been suspended')
account_login()
"""
"""
#以数字名字创建多个文件
def creatfile():
    path = r'e:\\'
    for i in range(1,5):
        with open(path + str(i) + ".txt",'w') as text:
            text.write(str(i))
            text.close()
            print('done')
creatfile()
"""
"""
import random
def roll_dice(numbers=3, points=None):
    print('<<<<< ROLL THE DICE! >>>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers - 1
    return points

def roll_result(total):
    isBig = 11 <= total <=18
    isSmall = 3 <= total <=10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'
def start_game():
    print('<<<<< GAME STARTS! >>>>>')
    choices = ['Big','Small']
    your_choice = input('Big or Small :')
    if your_choice in choices:
        points = roll_dice()
        total = sum(points)
        youWin = your_choice == roll_result(total)
        if youWin:
            print('The points are',points,'You win !')
        else:
            print('The points are',points,'You lose !')
    else:
        print('Invalid Words')
        start_game()
start_game()
"""
# 赌局游戏
import random

def roll_dice(numbers=3,points= None):
    print('#######ROLL THE DICE########')
    if points is None:
        points=[]
    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers - 1
    return points

def roll_result(total):
    isBig = 11 < total <= 17
    isSmall = 4 < total <= 10
    if isBig:
        return  'big'
    elif isSmall:
        return 'small'


def start_game():
    your_money=1000
    while your_money > 0:
        print('#######game start####')
        choices = ['big','small']
        your_choice = input('big or small:')
        if your_choice in choices:
            your_bet=int(input('how much you wanna bet?-'))
            points = roll_dice()
            total = sum(points)
            youwin = your_choice == roll_result(total)
            if youwin:
                print('The points is',points,'you win')
                print('you gaimed{},youhave {} now.'.format(your_bet,your_money + your_bet))
                your_money = your_money + your_bet
            else:
                print('THE POINTS IS',points,'you lose')
                print('you lost{},you have{}now'.format(your_bet,your_money - your_bet))
                your_money = your_money - your_bet
        else:
            print('invalid words')
    else:
        print('game over')
start_game()
