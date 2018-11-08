
# coding: utf-8

# In[1]:


from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras import backend as K
K.set_image_dim_ordering('th')
import matplotlib.pyplot as plt
from scipy import io as spio
import numpy as np


# In[2]:


#loading data
emnist = spio.loadmat("Data/emnist-letters.mat")
#Dataset structure 
#emnist[dataset][0][0][0][0][0][0] this is the array for the image pixel values
#emnist[dataset][0][0][0][0][0][1] this is the array for the labels of the image
#emnist[dataset][0][0][1][0][0][0] this is the array for the test image pixel values
#emnist[dataset][0][0][1][0][0][1] this is the array for the labels of the test images


# In[3]:


x_train = emnist["dataset"][0][0][0][0][0][0] #training images
x_train = x_train.astype(np.float32)
y_train = emnist["dataset"][0][0][0][0][0][1] #training labels


# In[4]:


x_test = emnist["dataset"][0][0][1][0][0][0] #test images
x_test = x_test.astype(np.float32)
y_test = emnist["dataset"][0][0][1][0][0][1] #test labels


# In[5]:


train_labels = y_train
test_labels = y_test


# In[6]:


#normalize the test and train 
x_train /= 255
x_test /= 255


# In[7]:


x_train.shape[0]


# In[8]:


x_test.shape[0]


# In[9]:


x_train = x_train.reshape(x_train.shape[0], 1, 28, 28, order = "A")
x_test = x_test.reshape(x_test.shape[0], 1, 28, 28, order = "A")


# In[10]:


x_train.shape


# In[11]:


y_train.shape


# In[12]:


#encode the labels aka make it into an array of zeros and ones
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)


# In[13]:


y_train.shape


# In[14]:


y_train[0]


# In[20]:


#confirm the data is loaded correctly
sample = 5437
img = x_train[sample]
plt.imshow(img[0], cmap = 'gray')


# In[21]:


#confirm label is correct
train_labels[sample][0]


# In[23]:


num_classes = y_test.shape[1]


# In[26]:


#create model
model = Sequential()
layer1 = Conv2D(30,(5,5), input_shape = (1,28,28), activation = 'relu', name = 'layer1')
model.add(layer1)
model.add(MaxPooling2D(pool_size=(2,2)))
layer2 = Conv2D(15, (3,3), activation='relu', name = 'layer2')
model.add(layer2)
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(128, activation = 'relu'))
model.add(Dense(50, activation = 'relu'))
model.add(Dense(num_classes, activation='softmax'))
#compile model
model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()


# In[36]:


model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs = 6, batch_size = 1000)


# In[37]:


scores = model.evaluate(x_test, y_test, verbose=0)
print("Large CNN Error = %.2f%%" % (100-scores[1]*100))

