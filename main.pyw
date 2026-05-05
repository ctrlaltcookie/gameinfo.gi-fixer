from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.font as tkFont
import re
import os.path

# intiiate tkinter shit
tk_window = Tk()
tk_window.geometry("500x200")
# this is just because its hilarious to have a horrible colour <3
tk_window.config(bg="yellow")

# Define a custom font / so the fucking shit is visibile innit
custom_font = tkFont.Font(family="Arial", size=20)
left = ttk.Label(tk_window, text="click to find and fix gameinfo.gi", font=custom_font)

left.pack()
file_path = False

# get the file name and edit the file
def fileNameCallback():
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
   print("piss")
   tk_window.quit()

# button so cavemen get the file name
file_name_button = Button(
   tk_window, 
   text='''click me 
   (trans rights are human rights)''',
   command=fileNameCallback,
   font=custom_font
)

file_name_button.pack()

tk_window.mainloop()
