# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def genpass():
  ###Generates a random password
  password_list = []
  new_password = ''
  nr_letters = random.randint(8,10)
  nr_numbers = random.randint(2,4)
  nr_symbols = random.randint(2,4)
  for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

  for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

  for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

  print(password_list)
  random.shuffle(password_list)
  print(password_list)

  for char in password_list:
    new_password += char
  gen_password.delete(0,END)
  gen_password.insert(END,  string=f'{new_password}')
  pyperclip.copy(new_password)      #Copies to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
  #Saves password information to a doc called 'Password Saves.txt'
  save_website = str(website_answer.get())
  save_username = str(user_answer.get())
  save_password = str(gen_password.get())
  websites = {save_website: {"Username": save_username, "Password": save_password}}
  is_ok = messagebox.askokcancel(title=save_website, message=f"Is this info correct?:\nWebsite: {save_website} " f"\nUsername: {save_username}" f"\nPassword: {save_password}")
  if is_ok is True and (len(save_password) != 0 and len(save_username) != 0 and len(save_website) != 
 0):
    try:
      with open('Password Saves.json', 'r') as passFile:
        password_data = json.load(passFile)
    except FileNotFoundError:
      with open('Password Saves.json', 'w') as passFile:
        json.dump(websites, passFile, indent=4)
    else:
      password_data.update(websites)
      with open('Password Saves.json', 'w') as passFile:
        json.dump(password_data, passFile, indent=4)
    finally:
      gen_password.delete(0,END)
      user_answer.delete(0,END)
      website_answer.delete(0,END)
  elif is_ok == False:
    pass
  else:
    messagebox.showinfo(title="Missing Input", message='Please be sure to fill all fields')
  
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 20, pady = 20)
canvas = Canvas(height = 175, width =210 )
logo = PhotoImage(file='logo.png')
canvas.create_image(150,100, image=logo)
canvas.grid(column=1,row=0)
website = Label(text="Website:")
website.grid(column=0,row=1)
website_answer = Entry(width=35)
website_answer.grid(column=1,row=1,columnspan=2)
user = Label(text='Email/Username:')
user_answer = Entry(width=35)
user.grid(column=0,row=2)
user_answer.grid(column=1,row=2,columnspan=2)
password = Label(text='Password:')
gen_password = Entry(width=21)
password.grid(column=0,row=3)
gen_password.grid(column=1,row=3)
passgen = Button(text='Generate Password', command=genpass,width=12)
passgen.grid(column=2,row=3)
add = Button(text='Add', command=save, width=36)
add.grid(column=1,row=4,columnspan=2)
window.mainloop()