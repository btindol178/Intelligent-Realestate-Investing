<h1> Realestate Investing </h1><br>
<H3> The Goals of this project </h3><br>
* To get houses values that are for sale programmatically using API's<br>
* To scrape a website melissa.com to get all of the houses on a street that are not for sale.<br>
* Use Zillow Zestimate to get values of houses that are not for sale.<br>
* Make a web facing flask app that uses machine learning to predict what a new build would look like on that street. <br>
* Deploy the application to AWS Elastic beanstalk <br>

<h3> First we load the proper packages </h3><br> 

![Caption for the picture.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture.JPG)<br>

<h3> Next we make a dictionary for state to state abbr mapping for our API function</h3>
* The api we will use is from https://rapidapi.com/apidojo/api/realtor/.<br> 
* It is the relator api you dont need your own API key here you can use theirs.<br> 
<br>

![Caption for the picture2.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture2.JPG)<br>


![Caption for the picture3.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture3.JPG)<br>

<h3> Now we clean up the API's output! </h3>
* Here we are selecting the right columns <br>
* Then we are selecting the address columns and other to expand the dictonary into multiple individual columns<br>
* Then using the API function to get data for cape coral fl
<br>

![Caption for the picture4.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture4.JPG)<br>

<h3> Now we can visualize the houses for sale from Relator API using a custom folium map and function</h3>
<br>

![Caption for the picture5.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture5.JPG)<br>


![Caption for the picture6.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture6.JPG)<br>


![Caption for the picture7.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture7.JPG)<br>


![Caption for the picture8.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture8.JPG)<br>


![Caption for the picture9.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture9.JPG)<br>


![Caption for the picture10.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture10.JPG)<br>


![Caption for the picture11.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture11.JPG)<br>


![Caption for the picture12.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture12.JPG)<br>


![Caption for the picture13.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture12.JPG)<br>

![Caption for the picture14.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture14.JPG)<br>


