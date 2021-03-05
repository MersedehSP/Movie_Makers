
# Movie Makers

If you've ever wondered how to make a successful movie, we'd like to introduce you to the Movie Makers machine learning (ML) application that predicts whether your movie will be successful in the eye's of the audience based on it's budget and duration. This predictor was built using a logistic regression model and IMDB data sourced from Kaggle. The application assumes that an IMDB rating of 8 or higher out of 10 is a "successful" movie. You may the next great filmmaker in Hollywood, and we want to help you take La La Land by storm! Of course, there are several other factors that lead to a well-received film, but as a start you can guage how the duration and budget of your movie may predict its sucess. The data spans over 10,000 movies in the IMDB reaching as far back as the 1910s! We also provide visualizations to help you understand the movie landscape, for example, which genre is successful, how these trends changed over time, etc.

## How to use this application
Select the budget(USD) and duration(minutes) range that most accurately describe your movie, and we will predict whether your movie will be successful (IMDB rating of 8 or more) or not. Our machine learning model uses logistic regression to make predictions based on historical IMDB data with 90% accuracy.

## How we built this application

### Data cleaning
1. Sourced IMDB data from Kaggle and conducted the following data cleaning steps in a jupyter notebook.
2. Decided to only consider U.S. movies so that there is no currency conversion necessary. Removed all non-U.S. and non-English movies.
3. Noticed movies with missing or very low budgets, decided to remove all movies with budgets under $1000.
4. Added a column with a '1' for movies with IMDB ratings of 8 or greater, '0' for movies with ratings lower than 8.

### Data analysis
1. The cleaned data was analyzed in Jupyter notebook using Pandas and Matplotlib and a few other Python libraries. 
2. First a few correlations were done between the IMDB rating and other parameters from the movie csv in order. Analysis of budget vs. IMDB showed that we needed to bin the budgets to better organize the data. These bins were used in the ML section.
3. Using groupby, data was grouped based on budget, genre, year, etc. to make the following graphs:
 * Total movie count base on budget
 * Total movie count based on genre
 * Movie count based on the top 5 genres
 * Avg imdb rating for top 5 genres
This was also the basis of the Tableau visualization.

Links to Tableau Public:
* IMDB Rating, Duration and Budget Correlations: https://public.tableau.com/views/IMDBCorrelationwithbudgetandduration_Final/Dashboard1?:language=en&:display_count=y&:origin=viz_share_link  
* Genre Analysis:
https://public.tableau.com/views/AnalysisofGenresOverTime_Final/Dashboard2?:language=en&:display_count=y&publish=yes&:origin=viz_share_link  
* Successful vs. Unsuccessful Movies:
https://public.tableau.com/views/Goodmovies_BadMovies_Final/Dashboard3?:language=en&:display_count=y&publish=yes&:origin=viz_share_link

### Machine Learning
We decided to use IMDB data from Kaggle, and first looked at the variables that may correlate with the rating. Both the budget and duration are quantitative fields that have a slight positive correlation with the overall IMDB rating. We decided to bin the budget and duration according to ranges that are both easily understood by the users of our tool, as well as capturing the full range of our data. 
* Budget - 
  * <100K, 100K-1M, 1M-10M, 10M-100M, 100M-1B
* Duration - 
  * <30min, 30-60min, 60-90min, 90-120min, >120min
  

For the definition of success, we tested ratings of 6,7 and 8 as cut-offs for success. Defining it as 8 or more gave us the highest testing data score (0.89 or 89%).We discovered that our data has more unsuccessful movies, and to account for this, we balanced our model. Refer to "Final_ML_Model.ipynb"

Given more time, we can add additional features such as genres, directors, production company, languages, etc.

### Flask API
1. Imported the ML model and accepted inputs from webpage 
2. Ran the inputs through the ML model
3. Returned output "Successful" or "Unsuccesful" according to the model's prediction

### HTML page with visualizations powered by Tableau
1. Built a main page to allow user inputs of budget and duration ranges, and show the ML model's prediction
2. Built an additional visualization page to show data analysis and key observations

## Authors

* **Brian Regan** - *Data sourcing and cleaning* - [bregan78](https://github.com/bregan78)
* **Joseph Lubrano** - *Flask* - [jlubranos](https://github.com/jlubranos)
* **Mersedeh Saniepay** - *Data analysis and visualizations* - [MersedehSP](https://github.com/MersedehSP)
* **Veena Uppalapati** - *Webpage design* - [veenauppalapati](https://github.com/veenauppalapati)
* **Ramyata Upmaka** - *Machine learning* - [rambunctious2050](https://github.com/rambunctious2050)

## Acknowledgments

* Rutgers Data Science Bootcamp Instructors and TAs
