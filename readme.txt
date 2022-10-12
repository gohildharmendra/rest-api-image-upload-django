#Go to Postman
#Get Token EndPoint
Method : POST
URL : http://127.0.0.1:8000/gettoken/

body :
{
    "username":"admin",
    "password":"admin"
}

#Upload image EndPoint
Method : POST
URL : http://127.0.0.1:8000/upload/

#Header pass Token [Authorization Token <t-value>]

body : Form
{
    "image":,
    "name":
}

#venv folder available in local pc
#.env file available in local pc