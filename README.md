# FloodML
FloodML is a web application that uses Machine Learning to predict floods based on weather and and various historical data.

## Getting started
- Clone the project and install dependencies
- Activate virtual environment
- run pip install -r requirements.txt
- run python app.py
- You're Done!


## Inspiration
Floods are one of the most dangerous and frequent natural disasters in the world.

According to the World Resources Institute, over 80% of India's population, that is, 1.08 billion people, are at risk due to floods. Floods cause an economic loss of nearly 40 billion USD annually worldwide, and 15 billion USD per year in India alone. In the recent Kerala flood tragedy, over 100 people lost their lives, and over 15,000 houses and buildings were swept away in the torrential rains. These kinds of floods happen almost every single year in many prone areas, and cause major damage to life and property. The major cause of this is the overflowing of rivers, reservoirs and other water bodies due to extensive rainfall during the monsoon season.

Furthermore, climate change is increasing the risk of floods worldwide, particularly in coastal and low-lying areas, because of its role in extreme weather events and rising seas. The increase in temperatures that accompanies global warming can contribute to hurricanes that move more slowly and drop more rain, funneling moisture into atmospheric rivers like the ones that led to heavy rains and flooding in California in early 2019. Meanwhile, melting glaciers and other factors are contributing to a rise in sea levels that has created long-term, chronic flooding risks for places ranging from Venice, Italy to the Marshall Islands. As such, the risk and impact of floods is continuing to slope upwards.

Our team wanted to help solve this problem, so we created FloodML, a web application to predict floods and their impact before they even happen. Then, we display this information in an interactive graphical format, making the information compelling and easy to understand for people and governments alike.
  
## What it does
FloodML is our solution to floods in India. It is a web app that uses advanced machine learning algorithms to predict future floods based on weather forecast data – precipation, wind speed, humidity, temperature, maximum temperature, cloud cover – while allowing users to effectively visualize current and upcoming floods. The app has 4 core components:

#### 1. Plots
The 3 visualizations on the plots page are bubble plots that display flood predictions, damage predictions, and heavy rainfall predictions across India, taking in factors such as precipation, wind speed, humidity, temperature, cloud cover, as well as previous data history. Plots:
* The first plot is our flood prediction plot, which shows our ML powered prediction of where a flood is going to occur, marked by red dots.
* The second plot is a precipitation plot, showing the current precipitation data across the nation, with larger bubbles indicating more precipitation.
* Lastly, the third plot is a damage analysis plot, which shows the estimated cost and damage for various places in India, based on the flood risk prediction and population size. The size of the bubbles indicate the extent of predicted monetary damage, measured in USD.

#### 2. Heatmaps
The 3 heatmaps show flood predictions, damage predictions, and heavy rainfall predictions across India, taking in factors such as precipitation, wind speed, humidity, temperature, cloud cover, as well as previous data history. Plots:
* The first plot is our damage analysis plot, which shows a cost and damage analysis, with the colorscale of the heatmap indicating the extent of predicted monetary damage, measured in USD.
* The second plot is a precipitation plot, showing the current precipitation data across the nation, with the darker red areas indicating a greater volume of precipitation.
* Lastly, the third plot is a flood prediction plot, which shows our ML powered prediction of where a flood is most likely to occur given the current environmental factors, marked primarily by the darker red spots on a continuous colorbar.

#### 3. Satellite Images
Our satellite image analysis displays the volume of precipitation over various cities in India for different months. In order to create this feature, we analyzed netCDF4 formatted data from NASA's Global Precipitation Measurement Project, and produced geo-referenced plots using a combination of libraries, namely numpy, matplotlib, and cartopy. We then displayed our processed images on our web application for users and governments to view.

#### 4. Predict Page
On our predict page, the user simply enters the name of any city in the world. Our app then automatically fetches the weather forecast data of that city in realtime, runs this data into our Machine Learning model, and gives instantaneous results, which include the flood prediction, the temperature, the maximum temperature, the humidity, the cloud cover, the windspeed, and the precipitation.

## How We built it
#### The dataset
Our goal was to predict floods from weather data using machine learning. For the dataset, we first scraped the website http://floodlist.com/tag/india using the python beautiful-soup 4 library. This website provided us with information about past and current floods India, as well as their date and location. We then used the Visual Crossing weather API to obtain historic weather data such as precipitation, humidity, temperature, cloud cover, and windspeed in those areas and during those times. We also performed several data augmentation techniques on this data set, which enabled us to significantly increase the diversity of data available for our training model, without actually collecting new data.

#### ML model
Our machine learning model is based on the python sci-kit learn library. We used pandas to generate a data-frame for the dataset, and then tried various machine learning models from Logistic Regression to K-Nearest Neighbors to Random Forest Classification. After experimenting heavily with all of these models, the Random Forest Classifier gave us the highest accuracy of 98.71% on the test set. We proceeded to save our model in a pickle file.

#### Data Visualization
We first obtained a dataset of the major cities and towns in India (around 200 of them) along with their latitude, longitude and population. We then obtained the numerous weather factors in each city using the weather API and ran the data into our machine learning model. Next, we plotted the data from the model on various different types of maps, using Plotly chart studio. The maps represent various data such as flood prediction, precipitation analysis, and damage estimates, in the form of scatter plots, heat-maps, and bubble plots. The damage estimates were calculated based on flood prediction and population. We also produced geo-referenced satellite images for various cities in India, based on retrieved data from NASA's Global Precipitation Measurement project.

#### Front-end and hosting
Our web app is based on the Flask python framework. We rendered HTML templates – with CSS for styling and Javascript for added functionality – and integrated it with our machine learning models and datasets via the flask back-end. We then used Heroku's hosting service to host our web application for everyone to try! 

## Challenges We ran into
Our biggest challenge was in mining and collecting data to build our models and data visualizations. Given the extremely limited existing data available for floods and water related factors in India, scraping quality data was a challenge. We used a combination of weather API's and scraping techniques to create and compile an accurate and effective dataset. We also struggled with integrating the plots with our web app application, being our first time working with Plotly. Lastly, we faced a lot of git merge conflict issues due to different encodings of csv files and pickle versions across different computer platforms.

## Accomplishments that We're proud of
We are extremely proud of compiling and creating a dataset that can accurately and effectively reflect the current situation of floods in India, as well as allow us to make future predictions. We are also proud to have expanded our machine learning skills by testing out new models, and ultimately implementing a model with over 98% accuracy. Lastly, we are proud to have integrated various data augmentation, data mining, and date manipulation techniques, together with our model, to create detailed and sophisticated, yet compelling and easy to understand plots for data visualization.

## What We learned
First and foremost, we learned a great amount of web scraping and data mining, through our collection of data from websites as well as API's. We also learned techniques to manipulate and augment that data to create more effective datasets that provide us with better visualizations. Since it was our team's first time using Plotly, we also learned how to use plotly chart studio to create great visualizations. Lastly, we also expanded our machine learning skills through the testing of various models, especially the random forest classification model.

## What's next for FloodML
We would like to expand our web application to cover cities in countries all around the world, and to make our visualizations and predictions accessible to people across all nations, in an effort to prepare people and governments to the best of their ability.

Our team also believes further scientific analysis of satellite data could help critically in flood detection. Thus, we would like to expand to create an image classification model to detect signs of upcoming floods from satellite images.

Most importantly, our team is proud to have created a web application that could potentially help people and governments prepare for and reallocate resources for floods, potentially saving thousands of lives and millions of livelihoods.
