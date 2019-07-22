# Twitter API

Project to get user tweets and search results from twitter

## Installation

You need to install `chromedriver` before start the project

If IOS
```
   brew cask install chromedriver
```
If Ubuntu
```
   sudo apt-get install chromium-chromedriver
```
or download it from
`https://sites.google.com/a/chromium.org/chromedriver/downloads`


Then you can create a virtual environment and install the requirements 

```bash
virtualenv -p python3.6 venv
source venv/bin/activate
pip install -r requirements.txt
export DRIVER_PATH=PATH_OF_CHROMEDRIVER
```

The project uses Falcon, Scrapy, Selenium and pytest
## Usage
To launch the app use the command to start the server
```
gunicorn server.app
```
The server will(usually) launch at `http://127.0.0.1:8000`

## Endpoints
`{{host}}/users/eleseguey?limit=10`

`{{host}}/users/eleseguey`

`{{host}}/hashtags/lacasadepapel?limit=45`

`{{host}}/hashtags/lacasadepapel`
