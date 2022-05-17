# ICP-11

##### [Dataset Link](https://umkc.app.box.com/s/znrabf69ksd4hkkpvj3r8ibo06lwuwlg)

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
Video Link: https://youtu.be/8anyJnPVmh0
```
### SUBMIT PYTHON NOTEBOOK FILE (ipynb files)
<br/>
 
# Write brief explanation here:
```
In this ICP, we created a Deep Learning model to solve a Sentiment Analysis problem. We used the IMBD review dataset and we wanted to know if we could classify a review as positive or negative. To be able to predict this label, we need to do some pre-processing work on the dataset. We did this by first removing all punctuation, uppercase letters were transformed to lowercase, and words with numbers in them were removed. We used the Regex library 're' to do this. We then tokenized the sentences into a list of words so that we could lemmatize them. Lemmatization reduces the overall number of words. After this we rejoined the list of words so that we got fully processed sentences. 

Before we input these sentences into an Embedded NN, we need to do a little more pre-processing to our labels by Encoding them so that they are numerical digits. We also transformed our sentences into a sequence of digits with a keras tokenizer which will allow the NN to learn about the data. Finally we padded these sequences so that they were a uniform length. 

Our Embedded NN has an Embedding layer. This layer takes the total number of vocabulary words we have and turns words into numbers that the NN can understand. A 1 dimensional Convolutional and Pooling layer are then used so that we can reduce the total number of features. Finally Dense layers perform calculations to predict the label of each sentence embedding. Because there are only 2 labels, we have an output layer with 1 neuron, a sigmoid activation function, and use the binary crossentropy loss function. We got an accuracy of 86%.

We compared this accuracy to the accuracy of a similar NN without the embedding layer which had an accuracy of 50%. 

For the 20 news group dataset, we analyzed our data and only got the important information (we filtered out the headers, footers, and quotes as unneccessary information). We preprocessed the data in exactly the same way as the previous dataset and we slightly altered the embedding model to take two parameters (vocab_size and max_len) for our input layer. We changed the activation in the output layer to be softmax and compiled the model with sparse_categorical crossentropy. Finally we fit the model with 10 epochs and the same callbakcs as the previous dataset and got an accuracy of 47%. Which makes sense since we really tried to stick to the code from the previous dataset (we really only had to change our embedded model a little).
```
