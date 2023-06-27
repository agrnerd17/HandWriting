from keras.datasets import mnist
from matplotlib import pyplot

(train_x, train_y), (test_x, test_y) = mnist.load_data()
#train data set & test data set

#print shape of the training and testing vectors:
print('X_train: ' + str(train_x.shape))
print('Y_train: ' + str(train_y.shape))
print('X_test: ' + str(test_x.shape))
print('Y_test: ' + str(test_y.shape))

#plotting
for i in range(9) :
    pyplot.subplot(330 + 1 + i)
    pyplot.imshow(train_x[i], cmap=pyplot.get_cmap('gray'))
    pyplot.show()    