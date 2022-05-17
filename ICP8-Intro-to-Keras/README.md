# ICP-8

#### Complete the following:
```
Name: Keenan Flynn
Email: kpfxn8@umsystem.edu
```
---
```
Partner Name: Jasmine Thai
Partner Email: jtt9fb@umsystem.edu
Partner ICP-Link: https://github.com/UMKC-APL-PythonDeepLearing/icp_8-JasmineThai-hub
```

```
Video Link: https://youtu.be/G6pzajL8emQ

```
### SUBMIT PYTHON NOTEBOOK FILE (ipynb files)
<br/>
 
# Write brief explanation here:

For ICP8 Question 1, we were given the diabetes csv to create a sequential model to predict, which allows us to create a deep learning model by adding layers to it. Every unit in a layer is connected to every unit in the previous layer. We passed the shape to the first layer, which in this case was input_dim = 8. We fit, transformed, and evaluated our model for three cases and plotted the history for loss and accuracy: 

     -Raw: Loss = 0.69; Accuracy = 65%
     -Normalized: Loss = 0.55; Accuracy = 73%
     -Normalized + Extra Dense Layers: Loss = 1.5; Accuracy = 72%
     
For the second part of the ICP we applied the same fully connected neural networks to a Breast Cancer dataset. This dataset has 31 independent variables and 1 dependent variable that tells us if a cancerous tumor is benign or malignant. We first preprocessed the dataset by curating the dataset to remove a column of nulls and the ID column. We then split the data using train_test_split with a test size of 25%. We made a copy of the X train and testing data before scaling it using a StandardScalar(). We also transformed the Y data from 'B' and 'M' (benign and malignant) to 0 and 1 respectively. This is because the sigmoid function at the end of the neural network will output a 0 or 1. 

First we got a benchmark by using the un-normalized data with an initial set of hidden layers (1 layer of 64 neurons). This network had an accuracy of 94% and loss of 0.15. We then graphed the accuracy and loss over the 100 epochs by using the models history() method. Next we used the same model but using normalized data. This model had an accuracy of 97.9% and loss of 0.15. This means that we achieved an increase of accuracy of 3%. Finally we used the normalized data and ran it through a NN with extra hidden layers (1 layer of 64 neurons, 1 layer of 128 neurons, and 1 more layer of 64 neurons). This model achieved an accuracy of 98.6% and loss of 0.18 which was the best performing model overall.
