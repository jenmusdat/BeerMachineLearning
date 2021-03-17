# Project3_BeerQuality

 - The project aims to look at beer reviews to determine a number of items based on the text reviews. Pulled from https://www.kaggle.com/ehallmar/beers-breweries-and-beer-reviews we will develop an analysis based on different types of machine learning. In creating this model we aim to use high accuracy to propose the best types of beers in the most approriate locations.
 
## Process:

 - Cursory exploratory analysis using Tableau (https://public.tableau.com/profile/jenny.kaylor#!/vizhome/Project3-Beer/Sheet4), SQL, Jupyter Notebooks
 - Used the text reviews to conduct a Word2Vec model analysis
 - Used the results of the Word2Vec model in a more complex linear regression to look for any connections between text reviews and scores
 - Created a k-means cluster analysis based on the Word2Vec results that will cluster like beers and review results together
 - Used the results of the clusters to create word clouds to discover any themes via the text within the clusters 
 - Created a logistic regression model placing the score results into two categories "postive" and "negative"
 - Each of the above required a great amount of srutinization and cleaning of the data
 
 ## Goal
 
 The goal of this project is to be able to use the text in the reviews to determine what beers and beer qualities have the highest chance of scoring 5s in all categories.
 
 ## Files
 [`Jay-Beer-Data-Explore.ipynb`](Analysis/Jay-Beer-Data-Explore.ipynb), [`Jenny-Beer-Data-Explore.ipynb`](Analysis/Jenny-Beer-Data-Explore.ipynb) - These were the notebooks used to explore the data, and perform the bulk of the ETL process.
 
[`Jay_word2vec.ipynb`](Analysis/Jay_word2vec.ipynb),[`training_smell.ipynb`](Analysis/training_smell.ipynb),[`Josh2vec.ipynb`](Analysis/Josh2vec.ipynb),[`Jenny_Feel_Model_to_Pandas.ipynb`](Analysis/Jenny_Feel_Model_to_Pandas.ipynb) - These are the notebooks where we trained our word2vec models.
 
[`Jenny_Beer_Regression_FeelTest.ipynb`](Analysis/Jenny_Beer_Regression_FeelTest.ipynb),[`Jenny_Beer_Regression_OverallTest.ipynb`](Analysis/Jenny_Beer_Regression_OverallTest.ipynb),[`Jay_word2vec.ipynb`](Analysis/Jay_word2vec.ipynb),[`scoretastelin.ipynb`](Analysis/scoretastelin.ipynb) - These are the notebooks where we calculated linear regression.

[`Jay_word2vec.ipynb`](Analysis/Jay_word2vec.ipynb) - This is the notebook used to create our clusters.
 
[`Jay_word2vec.ipynb`](Analysis/Jay_word2vec.ipynb),[`newExploration.ipynb`](Analysis/newExploration.ipynb) - We used these notebooks to understand our clusters.

[`WordClouds.ipynb`](Analysis/WordClouds.ipynb) - This notebook is where the Word Clouds were made.

[`Score_pos_neg.ipynb`](Analysis/Score_pos_neg.ipynb) - This notebook ran linear regression with a good or bad rating decided by picking a score value as a cutoff for each.
 ## Results
 ![2-d](https://user-images.githubusercontent.com/71193081/111407006-7158f500-8690-11eb-860d-37f8f0ae7fb0.png)
 
 ## Execution
 
 ## Conclusion
 This is a much larger topic than anticipated. The results show that we can use Natural Language Processing to find some interesting information. Even though we spent a lot of time cleaning the data, there could still be more cleaning of the data. Additionally the constraints of the environment greatly impacted our ability to accomplish all we set out to accomplish. That being said it is really exciting when we are able to get results that are meaningful. 
 
 ## Sources
 https://www.kaggle.com/ehallmar/beers-breweries-and-beer-reviews

3 Files:
- beers.csv
- breweries.csv
- reviews.csv
 
 ## Authors
 
Made by [Erica](https://www.linkedin.com/in/ericafisher1), [Jenny](https://www.linkedin.com/in/jenny-kaylor-045aaba5/), [Josh](https://www.linkedin.com/in/josh-gonzalez-williams-7aa9a31b0/), [Jay](https://www.linkedin.com/in/jay-hastings-techy/) with :heart: in 2021.
 
 


