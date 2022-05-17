# ICP-10

#### Complete the following:
```
Name: Keenan Flynn
Email: kpfxn8@umsystem.edu
```
---
```
Partner Name: Jasmine Thai
Partner Email: jtt9fb@umsystem.edu
Partner ICP-Link: https://github.com/UMKC-APL-PythonDeepLearing/icp_10-JasmineThai-hub.git
```

```
Video Link: https://youtu.be/QffeKSZTZMY
```
### SUBMIT PYTHON NOTEBOOK FILE (ipynb files)
<br/>
 
# Write brief explanation here: 

In this ICP we created a Convolutional Neural Network to classify image datasets. 

The first dataset that we classified was the CIFAR-10 dataset, which comes included in the Keras library.
To use a CNN, we need to know the shape of the data. The CIFAR-10 dataset has 1024 pixels and is 32x32 in dimensions. 
The images are color so they have 3 color channels (RGB). Before we train the neural network we need to pre-process the data.
We do this by normalizing the pixel intensities so that they are between 0 and 1. We also one-hot encode the labels so that they are binaries.
We then build our Functional API CNN by using the following layers(Input, Conv2D, Dropout, MaxPooling2D, Flatten, and Dense). 
The Convolutional and Max Pooling layers use filters to help reduce the overall number of input dimensions before the Fully connected layers use weights and biases to do the actual learning.
We use a softmax activation function to determine the correct class.
This model is then fit with our training data and uses the ModelCheckpoint, ReduceLROnPlateau, and EarlyStopping callback functions.
The model experienced a validation accuracy of about 73% and was then saved and the training history was plotted.

We then used a similar CNN to predict images from a new dataset. This dataset is a large list of pokemon images, with 120 classes and varying amounts of images for each pokemon.
We simplified this dataset by using only the top 5 pokemon that had the most amount of training data. The pixels in the images for the 5 classes were then normalized.
In addition to normalization we also used data augmentation to boost the training. We used the same CNN except we added BatchNormalization layers to make the training more stable.
The model accuracy came out to be 91% and we were able to successfully classify independent images with our model.