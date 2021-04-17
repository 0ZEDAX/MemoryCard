from PyQt5.QtCore import Qt #Подключаем Qt.Core для параметра aligment.
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)#Подключаем все нужные виджеты через запятую.
from random import randint, shuffle #Подключаем модуль рандом функцию shuffle
                           #shuffle - перемешивает последовательность (изменяется сама последовательность)
 
class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3,answer):
        #все строки надо задать при создании объекта,они запоминаются в свойства.
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.answer = answer
questions_list=[]
questions_list.append(Question("Кто из президентов США написал свой собственный рассказ про Шерлока Холмса" , 'Франклин Рузвельт', 'Джон Кеннеди', 'Рональд Рейган', 'Дональд Трамп', '32-1 президент США Франклин Рузвельт был известен и как писатель. В 1945 году он попытался воскресить образ\n знаменитого литературного героя, написав сочинение «Бейкер-стрит фолио:\n пять записок о Шерлоке Холмсе от Франклина Делано Рузвельта».'))
questions_list.append(Question("Какую пошлину ввели в XII  веке в Англии для того чтобы заставить мужчин пойти на войну", 'Налог на трусость', 'Налог на тунеядство', 'Налог на отсутствие сапог', 'Налог на наглость','Англичанам приходилось платить налог на трусость. Им облагали всех,\n кто не желал принимать участие в войнах во славу короля.'))
questions_list.append(Question("Откуда пошло выражение «деньги не пахнут»", 'От налога на туалеты', 'От подателей за провоз парфюмерии', 'От сборов за нестиранные носки', 'От Верблюда','Римский император Веспасиан ввел для горожан налог на общественные туалеты.\n Сын не поддержал идею отца. Тогда монарх поднес к носу отпрыска деньги и спросил,\n пахнут ли они. Отсюда произошло выражение.'))
questions_list.append(Question("Туристы, приезжающие на Майорку, обязаны заплатить налог...", 'На солнце', 'На плавки', 'На пальмы', 'На пляжи','Налог на солнце обязаны платить все туристы, которые приезжают на Майорку.\n Плата невысокая, всего 1 евро в день, Власти говорят, то собранные деньги\n тратятся на улучшение туристической инфраструктуры.'))
questions_list.append(Question("Основой для «Сказки о рыбаке и рыбке Пушкина послужила сказка братьев Гримм «Рыбак и его жена».\n В ней немецкая «коллега» нашей старухи превратилась в", 'Папу Римского', 'Королеву', 'Директора рыбзавода', 'Командира отряда водолазов','Героиня сказки братьев Гримм «Рыбак и его жена» превратилась в папу Римского.\n И только после желания стать Господом Богом осталась ни с чем.'))
questions_list.append(Question("Найдите ошибку в отрывке из басни Крылова:\n «Попрыгунья Стрекоза лето красное пропела; оглянуться не успела, как зима катит в глаза»", 'Эти насекомые совсем не издают звуков', 'Стрекозы не умеют прыгать', 'Зимы в тех местах, о которых писал Крылов, нет', 'Здесь нет ошибки, все правильно','Стрекоза совсем не издает звуков, поэтому петь она никак не могла.\n Во времена Крылова «стрекоза» являлось обобщенным названием для нескольких видов насекомых.\n Так что в басне под «попрыгуньей», скорее всего, подразумевается кузнечик.'))
questions_list.append(Question("Российский мультфильм, удостоенный «Оскара», -это...", '«Старик и море»', '«Простоквашино»', '«Винни-Пух»', '«Ну, погоди!»','В 2000 году премию «Оскар» вручили российскому режиссеру, художнику-мультипликатору\n Александру Петрову за лучший короткометражный мультфильм года «Старик и море»,\n снятый по мотивам повести Эрнеста Хемингуэя.'))
questions_list.append(Question("Кто из знаменитых художников за жизнь продал всего одну картину", 'Винсент Ван Гог', 'Пьер Огюст Ренуар', 'Леонардо да Винчи', 'Клод Моне','Единственная проданная при жизни картина Ван Гога -«Красные виноградники в Арле».'))
questions_list.append(Question("Один известный писатель рассказывал, что списал образ старушки-вредины со своей бывшей жены.\n При этом бабулька оказалась удивительно похожей на Коко Шанель. На голове у нее всегда была\n шляпка со складной тульей, благодаря которой она и получила прозвище...", 'Шапокляк', 'Красная Шапочка', 'Мадам Баттерфляй', 'Мадам Кошанель','Правильный ответ - Шапокляк.'))
#questions_list.append(Question("", '', '', '', '',''))

app = QApplication([]) #Создаём приложение. 
btn_OK = QPushButton('Ответить') #Создаём виджет кнопку с надписью "Ответить"
lb_Question = QLabel('Самый сложный вопрос в мире!') #Создаём виджет Текст "Самый сложный вопрос."
 
