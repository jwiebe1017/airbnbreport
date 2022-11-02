# AirBnB Report for Mom n Dad
My parents own an airbnb out in Jefferson, CO. My intent is to convert the `.ipynb`'s  
that I've created into a functioning product to allow for ease of use.  
The notebooks themselves work most the time. This will allow anyone to see how I start to move pieces  
from R&D into a proper development module.


## Steps, in `airbnb_main.ipynb`
 - given a date range and quanty of results - build various requests
 - head to airbnb's underlying api and ping out to it to retrieve results
 - compile and parse the json results into a useable dataframe
 - save out several sheets

## Steps, in `airbnb_plot.ipynb`
 - given the output excel from above
 - compile and parse necessary columns
 - plot various plots and immediately save out

## TODO
get fully working code from ipynb to `main`   
with working components from various `utils.___`  
unit testing

## requirements
`geopy`  
`pandas`  
`numpy`  
`requests`  
`toolz`  
`pyyaml`