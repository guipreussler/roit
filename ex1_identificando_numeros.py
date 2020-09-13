#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Instalando pacotes que serão utilizados.
get_ipython().system('pip install tensorflow keras numpy mnist matplotlib')


# In[2]:


# Importando as bibliotecas que serão utilizadas.
import numpy as np
import mnist
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical


# In[3]:


# Carregando e treinando os conjuntos de dados (Imagens e Labels).
train_images = mnist.train_images()
train_labels = mnist.train_labels()
test_images = mnist.test_images()
test_labels = mnist.test_labels()


# In[4]:


# Declarando as imagens e pixels (0,255) que serão utilizados;
# Utilizando -0.5 / 0.5 para facilitar no "treinamento" do código.
train_images = (train_images/255) - 0.5
test_images = (test_images/255) - 0.5

# Setando as imagens em 28x28, ou seja, 784 quadrantes;
# Para passar a rede neural.
train_images = train_images.reshape((-1,784))
test_images = test_images.reshape((-1,784))

# Escrevendo o formato das váriaveis;
# 60.000 Linhas, 784 Colunas;
# 10.000 Linhas, 784 Colunas.
print(train_images.shape)
print(test_images.shape)


# In[6]:


# Construção do modelo;
# 3 e 2 camadas com 64 neurônios e a função relu;
# Função Relu -> função de ativação utilizada com melhor desempenho / utilizada para subtituir a ativação sigmóide.
model = Sequential()
model.add( Dense(64, activation='relu', input_dim=784))
model.add( Dense(64, activation='relu'))
# 1 camada com 10 neurônios e a função softmax.
# Função Softmax -> Utilizada para transformar números em probabilidades / produz um vetor que exibe a probabilizade de uma
# lista de resultados.
model.add(Dense(10, activation='softmax'))


# In[7]:


# Compilando o modelo
# A função de loss, mede o desempenho do modelo em suas tentativas;
# Melhoras na utilização do comando optimizer.
model.compile(
    optimizer='adam',
        loss = 'categorical_crossentropy',
        metrics = ['accuracy']
)


# In[8]:


# Treinando o modelo;
# Caso o número descrito seja 2, vetor apresentado --> [0, 0, 1, 0, 0, 0, 0, 0, 0, 0];
# Caso o número descrito seja 8, vetor apresentado --> [0, 0, 0, 0, 0, 0, 0, 0, 1, 0].
# O sistema funciona com base na probabilidade.
model.fit(
    train_images,
        to_categorical(train_labels),
        epochs = 5,
        batch_size=32
)


# In[9]:


# Avalia o modelo.
model.evaluate(
    test_images,
    to_categorical(test_labels)
)


# In[11]:


# Previsão nas 5 primeiras imagens de teste apresentadas.
predictions = model.predict(test_images[:5])
# Escreve a previsão realisada.
print(np.argmax(predictions, axis = 1))
print(test_labels[:5])


# In[12]:


# Imagens utilizadas no 5 primeiros testes.
for i in range(0,5):
        first_image = test_images[i]
        first_image = np.array(first_image, dtype='float')
        pixels = first_image.reshape((28,28))
        plt.imshow(pixels,)
        # cmap='gray' - > Comando pode ser utilizado para alterar a cor das imagens de teste.
        plt.show()


# Referência: https://www.youtube.com/watch?v=kOFUQB7u5Ck -> aprendizado do código




