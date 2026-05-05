# powered by delicious sweets

from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import filedialog
import tkinter.font as tkFont
import re
import os
import os.path
import zipfile
import patoolib

# intiiate tkinter shit
tk_window = Tk()
tk_window.geometry("800x600")
# this is just because its hilarious to have a horrible colour <3
tk_window.config(bg="blue")

# Define a custom font / so the fucking shit is visibile innit
custom_font = tkFont.Font(family="Arial", size=15)
instructuions = ttk.Label(tk_window, text="this is a small app to do mod managing without all the shit faff", font=custom_font, background="white")

instructuions.pack()
mod_folder_path = False

# get the file name and edit the file
def file_name_callback():
   file_path = filedialog.askopenfilename(
      initialdir="C:\\Program Files (x86)\\Steam\\steamapps\\common\\Deadlock\\game\\citadel\\",
      initialfile="gameinfo.gi"
   )

   with open(file_path, 'r+') as file:
      file_content = file.read()

      if not os.path.exists(file_path+" - copy"):
         file_copy = open(file_path+" - copy", 'w')
         file_copy.write(file_content)
         file_copy.close()
      
      regex_pattern_mod_exists = r"Mod(\s+)core"
      if re.search(regex_pattern_mod_exists, file_content) is None:
         regex_pattern_capture_game_citadel = r"Game(\s+)citadel"
         regex_pattern_capture_game_core = r"Game(\s+)core"
         first_section_replacement = '''
                     Mod                 citadel
                     Write               citadel
                     Game                citadel/addons
                     Game                citadel
                     Mod                 core
                     Write               core'''
         second_section_replacement = '''Game				core
                     AddonRoot           citadel_addons
                     OfficialAddonRoot   citadel_community_addons'''
         first_pass_file_content = re.sub(regex_pattern_capture_game_citadel, first_section_replacement, file_content)
         second_pass_file_content = re.sub(regex_pattern_capture_game_core, second_section_replacement, first_pass_file_content)
         file.seek(0)
         file.write(second_pass_file_content)
         file.truncate()
      file.close()

# button so cavemen get the file name
file_name_button = Button(
   tk_window,
   text='''click me to mod gameinfo''',
   command=file_name_callback,
   font=custom_font
)

file_name_button.pack()

instructuions_two = ttk.Label(tk_window, text="show us where your mods folder is", font=custom_font, background="pink")

instructuions_two.pack()

def mod_folder_callback():
   global mod_folder_path
   mod_folder_path = filedialog.askdirectory(
         initialdir="C:\\mods",
      )

folder_button = Button(
   tk_window,
   text='''click me to find mods folder''',
   command=mod_folder_callback,
   font=custom_font
)

folder_button.pack()

instructuions_three = ttk.Label(tk_window, 
   text='''show us where your addons folder is 
   (shoudl be in Deadlock\\game\\citadel\\addons)''', 
   font=custom_font, 
   background="pink")
instructuions_three.pack()

def addons_mod_folder_callback():
   global mod_folder_path
   addons_folder_path = filedialog.askdirectory(
      initialdir="C:\\Program Files (x86)\\Steam\\steamapps\\common\\Deadlock\\game\\citadel\\addons",
      )
   for zip_file_to_extract in os.scandir(mod_folder_path):
      print(zip_file_to_extract.path)
      patoolib.extract_archive(zip_file_to_extract.path, outdir=addons_folder_path)
   tkinter.messagebox.showinfo("Everything is fine",  "Well done your shit is modded")

addons_folder_button = Button(
   tk_window,
   text='''click me to install mods to addons''',
   command=addons_mod_folder_callback,
   font=custom_font
)

addons_folder_button.pack()

tk_window.mainloop()

# this shit was made by cookie in a single fucking day why are you using AI you fucking hacks
