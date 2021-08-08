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


<h3> Now we need to loop through all of the individual addresses and put them into Melissa.com to get all of the addresses on that street.</h3>
* Here we paste a few columns together and inject them into a url for later use with selenium webdriver. <br>
<br>

![Caption for the picture7.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture7.JPG)<br>

<h3> Now that we have all the addresses we want and the urls we will inject them into the website with selenium webdriver and download an excel file of the data for each street of house addresses.</h3>
<br>

![Caption for the picture8.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture8.JPG)<br>


![Caption for the picture9.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture9.JPG)<br>


<h3> Now that we saved all of the excel files into our downloads folder lets loop through the files open them and append them to each other to make one big dataset. </h3>
<br>

![Caption for the picture10.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture10.JPG)<br>


![Caption for the picture11.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture11.JPG)<br>

<h3> Zillow API has been retired but this is the code used to get the zestimate for each of the houses not for sale. </h3>
* You can go here to do it manually https://www.zillow.com/how-much-is-my-home-worth/ <br>
<br>

![Caption for the picture12.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture12.JPG)<br>

<h3> Now that I have all of the houses on every street that has a house for sale ill reduce my data set for one street and compare some ML models for Prediction. </h3>
* I will compare Linear regression, gradient and regressor trees <br>
<br>

![Caption for the picture13.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture13.JPG)<br>

![Caption for the picture14.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture14.JPG)<br>

<h3> You can see the accuracy is not the best as this dataset is not trained on mucyh and didnt use very complex methods of training either. </h3> <br>.
<br>

<h3> Now lets make a web facing flask app using this ML model  </h3>
* First grab all of the files under the readme and make a new folder in your perfered ide mine is visual studio code.<br>
<br>

Step 1) Start virtual enviornment <br>
py -m venv venv<br>
<br>
Step 2) Activate the virtual env<br>
venv\Scripts\activate <br>
<br>
Step 3) Install Flask in virtual machine <br>
pip install flask <br>
<br>
Step 4) Install flask-wtf <br>
pip install flask-wtf <br>
<br>
Step 5) In main folder create .flaskenv file <br>
.flaskenv <br>
<br>
Step 6) Inside the .flaskenv file write this <br>
FLASK_ENV=development <br>
FLASK_APP=main.py <br>
<br>
Step 7) Install package called pip install python-dotenv to envoke the above enviornment variables<br>
pip install python-dotenv<br>
<br>
Step 8) Make requirements.txt folder<br>
pip freeze > requirements.txt <br>
	Step 8 Note) if needed to install requirements.txt folder do this<br>
	pip install -r requirements.txt<br>
<br>
Step 9) Install<br>
pip install pandas<br>
pip install numpy <br>
pip install scikit-image<br>
pip install -U scikit-learn<br>
<br>
Step 9) Make sure your in the right directory if you need to go deeper just use cd (next folder in) untill you get to where model.py is stored <br>
<br>
Step 10)Run Final Commmand <br>
python model.py <br>
python app.py <br> 
<br>

<h3> The app will look like this. I have put 3 bed 2 bath and 2000sqft in the inputs and you can see the output. </h3><br>
<br>



![Caption for the picture15.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture15.JPG)<br>

<h3> Now lets deploy this application to AWS Elastic Beanstalk!  </h3> <br>
* First you need to grab the style file and put it in a folder called static<br>
* Secondly you need to grab the python.config file and put it in a folder called .ebextensions this is for AWS<br>
* Thirdly you need to grab the html file and put it in a folder called templates<br>
* Lastly zip all of the files similar to the picture below for EB upload later<br>

![Caption for the picture16.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture1z.JPG)<br>

<h3> Log in at https://aws.amazon.com/console/ and create an AWS account </h3> 
* Then go to Elastic beanstalk via the search bar <br> 

![Caption for the picture17.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture2z.JPG)<br>


![Caption for the picture18.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture3z.JPG)<br>


![Caption for the picture19.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture4z.JPG)<br>


![Caption for the picture20.](https://raw.githubusercontent.com/btindol178/Intelligent-Realestate-Investing/main/photos/Capture6z.JPG)<br>
