

## Refer to "Final_ML_Model.ipynb"


# Movie Makers

If you've ever wondered how to make a successful movie, we'd like to introduce you to the Movie Makers machine learning (ML) application that predicts whether your movie will be successful in the eye's of the audience based on it's budget and duration. This predictor was built using a logistic regression model and IMDB data sourced from Kaggle. The application assumes that an IMDB rating of 8 or higher out of 10 is a "successful" movie. You may the next great filmmaker in Hollywood, and we want to help you take La La Land by storm! Of course, there are several other factors that lead to a well-received film, but as a start you can guage how the duration and budget of your movie may predict its sucess. The data spans over 10,000 movies in the IMDB reaching as far back as the 1910s!

## How to use this application
Select the budget(USD) and duration(minutes) range that most accurately describe your movie, and we will predict whether your movie will be successful (IMDB rating of 8 or more) or not. Our machine learning model uses logistic regression to make predictions based on historical IMDB data with 90% accuracy.

## How we built this application

### Data cleaning and analysis

### Machine Learning
  We decided to use IMDB data from Kaggle, and first looked at the variables that may correlate with the rating. Both the budget and duration are quantitative fields that have a slight positive correlation with the overall IMDB rating. We decided to bin the budget and duration according to ranges that are both easily understood by the users of our tool, as well as capturing the full range of our data. 
* Budget - 
  * <100K
  * 100K-1M
  * 1M-10M
  * 10M-100M
  * 100M-1B
* Duration - 
  * <30min
  * 30-60min
  * 60-90min
  * 90-120min
  * >120min
For the definition of success, we tested ratings of 6,7 and 8 as cut-offs for success. Defining it as 8 or more gave us the highest testing data score (0.89 or 89%).We discovered that our data has more unsuccessful movies, and to account for this, we balanced our model. Refer to "Final_ML_Model.ipynb"

### Flask API

### HTML page with visualizations powered by Tableau


![demo](https://github.com/MersedehSP/Meetup_Project2/blob/main/video/demo.gif)

## Authors

* **Brian Regan** - *Data sourcing, data cleaning* - [bregan78](https://github.com/bregan78)
* **Joseph Lubrano** - *Flask* - [jlubranos](https://github.com/jlubranos)
* **Mersedeh Saniepay** - *Data analysis on * - [MersedehSP](https://github.com/MersedehSP)
* **Veena Uppalapati** - *Data sourcing (web scraping), visualizations* - [veenauppalapati](https://github.com/veenauppalapati)
* **Ramyata Upmaka** - *Visualizations, webpage* - [rambunctious2050](https://github.com/rambunctious2050)

## Acknowledgments

* Rutgers Data Science Bootcamp Instructors and TAs
