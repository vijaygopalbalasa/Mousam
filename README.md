<img src="https://raw.githubusercontent.com/Raks-coder/Mousam/master/cloud.jpg" width="500">

# Mousam

## About 
> This is a machine learning based application which makes use of the delhi weather kaggle dataset. 

> The application makes use of lagged datasets

> We have made use of logistic regression and linear regression for the prediction of rain and temperature respectively

> The application predicts average temperature for the day in degree celsius

> Our Parameter for calling a day as hot is if the average temperature for the day is above 25 degree celsius

## Graphs and Plots

#### Some of my graphical analysis is shown below : 

<img src="https://raw.githubusercontent.com/Raks-coder/Mousam/master/temp-hum.PNG" width="650">

<img src="https://raw.githubusercontent.com/Raks-coder/Mousam/master/dew-temp.PNG" width="650">

## Hosting with Flask and Git

<img src="https://raw.githubusercontent.com/Raks-coder/Mousam/master/heroku.png" width="350">

Hosting with heroku is pretty simple, just follow the following steps:

1. `Heroku Login` - This will open up the browser through which you can log in to your heroku account

2. `git clone (your repo link)` - This clones your repo

3. `cd` into the folder of interest and use the following commands:-

          1. git init - It will initialize an empty repository
          
          2. git add . - It will add the files to the repository
          
          3. git commit - It will commit the changes
          
4. Use `heroku create (your desirable app name)` and then use `heroku git:remote -a (the git link generated from heroku create command)`

5. Finally use `git push heroku master`

<b>NOTE</b>
1. Add a requirements.txt to your repository 
2. Add Procfile to your repository

## Our App

Our weather prediction app is available at https://mousam-webapp.herokuapp.com 

For any doubts drop an email to me
          
