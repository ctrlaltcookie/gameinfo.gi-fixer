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
tk_window.title("Stimmy the SDMI")
tk_window.geometry("800x600")
# this is just because its hilarious to have a horrible colour <3
tk_window.config(bg="white")

# Define a custom font / so the fucking shit is visible innit
custom_font = tkFont.Font(family="Arial", size=15)

instructions = ttk.Label(tk_window, text="Tell us where your steam installation is!", font=custom_font, background="light blue")
instructions.pack()

mod_folder_path = False
steam_folder_path = False
steamapps_folder_path = os.path.join("steamapps","common","Deadlock","game","citadel")

def steam_folder_locator():
      global steam_folder_path
      steam_folder_path = filedialog.askdirectory(
         initialdir="C:\\Program Files (x86)\\Steam\\",
      )

steam_path_button = Button(
   tk_window,
   text='''Locate Steam Install!''',
   command=steam_folder_locator,
   font=custom_font
)

steam_path_button.pack()

# get the gameinfo location and edit it
def edit_game_info():
   global steam_folder_path
   file_path = os.path.join(steam_folder_path, steamapps_folder_path, "gameinfo.gi")

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

instructions_two = ttk.Label(tk_window, text="Tell us where your mods folder is!", font=custom_font, background="pink")
instructions_two.pack()

def mod_folder_locator():
   global mod_folder_path
   mod_folder_path = filedialog.askdirectory(
         initialdir="C:\\mods",
      )

mod_folder_locator_button = Button(
   tk_window,
   text='''Locate Mods Folder!''',
   command=mod_folder_locator,
   font=custom_font
)
mod_folder_locator_button.pack()

def unpack_mods_to_addons_folder():
   global mod_folder_path

   addons_folder_path = os.path.join(steam_folder_path, steamapps_folder_path, "addons")

   for zip_file_to_extract in os.scandir(mod_folder_path):
      print(zip_file_to_extract.path)
      patoolib.extract_archive(zip_file_to_extract.path, outdir=addons_folder_path)
   tkinter.messagebox.showinfo("Update!",  "Mods installed! You can close the program now.")

def install_mods_and_edit_gameinfo():
   edit_game_info()
   unpack_mods_to_addons_folder()

install_mods_and_edit_gameinfo_button = Button(
   tk_window,
   text='''Install Mods!''',
   command=install_mods_and_edit_gameinfo,
   font=custom_font
)
install_mods_and_edit_gameinfo_button.pack()

tk_window.mainloop()

# Made by cookie in 2 days okay maybe this is harder than i thought
