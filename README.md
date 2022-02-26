# ColorPaletteGenerator
This is the capstone project of MISK Data Science Immersive course. It is a program that will generate a color palette for the user depending on colors data and color theory, the user input will be in the format of a single word. I'll keep updating this repo with my progress till the project is fully implemented. 

### Current status of the project
<strike>I'm currently working on exploring the possible data sets that I can use, I have 3 options to choose from:
 
 1. Palette-and-Text (PAT) dataset collected for the [Text2Color](https://github.com/awesome-davian/Text2Colors) project.
 2. Improving the [color terms dataset](https://www.kaggle.com/rtatman/color-terms-dataset) by scrapping more labels from text and article that describe colors in words.
 3. Using Image processing to obtain colors from images that is related to the used word, for this I think of using [Unsplash API](https://unsplash.com/developers).
 
I want to test each approach, I'll update the repo with my experiments and decision before moving to the next step.</strike> 19/2/2022

The dataset is ready, I decided to go with PAT dataset, is contains around 10k entries of single words and sentences, and a color pallet for each entry (from 1 to 5 colors). Next step exploring this data, ensuring that everything is correct and trying to visualize the colors which are in (r,g,b) format.
I'm planning to split the entences  into single words, this will increase my dataset while keeping the colors relative to the word itself. I'll try and ignore the common words such as "the, of, I, etc." when splitting.22/2/2022

### About the Dataset
Palette-and-Text (PAT) is a dataset collected by a research team from Korea University and Hong Kong University of Science and Technology. It contains words and a color palette that represent these words, you can read more about their research [here](https://arxiv.org/abs/1804.04128). From the repository of their project, [Text2Color](https://github.com/awesome-davian/Text2Colors), the data can be found in the format of .pkl files. The data was split into a train and test sets. I loaded the .pkl files into panda dataframes and saved them into .csv format. The data contains a total of 10184 entries.


