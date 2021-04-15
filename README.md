# NASA FLASHFLUX TEAM INTERNAL SITE

This is a lightweight website written in Python Flask/Dash/Plotly (backend) and Bootstrap HTML/CSS (frontend).
The main purpose of this site is to share the Python Plotly figures with group members. 


## Environment

### Python version requirement
A minimum version of Python 3.8 is required for this project. Older versions are not supported. 
Please install an appropriate version of Python.


### Running the Python virtual environment
This project utilizes the Python virtual environment to pack all the needed packages to `requirements.txt`.

- For the first time usage, running the bash script with `sh start_venv.sh`.
- Then each time to edit the project, you can follow *either* of the following to start the virtual environment:
    1. Command line: `source .venv/bin/activate`. You will find the difference in the shell screen.
    2. IDE (PyCharm, in my case): follow the instructions 
   [here](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html) 
   and set the Python interpreter as `$current_folder$/.venv/bin/python3`.
- After adding more modules into the environment, please use `python3 -m pip freeze` to update `requirements.txt`.
A reference can be found [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).
  
## Description
### Folder structure
![](folder_structure.png)

### Backend
The backend mainly consists of Python Dash+Plotly apps. 
Each app is within a folder named as `./apps/dashapp_xxx`. 
For example, the latency plots are at `./apps/dashapp_latency`.

### Frontend
The static html webpages have to be under `./apps/templates/`. 

Flask will automatically search for the `.html` files at this location. 
Inappropriate processing of the locations may cause error.

## Deployment

### Configuring Apache
NASA is using Apache to host the websites.
- [ ] [Apache](https://flask.palletsprojects.com/en/1.1.x/deploying/mod_wsgi/)

### Revising codes for production usage
- In `/apps/constants.py` line 5, change `HTML_HOME_PATH = "http://127.0.0.1:5000"` 
  to the actual homepage url address after deployment.
  
## Updates
### Latency charts
- Source data location: `apps/data/latency/*.csv`. 
  Replacing the files in this folder to update the plots at the webpage endpoint.
- Naming rules:
  1. Monthly latency data files are named as "typestr_vstr_SR_by_month.csv",
  2. Annual latency data files are named as "vstr_latency_by_year.csv"

    where `typestr` is one of "Aqua", "Terra" or "TISA", and `vstr` is "Version3C" or "Version4A".
- The location and the file names are hardcoded in the backend scripts. Please follow them to save time.  
- The source data files are got through 
  the [automatic latency statistic scripts](https://github.com/cissieAB/LatencyResample). 
  Copying the results there to here is super welcome.
  


 

## References

- [How to embed a Dash app into an existing Flask app](https://medium.com/@olegkomarov_77860/how-to-embed-a-dash-app-into-an-existing-flask-app-ea05d7a2210b#bd30)
- [The Flask official documentation: deployment with Apache](https://flask.palletsprojects.com/en/1.1.x/deploying/mod_wsgi/)
