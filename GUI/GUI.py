####################### Importing packages ####################### 
import tkinter as tk
import customtkinter
import colorsys
from pyparsing import null_debug_action

import tensorflow
from keras import preprocessing
from keras.models import model_from_json
from keras.utils import np_utils
import json
from keras_preprocessing.text import tokenizer_from_json
import pylab as plt
import numpy as np

####################### Loading the model ####################### 
with open('model/tokenizer.json') as f:
    data = json.load(f)
    t = tokenizer_from_json(data)

# load json and create model
json_file = open('model/RNN_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
# load weights into new model
model.load_weights('model/RNN_model.h5')

####################### Defining needed methods ####################### 

def scale(n):
    return int(n * 255) 

def predict_color(name):
    name = name.lower()
    tokenized = t.texts_to_sequences([name])
    padded = preprocessing.sequence.pad_sequences(tokenized, maxlen=30)
    one_hot = np_utils.to_categorical(padded, num_classes=28)
    pred = model.predict(np.array(one_hot))[0]
    r, g, b = scale(pred[0]), scale(pred[1]), scale(pred[2])
    return r, g, b

def hex_color(rgb):
    return '#%02x%02x%02x' % tuple(rgb)

def comp_color(rgb):
    return tuple(np.subtract((255, 255, 255) , rgb))

#color schemes methods was obtained from thingsgrow.me blog    

def analog_color(rgb):
    """
    Takes rgb tuple and angle (out of 100) and produces list of analogous colors)
    """
    d= 35
    analogous_list = []
    #set color wheel angle
    d = d /360.0
    #value has to be 0 <span id="mce_SELREST_start" style="overflow:hidden;line-height:0;"></span>&lt; x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, rgb)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #rotate hue by d
    h = [(h+d) % 1 for d in (-d, d)]
    for nh in h:
        new_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(nh, l, s)))
        analogous_list.append(new_rgb)
    return analogous_list

def triadic_color(rgb):
    """
    Takes rgb tuple and produces list of triadic colors.
    """
    #value has to be 0 < x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, rgb)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 120 and 240 degrees
    deg_120_hue = h + (120.0 / 360.0)
    deg_240_hue = h + (240.0 / 360.0)
    #convert to rgb
    color_120_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_120_hue, l, s)))
    color_240_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_240_hue, l, s)))
    return [color_120_rgb, color_240_rgb]


def tetradic_color(val):
    """
    Takes rgb tuple and produces list of tetradic colors.
    """
    #value has to be 0 <span id="mce_SELREST_start" style="overflow:hidden;line-height:0;"></span>&lt; x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 120 and 240 degrees
    deg_60_hue = h + (60.0 / 360.0)
    deg_180_hue = h + (180.0 / 360.0)
    deg_240_hue = h + (240.0 / 360.0)
    #convert to rgb
    color_60_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_60_hue, l, s)))
    color_180_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_180_hue, l, s)))
    color_240_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_240_hue, l, s)))
    return [color_60_rgb, color_180_rgb, color_240_rgb]
  
####################### building the gui ####################### 

root_tk = tk.Tk()
root_tk.geometry("800x600")
root_tk.title("Color Palette Generator")

frame = customtkinter.CTkFrame(master=root_tk,
                           width=700,
                           height=250,
                           fg_color='#cfcfcf',
                           corner_radius=10)
frame.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

frame = customtkinter.CTkFrame(master=root_tk,
                           width=700,
                           height=250,
                           fg_color='#cfcfcf',
                           corner_radius=10)
frame.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

label = customtkinter.CTkLabel(master=root_tk,
                               text="Enter your Words Here",
                               width=120,
                               height=25,
                               fg_color='#cfcfcf',
                               bg_color='#cfcfcf',
                               corner_radius=8)
label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

entry = customtkinter.CTkEntry(master=root_tk,
                               placeholder_text="",
                               width=120,
                               height=25,
                               bg_color='#cfcfcf',
                               corner_radius=10)
entry.place(relx=0.5, rely=0.15, anchor=tk.CENTER)


'''radio_one = customtkinter.CTkCheckBox(master=root_tk,
                                     text="Solid")
radio_one.place(relx=0.1, rely=0.6, anchor=tk.CENTER)'''

checkBox_comp = customtkinter.CTkCheckBox(master=root_tk,
                                     text="Complimentary",
                                     bg_color='#cfcfcf')
checkBox_comp.place(relx=0.2, rely=0.25, anchor=tk.CENTER)

