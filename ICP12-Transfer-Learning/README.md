# ICP-12

#### Complete the following:
```
Name: Keenan Flynn
Email: kpfxn8@umsystem.edu
```
---
```
Partner Name: Jasmine Thai
Partner Email: jtt9fb@umsystem.edu
Partner ICP-Link: https://github.com/UMKC-APL-PythonDeepLearing/icp_12-JasmineThai-hub.git
```

```
Video Link: https://youtu.be/8anyJnPVmh0
```
### SUBMIT PYTHON NOTEBOOK FILE (ipynb files)
<br/>
 
# Write brief explanation here:
We did some pre-processing work on the sentiment and spam dataset. We did this by first removing all punctuation, uppercase letters were transformed to lowercase, and words with numbers in them were removed. We used the Regex library 're' to do this. We then tokenized the sentences into a list of words.

Before we input these texts into an Embedded NN, we need to do a little more pre-processing to our labels by Encoding them so that they are numerical digits. We also transformed our sentences into a sequence of digits with a keras tokenizer which will allow the NN to learn about the data. Finally we padded these sequences so that they were a uniform length.

We also added an LSTM layer and for our output dense layer, we used activation='softmax'.

For the sentiment dataset we got 65% accuracy.

For the spam dataset we got 98% accuracy.

In the Transfer Learning portion of the ICP, we followed a Keras Tutorial to apply an ImageNet Classifier on the Cats and Dogs dataset. After loading in the data, we visualized the Cats and Dogs with matplotlib. We then reshaped the dataset to (150, 150, 3) to make sure all of the images were uniform. We also used prefetching to increase the loading speed of the NN. We also used data augmentation to increase the variability of the data. 

We then began to build the model. First we created the input layers so that the ImageNet can process our dataset. We have an Input layer, data_augmentation layer, and scaling layer which makes our dataset usable by ImageNet. Next we loaded the ImageNet weights without the top layers and Training=False. This will preserve the pretrained weights in ImageNet. We added top layers which were GlobalAveragePooling, Dropout, and a Dense layer for the output layer. We trained this model and got a 97% accuracy.

Finally we finetuned the model by making the ImageNet weights trainable. We made the learning rate very low so that no drastic changes would be made. This model achieved an accuracy of 98%.