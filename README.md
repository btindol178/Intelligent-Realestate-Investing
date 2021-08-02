## Intelligent-Realestate-Investing

Goals of this Project: <br>
* Collect housing data from different sources and API's and visualize the location in a folium map <br>
* Using selenium take the addresses of API information and input into melissa.com where we can get address's of all neighbors on street <br>
* Use Zillow API to get zestimate and other stats on each house on the same street <br>
* Make a linear regression model or other prediction model showing what housing prices should be on that street <br>
* Make a web facing flask site for the ML algorithm <br>
* Deploy/learn to deploy the flask app on AWS  <br>

-----------------------------------------------------------------------------------------------------------------------------------------------
<h3> Package imports </h3>

import pandas as pd<br>
import requests<br>
import json                                                        #helps manipulate json<br>
import csv                                                         # helps with csv files<br>
from bs4 import BeautifulSoup                                      # to scrape web<br>
!pip install pyzillow                                              # zestimate api<br>
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults  # zestimate api<br>
from selenium import webdriver                                     # to scrape web<br>
from selenium.webdriver.support.ui import WebDriverWait            # to scrape web<br>
from selenium.webdriver.support import expected_conditions as EC   # to scrape web<br>
import os                                                          # to set directory<br>
import shutil<br>
!pip install folium<br>
import folium                                                      # map visualization<br>


email = 'blaketindol@gmail.com'<br>
passwordz = 'Your Password' <br>
