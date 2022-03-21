# 導入函式
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras import utils #將 label 標籤轉成 one-hot-encoding
import matplotlib.pyplot as plt

# 載入訓練資料
(x_train, y_train),(x_test,y_test) = mnist.load_data()

# 建立簡單線性執行的模型
model = Sequential()

# Add Input layer, 隱藏層(hidden layer) 有256個輸出變數
model.add(Dense(units=256, input_dim=784,
kernel_initializer='normal', activation='relu'))

#Add output layer
model.add(Dense(units=10, kernel_initializer='normal',
activation='softmax'))

# 編譯:選擇 損失函數(loss)、優化方法(optimizer)及成效衡量方式(metrics)
model.compile(loss='categorical_crossentropy', optimizer='adam',
metrics=['accuracy'])

# 將 training 的 label 進行 one-hot encoding，例如數字 7 經過 One-hot encoding 轉換後是 0000001000，即第7個值為 1
y_trainonehot = utils.to_categorical(y_train)
y_testonehot = utils.to_categorical(y_test)

# 將 training 的 input 資料轉為2為
x_train_2D = x_train.reshape(60000, 28*28).astype('float32')
x_test_2D = x_test.reshape(10000, 28*28).astype('float32')

x_train_norm = x_train_2D/255
x_test_norm = x_test_2D/255

# 進行訓練, 訓練過程會存在 trainhistory 變數中
train_history = model.fit(x=x_train_norm, y=y_trainonehot, validation_split=0.2, epochs=10, batch_size=800, verbose=2)

# 顯示訓練成果(分數)
scores = model.evaluate(x_test_norm , y_testonehot)
print()
print("\t[Info] Accuracy of testing data = {:2.1f}%".format(scores[1]*100.0))

# 預測(prediction)
X = x_test_norm[0:10,:]
predictions = np.argmax(model.predict(X), axis=-1)
# get prediction result
print(predictions)

# 看第一筆測試資料
plt.imshow(x_test[0])
plt.show()

plt.plot(train_history.history['loss'])  # 優化後的損失函數
plt.plot(train_history.history['val_loss'])  # 損失函數
plt.title('Train History')  
plt.ylabel('loss')   # 優化後的損失函數
plt.xlabel('Epoch')  # 時期
plt.legend(['loss', 'val_loss'], loc='upper left')  
plt.show()





