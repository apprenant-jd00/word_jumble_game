from tkinter import *
from random import choice
from random import shuffle
from tkinter import messagebox

root = Tk()
root.title('Word Jumble')
root.geometry("600x400")
root['bg']='#AFEEEE'

myLabel = Label(root, text="", font=("Helvetica", 50), bg='#AFEEEE')
myLabel.pack(pady=20)

score = 0
timeleft = 60


def startGame(event):
    if timeleft == 60:
        countdown()
        shuffler()
        scorelabel.config(text="Score: 0")
    else:
        answer()


def countdown():
    global timeleft
    if timeleft == 0:
        messagebox.showinfo("Time Over", "Time is over and your score is " + str(score))
    if timeleft > 0:
        timeleft -= 1
        timelabel.config(text="Time Left: " + str(timeleft))
        timelabel.after(1000, countdown)
    if timeleft <=10:
        timelabel.config(fg='red')



def shuffler():
    eAnswer.delete(0, END)
    ansLabel.after(400, lambda: ansLabel.config(text=''))

    global word
    Countries = ['Egypt', 'Sudan', 'Oman', 'Yemen', 'Syria', 'Algeria', 'Qatar', 'Lebanon', 'Tunisia', 'Libya',
                 'Kuwait', 'Jordan', 'Iraq', 'France', 'Germany', 'Spain', 'China', 'India', 'Canada', 'Brazil',
                 'Italy', 'Poland', 'Sweden', 'Norway', 'Greece', 'Netherlands', 'Japan', 'Iran', 'Portugal', 'Mexico',
                 'Cuba', 'Argentina', 'Colombia']

    word = choice(Countries)

    breakWord = list(word)
    shuffle(breakWord)

    global shuffled
    shuffled = ''
    for letter in breakWord:
        shuffled += letter

    myLabel.config(text=shuffled)


def answer():
    global score
    global timeleft

    if timeleft > 0:
        eAnswer.focus_set()
        if eAnswer.get().lower() == word.lower():
            score += 1
            ansLabel.config(text="Correct! +1", fg='#00A36C')
            timeleft = 60
        else:
            ansLabel.config(text="Incorrect", fg='#D70040')
            timeleft = 60
        scorelabel.config(text="Score: " + str(score))

        shuffler()



scorelabel = Label(root, text="Hit enter to start", font=('Helvetica', 24), fg='green', bg='#AFEEEE')
scorelabel.pack()

timelabel = Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12), bg='#AFEEEE')
timelabel.pack()

eAnswer = Entry(root, font=("Helvetica", 25))
eAnswer.pack(pady=20)

myFrame = Frame(root, bg='#AFEEEE')
myFrame.pack(pady=20)


ansButton = Button(myFrame, text="Answer!", command=answer, padx=15)
ansButton.grid(row=0, column=0, padx=10)

ansLabel = Label(root, text="", font=("Helvetica", 15), bg='#AFEEEE')
ansLabel.pack(pady=20)


root.bind('<Return>', startGame)
eAnswer.focus_set()

root.mainloop()
