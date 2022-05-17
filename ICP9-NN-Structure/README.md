# ICP-9

#### Complete the following:
```
Name: Keenan Flynn
Email: kpfxn8@umsystem.edu 
```
---
```
Partner Name: Jasmine Thai
Partner Email: jtt9fb@umsystem.edu
Partner ICP-Link: https://github.com/UMKC-APL-PythonDeepLearing/icp_9-JasmineThai-hub
```

```
Video Link: https://youtu.be/rCiAe61Y8gY

```
### SUBMIT PYTHON NOTEBOOK FILE (ipynb files)
<br/>
 
# Write brief explanation here:
In this ICP, we used a fully connected neural network to predict the classes of the MNIST dataset. The dataset is a collection of 28x28 pixel images of handwritten digits. We used Keras and a tensorflow front end, to solve this classification problem. After loading in the MNIST dataset, we normalized and flattened the input data so that it is a 1 dimensional vector of 784 pixels. We also used one-hot encoding for the labels to get them in binary format. 

We then built functions which defined 5 different Keras models.
-baseline model 
    -input layer with 784 nodes
    -hidden layer with 64 nodes
    -output layer with 10 nodes
    -accuracy: 97.8%. 
-boosted model 
    -increased the hidden layer depth by adding a hidden layer with 128 nodes
    -accuracy: 98%.
-tanh model 
    -used tanh as the activation function
    -accuracy: 97.5%. 

We used the baseline model to predict images with un-normalized pixel density
    -accuracy: 96% 

Finally we re-wrote the baseline model to use Keras functional API
    -accuracy: 97.9%

We were able to use these models to predict an arbitary images class by using the model.predict() and argmax() method. 

For the extra credit, we were able to use Sparse cross categorical loss function by using the raw labels that had not been one-hot encoded. 
Our prediction methods used the Numpy method argmax() to get the correct class for an image. 