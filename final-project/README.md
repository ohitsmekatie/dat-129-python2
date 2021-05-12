# Final Project DAT-129 (Python2)

## Project overview 

<img width="734" alt="Screen Shot 2021-05-11 at 10 09 44 AM" src="https://user-images.githubusercontent.com/9855295/117829914-2d720e80-b241-11eb-9740-ceef0b66cb85.png">


👋 My final project reads in data from the Star Wars API (planets and film endpoints to start) and:

1. 🪐 📽️ Displays film and planet stats 
2. 🌎 Shows you which planet you might want to live on based on your population preferences 
3. ❓Has a short interactive quiz about the film and planet stats

[Here](https://github.com/ohitsmekatie/dat-229-final-project/blob/main/raw_csv_files/.ipynb_checkpoints/get-final-project-csvs-checkpoint.ipynb) is a link to the Notebook that grabs the data from the Star Wars API and exports it to CSV's if you'd like to reuse the data and play around with it on your own! 

## Project preview 

<img width="775" alt="Screen Shot 2021-05-12 at 4 00 12 PM" src="https://user-images.githubusercontent.com/9855295/118037076-62fb2280-b33b-11eb-9eaf-f704bf79a29a.png">

<img width="974" alt="Screen Shot 2021-05-12 at 4 00 36 PM" src="https://user-images.githubusercontent.com/9855295/118037099-68f10380-b33b-11eb-9993-56a719ca8771.png">

<img width="1280" alt="Screen Shot 2021-05-12 at 4 00 45 PM" src="https://user-images.githubusercontent.com/9855295/118037113-6db5b780-b33b-11eb-9d0e-5dd36ae2b51c.png">

<img width="975" alt="Screen Shot 2021-05-12 at 4 01 36 PM" src="https://user-images.githubusercontent.com/9855295/118037132-73130200-b33b-11eb-919b-8b424393d875.png">


## Project technical details
* Written in Python using a Jupyter notebook
* Reads data into a Pandas dataframe and creates a Database using SQLite 
* Queries the database using SQL 

## What's next

1. There's a 🐛 with my SQL for calculating which planet would be most ideal based on your population density preferences. Need to fix that 🙃
2. Experiment with adding more data visualizations. Due to lack of time I didn't get to work with Pandas/Plotly as much as I'd like (read: not really at all 😄)
3. Look at other API endpoints to see if there's anything more interesting to look into or analyze; what species inhabit which planets? what is the gender breakdown of species? 
4. It's interesting that the opening crawl text is included and it might be cool to do some kind of sentiment analysis on the content 
