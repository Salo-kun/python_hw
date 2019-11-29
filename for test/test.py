from tkinter import *


root = Tk()
root.geometry('800x600')
root.title('Black Jack on Python')
c = Canvas(root, bg='springgreen4')
c.pack(fill = BOTH, expand = 1)
card_x = 220
card_y = 20
player_card_x = 220
player_card_y = 220
bank = 2000
card_value = 'A♠'
output_text = 'Press Stand to start game'
stand = Button(root, text = 'Stand').place(x=220, y= 500, width = 180, height = 80)
hit = Button(root, text = 'Hit').place(x=420, y= 500, width = 180, height = 80)
money = Label(root, text = 'Bank: {}'.format(bank), bg ='springgreen4', font = ('arial2',25)).place(x = 20, y = 500 )
Label(root, text = 'Player', bg ='springgreen4', font = ('arial2',25)).place(x = 20, y = 220)
Label(root, text = 'Dealer', bg = 'springgreen4', font = ('arial2',25)).place(x = 20, y = 20)
dealer_score = Label(root, text = player.hand.get_value)

output = Label(root, text = output_text, bg = 'springgreen4', font = ('arial2',20)).place(x = 220, y = 420)
dealer_card = Label(root, text = card_value).place(x = card_x, y = card_y, width = 50, height = 80)
player_card = Label(root, text = card_value).place(x = player_card_x, y = player_card_y, width = 50, height = 80)

root.mainloop()