RadioGroupBox = QGroupBox("Варианты ответов") #Конструктор для создания группы радио кнопок.
                                             #Выделяется визуально!
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2') #Создаём 4 радиокнопки для вариантов ответа.
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup() #Все переключатели объединяем в специальную группу.
RadioGroup.addButton(rbtn_1) #Теперь может быть выбран только один из них.
RadioGroup.addButton(rbtn_2)   
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   #Создаём горизантальную линию в группе.
layout_ans2 = QVBoxLayout()   #Создаём вертикальную линию в группе.
layout_ans3 = QVBoxLayout()   #Создаём вертикальную линию в группе.
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке
 
RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 
 
AnsGroupBox = QGroupBox("Результат теста") #Конструктор для создания группы ответа. Наше 2 окно!
lb_Result = QLabel('прав ты или нет?') #Создаём надпись Результата.
lb_Correct = QLabel('ответ будет тут!') #Создаём надпись Правильного ответа.
 
layout_res = QVBoxLayout()#cоздаём вертикальную линию.
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))#Метод, добавляющий виджет к линии 
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2) 
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout() #создаём горизантальную линию  # вопрос
layout_line2 = QHBoxLayout() #создаём горизантальную линию  # варианты ответов или результат теста
layout_line3 = QHBoxLayout() #создаём горизантальную линию  # кнопка "Ответить"
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter)) #Метод, добавляющий виджет к линии и располагающий по центру.
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()  # скроем панель с ответом, сначала должна быть видна панель вопросов
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # stretch Растянуть виджет (кнопку) 
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)# layout_card.setSpacing(5) # пробелы между содержимым
 
def show_result(): #Функция показывающая результат!(Функция-обработчик,отображающая форму ответа.)
    ''' показать панель ответов '''
    RadioGroupBox.hide() #команда hide скрывает наше 1 окно с вариантами ответа.
    AnsGroupBox.show()  #команда show показывает наше 2 окно с результатом ответа.
    btn_OK.setText('Следующий вопрос') #меняется надпись на кнопке "Ответить" на "Следующий вопрос"
 
def show_question(): #Функция показывающая наше 1 окно с вопросом и 4 ответами.(Функция-обработчик,отображающая форму вопроса.)
    ''' показать панель вопросов '''
    RadioGroupBox.show() #показываем наше 1 окно с вариантами ответов.
    AnsGroupBox.hide() #Скрываем наше 2 окно с результатом ответа.
    btn_OK.setText('Ответить') #Меняем текст на кнопке.
    RadioGroup.setExclusive(False) #Снимаем ограничения для сброса выбора.
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)#Снимаем выбор всех переключателей.
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) #Возвращаем ограничения.
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] #Создадим список переключателей и перемешаем его элементы с помощью shuffle
 
def ask(q: Question): #функция, задающая (отображающая) указанный вопрос.
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers) #Функция из модуля random с её помощью можно перемешать кнопки!
    answers[0].setText(q.right_answer) #Если нажат первый переключатель answer[0], то показать сообщение «Правильно!».
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)#Если нажат любой другой переключатель, то показать сообщение «Неправильно!»
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # вопрос
    lb_Correct.setText(q.answer)  # ответ 
    show_question() #Функция показывающая наше 1 окно с вопросом и 4 ответами.(Функция-обработчик,отображающая форму вопроса.)
 
def show_correct(res):#Отображаем форму ответа с правильным ответом и пометкой res («Правильно»/«Неправильно»).
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()#Показать функцию 
 
def check_answer():#Проверяем ответ. Если нажат переключатель answer[0], то ответ верный. Если любой другой –– неверный. Вызываем show_correct(), передавая строку с результатом
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():#Метод переключателя .isChecked() проверяет, нажат ли он.
        show_correct('Правильно!')#выводит слово Правильно!
        window.score+=1
        print('Статистика\n-Всего вопросов: ', window.total,'\n-Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100),'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():#Если нажат любой другой переключатель, то показать сообщение «Неправильно!»
            show_correct('Неверно!')#Неверно!
            print('Рейтинг: ', (window.score/window.total*100),'%')
def next_question():
    '''Задаё следующий вопрос из списка'''
    window.total +=1 #прибавляем единицу.
    print('Статистика\n-Всего вопросов: ', window.total,'\n-Правильных ответов: ', window.score)
    cur_question = randint(0, len(questions_list)-1)
    q=questions_list[cur_question]#взяли вопрос.
    ask(q)

def click_OK():
    #определяет,надо ли показывать другой вопрос либо проверить ответ на этот
    if btn_OK.text() == "Ответить":
        check_answer()#Проверка ответа.
    else:
        next_question()#Следующий вопрос.

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
btn_OK.clicked.connect(click_OK) # когда пользователь жмёт на кнопку срабатывает функция.
window.score=0
window.total=0
next_question()

window.show()
window.resize(700,500)
app.exec() #Команда для работы программы пока пользователь не нажмет на крестик.