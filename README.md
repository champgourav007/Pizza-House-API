# <div style='display:flex;justify-content:center;'><p>Pizza House<p></div>
<div style='display:flex;justify-content:center;'>
    <img style='margin: 0px 2px 0px 2px;' src='https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white' />
    <img style='margin: 0px 2px 0px 2px;' src='https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white'/>
    <img style='margin: 0px 2px 0px 2px;' src='https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white'/>
    <img style='margin: 0px 2px 0px 2px;' src='https://img.shields.io/badge/rabbitmq-%23FF6600.svg?&style=for-the-badge&logo=rabbitmq&logoColor=white'/>
</div>

<div style='display:flex;justify-content:center;'>
    <img style='margin: 0px 2px 0px 2px;' src='https://github.com/champgourav007/Pizza-House-API/actions/workflows/python-package.yml/badge.svg' />
</div>

## About
1. This is `Flask` based project which constitutes API to perform several functions.
2. `RabbitMq` is used to deal with continious API hitting and processing the result.

## Requirements
* Python 3.8x+
* Elang-otp `(install and setup to your local machine)`
* RabbitMq `(install and setup to your local machine)`

## Steps to Run the Project
1. Create a `git clone`.
2. To install all the dependencies perform `pip install -r requirements.txt`
3. Create a `.env` file to store the MongoDb Uri string in `DATABASE_URI` variable.
4. Make sure rabbitMq is configured to `localhost` to check the rabbitmq is working fine open is browser and `http://rabbitmq:15672/` go this url. Facing any issue then refer official docs of rabbitMq.
* If everthing is go well then just open the project and type `python app.py` make sure you are on correct folder.
