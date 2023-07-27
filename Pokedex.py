from cProfile import label
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
# from matplotlib import image

#colors
co0 = "#444466" #black
co1 = "#feffff" #white
co2 = "#6f9fbd" #blue
co3 = "#403d3d" #ash

window = Tk()
window.title('Pokedex')
window.geometry('550x510')
window.resizable(width=False, height=False)
window.configure(bg=co1)

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

main_frame = Frame(window, width=500, height=305, bg=co1)
main_frame.grid(row=0, column=0, padx=1, pady=1)

def choose_pokemon(i):
    global i_icon_l, pokemon_image


pok_name = Label(main_frame, text = "Pokemon name", anchor="center", font=("Ivy 20 bold"), fg=co0)
pok_name.place(x=15, y=15)

pok_type = Label(main_frame, text = "Pokemon type", anchor="center", font=("Verdana 10 bold"), fg=co0)
pok_type.place(x=20, y=50)

pok_number = Label(main_frame, text = "Pokemon number", anchor="center", font=("Verdana 13 bold"), fg=co0)
pok_number.place(x=20, y=75)



# pokemon image

pokemon_image = Image.open('Img/pikachu.png')
pokemon_image = pokemon_image.resize((260, 260))
pokemon_image = ImageTk.PhotoImage(pokemon_image)

l_icon_1 = Label(window, image=pokemon_image, bg=co1)
l_icon_1.place(x=60, y=50)

# STATUS-----------------------------------------

pok_status = Label(window, text="Status", font=("Verdana 20"), bg=co1, fg=co0)
pok_status.place(x=15, y=310)

pok_hp = Label(window, text="HP: 35", font=("Verdana 10"), bg=co1, fg=co0)
pok_hp.place(x=20, y=360)

pok_attack = Label(window, text="Attaque: 55", font=("Verdana 10"), bg=co1, fg=co0)
pok_attack.place(x=20, y=385)

pok_defense = Label(window, text="Défense: 40", font=("Verdana 10"), bg=co1, fg=co0)
pok_defense.place(x=20, y=410)

pok_speed = Label(window, text="Vitesse: 90", font=("Verdana 10"), bg=co1, fg=co0)
pok_speed.place(x=20, y=435)

pok_total = Label(window, text="Total: 220", font=("Verdana 10 bold"), bg=co1, fg=co0)
pok_total.place(x=20, y=435)

# SKILLS-----------------------------------------

pok_skill = Label(window, text="Attaques", font=("Verdana 20"), bg=co1, fg=co0)
pok_skill.place(x=180, y=310)

pok_hb_1 = Label(window, text="Eclair", font=("Verdana 10"), bg=co1, fg=co0)
pok_hb_1.place(x=185, y=360)

pok_hb_2 = Label(window, text="Tonnerre", font=("Verdana 10"), bg=co1, fg=co0)
pok_hb_2.place(x=185, y=385)

# Loading all pokemons
# PIKACHU
img_pok_1 = Image.open('Img/profil-pikachu.png')
img_pok_1 = img_pok_1.resize((40, 40))
img_pok_1 = ImageTk.PhotoImage(img_pok_1)

icon_1 = Button(window, text='Pikachu', width=150, image=img_pok_1, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
icon_1.place(x=375, y=10)

# BULBIZARRE
img_pok_2 = Image.open('Img/profil-bulbizarre.png')
img_pok_2 = img_pok_2.resize((40, 40))
img_pok_2 = ImageTk.PhotoImage(img_pok_2)

icon_2 = Button(window, text='Bulbizarre', width=150, image=img_pok_2, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
icon_2.place(x=375, y=65)

# SALAMECHE
img_pok_3 = Image.open('Img/profil-salameche.png')
img_pok_3 = img_pok_3.resize((40, 40))
img_pok_3 = ImageTk.PhotoImage(img_pok_3)

icon_3 = Button(window, text='Salameche', width=150, image=img_pok_3, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
icon_3.place(x=375, y=120)

# LEVIATOR
img_pok_4 = Image.open('Img/profil-leviator.png')
img_pok_4 = img_pok_4.resize((40, 40))
img_pok_4 = ImageTk.PhotoImage(img_pok_4)

icon_4 = Button(window, text='Leviator', width=150, image=img_pok_4, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
icon_4.place(x=375, y=175)

# ECTOPLASMA
img_pok_5 = Image.open('Img/profil-ectoplasma.png')
img_pok_5 = img_pok_5.resize((40, 40))
img_pok_5 = ImageTk.PhotoImage(img_pok_5)

icon_5 = Button(window, text='Ectoplasma', width=150, image=img_pok_5, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
icon_5.place(x=375, y=230)

# DRACOLOSSE
img_pok_6 = Image.open('Img/profil-dracolosse.png')
img_pok_6 = img_pok_6.resize((40, 40))
img_pok_6 = ImageTk.PhotoImage(img_pok_6)

icon_6 = Button(window, text='Dracolosse', width=150, image=img_pok_6, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
icon_6.place(x=375, y=285)

window.mainloop()