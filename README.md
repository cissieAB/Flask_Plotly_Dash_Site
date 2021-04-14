# NASA FLASHFLUX TEAM INTERNAL SITE

This is a lightweight website written in Python Flask/Dash/Plotly (backend) and Bootstrap HTML/CSS (frontend).
The main purpose of this site is to share the Python Plotly figures with group members. 

## Development

### Python version requirement
A minimum version of Python 3.8 is required for this project. Older versions are not supported. 
Please install an appropriate version of Python.


### Running the Python virtual environment
This project utilizes the Python virtual environment to pack all the needed packages to `requirements.txt`.

To start the virtual environment, you can follow *either* of the following:
1. Command line
- For the first time usage, running the bash script with `sh start_venv.sh`.
- Then each time to edit the project, start the virtual environment by `source .venv/bin/activate`. 
  You will find the difference in the shell screen.
  
2. IDE (PyCharm, in my case): follow the instructions 
   [here](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#add-existing-interpreter) 
   and set the Python interpreter as `$current_folder$/.venv/bin/python3`.



## Deployment
NASA is using Apache to host the websites.
- [ ] Apache 

### Codes to be revised
- In `/apps/constants.py` line 5, change `HTML_HOME_PATH = "http://127.0.0.1:5000"` 
  to the actual home page url address.
  
## Updates
### Latency charts
- Source data location: under the folder `apps/data/latency`.
- Naming rules:
  1. Monthly latency data files are named as "typestr_vstr_SR_by_month.csv", 
  where `typestr` is "Aqua", "Terra" or "TISA", and `vstr` is "v3C" or "v4A".
  2. Annual latency data files are named as "vstr_latency_by_year.csv" where
  `vstr` is "v3C" or "v4A".

When 
The location and the file names are hardcoded in the backend. Please follow the rules.    

 

## References

- [How to embed a Dash app into an existing Flask app](https://medium.com/@olegkomarov_77860/how-to-embed-a-dash-app-into-an-existing-flask-app-ea05d7a2210b#bd30)
- [The Flask official documentation: deployment with Apache](https://flask.palletsprojects.com/en/1.1.x/deploying/mod_wsgi/)

---

- 