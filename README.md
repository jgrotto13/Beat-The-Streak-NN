# Beat-The-Streak-NN

The purpose of this Neural Network is to analyze player matchups for MLB's Beat The Streak contest. It uses the BeautifulSoup package to scrape and parse MLB batter vs. pitcher matchups from RotoWire.com. This data then runs through the NN which predicts which player is most likely to record a hit on a given day. The model was built using the Keras and TensorFlow packages in Python.

The RotoTableParser.py file is used to scrape and record these matchups daily. The results are then manually added to the MatchupData.csv to improve the model's accuracy. I also run a Cross-Validation and Grid-Search on the model every couple of weeks and tweak the parameters accordingly.
