![image](https://user-images.githubusercontent.com/96572809/157335078-6156e25b-e014-4220-95c0-777c6261b108.png)
# Color Palettes Generator Using Keras
This is the capstone project of MISK Data Science Immersive course. It is a ML Model that takes words from the user and generate a color related to these words. The user can use from 4 different color schemes to obtain a color palette. Playing around with colors and palettes are very inspiring to any artist. designer, and programmer. I hope this simple implementation can inspire and help you to create more!

### Dependencies
- Tensorflow
-  Keras
- numpy
- pandas
- tkinter
- customtkinter


### About the Dataset
The used dataset is a combination of two datasets, [keras_colors](https://github.com/Tony607/Keras-Colors) and [Palette-and-Text (PAT)](https://github.com/awesome-davian/Text2Colors) dataset. The cleaning and modification, along with detailed explanation, can be found in the EDA notebook in the data folder.

### About the Model
The used model for color generating is a Recursive Neural Network (RNN) which was Implemented using Keras library. The model is based on the [project of Tony607](https://github.com/Tony607/Keras-Colors) for color generating.

### About the Color Schemes
Four color schemes can be applied using this tool to generate color palettes. The figure below shows the color schemes representation on a simple color wheel. Each color scheme serves a purpose and is suited to use for different goals, a good article that explains color schemes with clear examples can be found [here](https://drawpaintacademy.com/color-schemes/)

![image](https://user-images.githubusercontent.com/96572809/157335180-b52a85a2-698f-4ed8-9be4-c5ce7f864a2a.png)

### About the GUI
The method used to implement the model and make it interactable with users is a simple GUI using tkinter package. A screenshot of the GUI can be found below. To use the GUI, simply install the  dependencies  and run the GUI file inside the GUI folder.

![image](https://user-images.githubusercontent.com/96572809/157335276-4b5980ae-a5d8-4d64-98d6-6ba4fc0032d8.png)


### Refrences

-[Text2Colors](https://github.com/awesome-davian/Text2Colors)

-[Keras Colors](https://www.dlology.com/blog/how-to-train-a-keras-model-to-generate-colors/)

-[Color Theory in Python](https://thingsgrow.me/2020/01/02/navigating-through-000000-and-ffffff-color-theory-in-python/)


