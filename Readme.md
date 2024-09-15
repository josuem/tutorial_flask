# Tutorial Flask
A simple tutorial for first steps in [Flask](https://flask.palletsprojects.com/en/3.0.x/)

# Install 

``` bash
pip install -r requirements.txt
```

# Run aplication
On windows, create the variable in the terminal 

``` bash
$env:FLASK_APP="main.py"
```

and run

``` bash
flask run
```

## Activate debugg mode
To activate the log mode create the variable

``` bash
$env:FLASK_DEBUG=1
```
and rerun the server
``` bash
flask run
```