checkBox_ana = customtkinter.CTkCheckBox(master=root_tk,
                                     text="Analogous",
                                     bg_color='#cfcfcf')
checkBox_ana.place(relx=0.4, rely=0.25, anchor=tk.CENTER)

checkBox_tri = customtkinter.CTkCheckBox(master=root_tk,
                                     text="Triadic",
                                     bg_color='#cfcfcf')
checkBox_tri.place(relx=0.6, rely=0.25, anchor=tk.CENTER)

checkBox_tet = customtkinter.CTkCheckBox(master=root_tk,
                                     text="Tetradic",
                                     bg_color='#cfcfcf')
checkBox_tet.place(relx=0.8, rely=0.25, anchor=tk.CENTER)


####################### Event ####################### 

def button_event():
    words = entry.get()
    color=predict_color(words)
    
    frame = customtkinter.CTkFrame(master=root_tk,
                               width=700,
                               height=250,
                               fg_color='#cfcfcf',
                               corner_radius=10)
    frame.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    
    frame = customtkinter.CTkFrame(master=root_tk,
                               width=100,
                               height=100,
                               fg_color = hex_color(color),
                               bg_color='#cfcfcf',
                               corner_radius=10)
    frame.place(relx=0.2, rely=0.75, anchor=tk.CENTER)

    if checkBox_comp.get():
        frame = customtkinter.CTkFrame(master=root_tk,
                                width=100,
                                height=100,
                                fg_color = hex_color(comp_color(color)),
                                bg_color='#cfcfcf',
                                corner_radius=10)
        frame.place(relx=0.4, rely=0.75, anchor=tk.CENTER)

    elif checkBox_ana.get():
        frame = customtkinter.CTkFrame(master=root_tk,
                                width=100,
                                height=100,
                                fg_color = hex_color(analog_color(color)[0]),
                                bg_color='#cfcfcf',
                                corner_radius=10)
        frame.place(relx=0.4, rely=0.75, anchor=tk.CENTER)

        frame = customtkinter.CTkFrame(master=root_tk,
                                width=100,
                                height=100,
                                fg_color = hex_color(analog_color(color)[1]),
                                bg_color='#cfcfcf',
                                corner_radius=10)
        frame.place(relx=0.6, rely=0.75, anchor=tk.CENTER)

    elif checkBox_tri.get():
        frame = customtkinter.CTkFrame(master=root_tk,
                                width=100,
                                height=100,
                                fg_color = hex_color(triadic_color(color)[0]),
                                bg_color='#cfcfcf',
                                corner_radius=10)
        frame.place(relx=0.4, rely=0.75, anchor=tk.CENTER)

        frame = customtkinter.CTkFrame(master=root_tk,
                                width=100,
                                height=100,
                                fg_color = hex_color(triadic_color(color)[1]),
                                bg_color='#cfcfcf',
                                corner_radius=10)
        frame.place(relx=0.6, rely=0.75, anchor=tk.CENTER)

    elif checkBox_tet.get():
        frame = customtkinter.CTkFrame(master=root_tk,
                                width=100,
                                height=100,
                                fg_color = hex_color(tetradic_color(color)[0]),
                                bg_color='#cfcfcf',
                                corner_radius=10)
        frame.place(relx=0.4, rely=0.75, anchor=tk.CENTER)

        frame = customtkinter.CTkFrame(master=root_tk,
                                width=100,
                                height=100,
                                fg_color = hex_color(tetradic_color(color)[1]),
                                bg_color='#cfcfcf',
                                corner_radius=10)
        frame.place(relx=0.6, rely=0.75, anchor=tk.CENTER)

        frame = customtkinter.CTkFrame(master=root_tk,
                                width=100,
                                height=100,
                                fg_color = hex_color(tetradic_color(color)[2]),
                                bg_color='#cfcfcf',
                                corner_radius=10)
        frame.place(relx=0.8, rely=0.75, anchor=tk.CENTER)




button = customtkinter.CTkButton(master=root_tk,
                                 fg_color=("darkgray", "lightgray"),  # <- tuple color for light and dark theme
                                 text="Generate Colors!",
                                 bg_color='#cfcfcf',
                                 command=button_event)
button.place(relx=0.5, rely=0.35, anchor=tk.CENTER)


customtkinter.set_appearance_mode("System") # Other: "Light", "System"
customtkinter.set_default_color_theme("dark-blue") 
root_tk.resizable(False, False)

root_tk.mainloop()
