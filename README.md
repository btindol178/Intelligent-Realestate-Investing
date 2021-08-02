## Intelligent-Realestate-Investing

Goals of this Project: <br>
* Collect housing data from different sources and API's and visualize the location in a folium map <br>
* Using selenium take the addresses of API information and input into melissa.com where we can get address's of all neighbors on street <br>
* Use Zillow API to get zestimate and other stats on each house on the same street <br>
* Make a linear regression model or other prediction model showing what housing prices should be on that street <br>
* Make a web facing flask site for the ML algorithm <br>
* Deploy/learn to deploy the flask app on AWS  <br>

-----------------------------------------------------------------------------------------------------------------------------------------------
<h3> Package imports </h3> <br> 

![Caption for the picture2.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture.JPG) <br>

<h3> Make State Abbreviation Dictionary </h3> <br>

![Caption for the picture2.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/photos/statemapping.JPG) <br>

<h3> Relator API </h3>
Next your going to go to https://rapidapi.com/apidojo/api/realtor and get the sample API Code that is on the site to pull realestate listings. <br> 
These next two functions are right from the API page i didnt make them. <br> 

![Caption for the picture3.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/photos/api1.JPG) <br> 

![Caption for the picture4.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/photos/api2.JPG) <br>

<h3> Clean API Pull Data </h3> <br>

![Caption for the picture5.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/photos/clean%20api.JPG)<br>

<h3> Pick a city and state to use API Pull </h3><br>

![Caption for the picture6.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/photos/city1.JPG) <br>

<h3>Use cleaning function and API Function on data to make it more understandable</h3> <br>

![Caption for the picture7.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/photos/resp1.JPG)<br>

<h3> Expand address column that is a list of other columns </h3> <br>

![Caption for the picture8.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/photos/expand.JPG) <br>

<h3> Mapp the listings with Folium (Leaflet style map) to see if we can visually see patterns with color coding </h3><br>

![Caption for the picture9.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/photos/folium1.JPG) <br> 
