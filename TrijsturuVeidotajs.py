from tkinter import*

root=Tk()
root.geometry("700x600")
root.title("Trijstūru veidotājs")
def rekina():
  a=int(ent_a.get())
  b=int(ent_b.get())
  c=int(ent_c.get())
  A = (0, 0)
  B = (c, 0)
  hc = (2 * (a**2*b**2 + b**2*c**2 + c**2*a**2) - (a**4 + b**4 + c**4))**0.5 / (2.*c)
  dx = (b**2 - hc**2)**0.5
  C = (dx, hc)
  cv.delete("all")
  coords = [int((x + 1) * 75) for x in A+B+C]
  cv.create_polygon(*coords, fill="white", outline="black", width=5)
  if a==b and b==c and c==a:
    text="Vienādmalu"
    text2="trījstūris"
    infoText2.config(text=text2)
    infoText.config(text=text)
  elif a==c or a==b or b==c:
    text="Vienādsānu"
    text2="trījstūris"
    infoText2.config(text=text2)
    infoText.config(text=text)
  else:
    text="Dažādmalu"
    text2="trījstūris"
    infoText2.config(text=text2)
    infoText.config(text=text)
    
text = Label(text="Izveido savu trijstūri!", font="Times 20 bold underline")
text.place(x=250,y=20)

info = Label(text="Info:")
info.place(x=35, y=300)
infoText=Label()
infoText.place(x=40, y=320)
infoText2=Label()
infoText2.place(x=40,y=340)

ent_a=Entry(bd= 5, width = 10)
ent_a.place(x=35, y=100)
ent_b=Entry(bd= 5, width = 10)
ent_b.place(x=35, y=150)
ent_c=Entry(bd= 5, width = 10)
ent_c.place(x=35, y=200)

mala1 = Label(text="Mala 1")
mala1.place(x=35, y=80)
mala2 = Label(text="Mala 2")
mala2.place(x=35, y=130)
mala3 = Label(text="Mala 3")
mala3.place(x=35, y=180)

bt1=Button(root, text="Uzzīmēt", command=rekina, bd=5, width=7)
bt1.place(x=35, y=250)

cv=Canvas(root, width=500, height=500, bg="white")
cv.place(x=160,y=60)

root.mainloop()
