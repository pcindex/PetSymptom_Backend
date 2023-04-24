
## Requirements:

- Python 3
- 'pip install tensorflow'
- 'pip install torch'


## Important Notes:

- The original dataset can be found from Kaggle https://www.kaggle.com/paultimothymooney/medical-speech-transcription-and-intent
- Original source code is from https://github.com/ensembles4612/medical_intent_detector_using_BERT/blob/master/medical_intent_detector_Using_BERT.ipynb
- Dataset isn't large enough and inaccurate. 4 EPOCH is enough to generate 99.40 accuracy rate.
- It is best to work on Google Colab as you can use GPU to train the model; faster process. 
-- However, training with CPU for this case is fine since the batch size isn't large and the training data is only 6662 sets.