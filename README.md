# Waifu scrapper

Collection of scripts used to scrap waifu data, normalize it, select the top waifus and put the results into a relational database.

**Scrapping**: Scraps all the waifu data and images from [MyWaifuList](https://mywaifulist.moe) using internal site API's pretending to be the site doing normal calls (their API endpoints aren't rate-limited at the moment of writing)

**Selecting waifus**: Selecting is just done by picking the top N waifus ranked by popularity, where popularity is defined as #upvotes+#downvotes

# Install
```
pip install -r requirements.txt
```

# Use
```
python scrapper.py #Obtain all waifu data
python normalize.py #Normalize image filenames
python waifuselect.py #Select best waifus and prepare the data
python createdb.py #Put all the data in an SQL database
```

All the scrapped info will be stored in `waifus.json`. If you're only interested in the dataset itself, see [a detailed overview of the dataset](https://github.com/thewaifuproject/waifu-dataset) and [the full dataset on Kaggle](https://www.kaggle.com/corollari/waifus).
