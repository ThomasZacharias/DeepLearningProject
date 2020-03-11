# DeepLearningProject Tel Aviv University
## Overview
The project consists of three parts- 
1. A simple RNN character level language model      (SimpleRNNBasedTranslator)
2. A text style transfer based machine translator   (StyleBasedTranslator)
3. A script generator using StyleGAN                (StyleGANBasedScripter)

### SimpleRNNBasedTranslator
'data' -> folder containing some of the datasets we created.<br/>
'precompiledResults' -> folder containing some of our precompiled results. <br/>
'rnn_char_gen.py' -> python file with RNN model. To run file simply point to the location of relevant dataset and run.<br/>
Dependencies: Python 3, PyTorch 1.3<br/>

### StyleBasedTranslator
'data' -> folder containing some of the datasets we created.<br/>
'precompiledResults' -> folder contains some of our precompiled results.<br/>
'prepLangFile.py' -> python file to convert custom dataset to required format.<br/>
'code' -> folder containg text style transfer codes. Use 'style_transfer.py' to train/test models.<br/>
To train model, create a /StyleBasedTranslator/tmp folder (this will store the model and results) and then go to /StyleBasedTranslator/code folder and run the following:
```bash
python style_transfer.py --train ../data/1000MostCommonWords/language.train --dev ../data/1000MostCommonWords/language.dev --output ../tmp/language.dev --vocab ../tmp/1000MostCommonWords.vocab --model ../tmp/model
```
To extend the language, run the following:
```bash
python style_transfer.py --test ../data/1000MostCommonWords/language.test --output ../1000MostCommonWords/language.test --vocab ../tmp/1000MostCommonWords.vocab --model ../tmp/model --load_model true --beam 8
```
Dependencies: Python 3, Tensorflow 1.9

### StyleGANBasedScripter
'dataGenerator'-> contains python file 'createCharacters.py' to generate images of Unicode characters. <br/>
'characterGAN' -> contains StyleGAN files with the datasets we creted<br/>
Once images are generated using 'createCharacters.py', save them to folder custom-images and use 'dataset_tool.py' to convert them to the format that StyleGAN requires: <br/>
```bash
python dataset_tool.py create_from_images charImageStyleFormat ~/custom-images
```
Then edit 'train.py' to point to new directory and run:<br/>
```bash
python train.py
```
Dependencies: Python 3, Tensorflow 1.9

