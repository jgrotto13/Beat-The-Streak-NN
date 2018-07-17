"""""""""""""""""""""""""""
Beat The Streak Neural Network

Justin Grotton
"""""""""""""""""""""""""""
#Import Libraries
import numpy as np
import pandas as pd

#Fix random seed for reproducibility
seed = 7
np.random.seed(seed)

#Import data
dataset=pd.read_csv('MatchupData.csv')

#Split data into independent and dependent variables
X=dataset.iloc[:,2:13].astype(float)
y=dataset.Result

#Splitting the dataset into the training set and the test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train, y_test=train_test_split(X,y, test_size=0.2, random_state=0)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)

#Importing keras
import keras
from keras.models import Sequential
from keras.layers import Dense

# Initializing the NN
classifier=Sequential()

#Initial Layer and First Hidden Layer
classifier.add(Dense(input_dim=11,
kernel_initializer ='normal',
activation ='relu',
units=6))

#Second Hidden Layer
classifier.add(Dense(units=6,
kernel_initializer ='uniform',
activation ='relu'))

#Output Layer
classifier.add(Dense(units=1
,kernel_initializer ='normal',
activation ='sigmoid'))

#Compile NN
classifier.compile(optimizer='adam',
loss='binary_crossentropy',
metrics=['accuracy'])

#Fit Training Set to NN
classifier.fit(X_train,y_train,
batch_size=15,
epochs=25)

#Apply Test Set to NN
y_pred=classifier.predict(X_test)
y_pred=(y_pred>.5)

"""""""""""""""
RotoTableScraper
"""""""""""""""
#Import libraries
from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup
#***************SCRAPING*********************
url = "https://www.rotowire.com/baseball/matchup.htm"
html = urlopen(url)
soup = BeautifulSoup(html)
type(soup)
column_headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]
column_headers
data_rows = soup.findAll('tr')[2:27]
type(data_rows)
matchup_data = [[td.getText() for td in data_rows[i].findAll('td')]
            for i in range(len(data_rows))]
                
matchup_data_02 = []  #create an empty list to hold all the data

for i in range(len(data_rows)):  #for each table row
    matchup_row = []  #create an empty list for each matchup

    #for each table data element from each table row
    for td in data_rows[i].findAll('td'):
        #get the text content and append to the matchup_row 
        matchup_row.append(td.getText())

    #then append each matchup to the matchup_data matrix
    matchup_data_02.append(matchup_row)
    
matchup_data == matchup_data_02
df = pd.DataFrame(matchup_data, columns=column_headers)

#****************CLEANING********************
df[df['Batter'].isnull()]
df = df[df.Batter.notnull()]

df.drop('Pos', axis='columns', inplace=True)
df.drop('Team', axis='columns', inplace=True)
df.drop('Home?', axis='columns', inplace=True)
df.drop('Game Date', axis='columns', inplace=True)
df.drop('Opp', axis='columns', inplace=True)
df.insert(13, 'Result', ' ')

#****************EXECUTING*******************
Z=df.iloc[:,2:13].astype(float)

for index, row in Z.iterrows():
    #Transforming player matchups and running through the NN
    matchups = classifier.predict(sc_X.transform([row]))
    #Printing the predictions
    print (df.Batter[index], "Vs.", df.Pitcher[index], "\nHit Probability: ", matchups, "\n")
    
    






