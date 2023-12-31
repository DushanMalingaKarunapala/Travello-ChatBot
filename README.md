---------------------------------Implementation Details---------------------------
Implementation(User Manual)
User Manual: Setting up and Running the Chatbot

1. Prerequisites
   o Ensure that Python is installed on your computer(pyhon 3.9 recommended) You can download Python from the official website (https://www.python.org) and follow the installation instructions.
   o Ensure postgres is installed in your computer >Install PostgreSQL: In order to set up the PostgreSQL database, you need to install PostgreSQL with postgis(postgres stackbuilder>Other applications> Categories> Spatial Extentions > Postgis) on the computer. You can download the appropriate version for their operating system from the official PostgreSQL website.(https://www.postgresql.org/download/). And also download PG admin in order to interact with postgres
2. Download the Chatbot Package
   o Receive the chatbot package from the developer, which includes all the necessary files. it will include files like Chatbot,chatbotfullfilment, manage.py, requirements.txt, a psql file
   o Extract the contents of the package to a suitable location on your computer.
   19
3. Setting up the Virtual Environment
   o Open a command prompt or terminal.
   o Navigate to the extracted chatbot package directory.
   o Create a new virtual environment by running the following command:
   python -m venv myenv
4. Activate the Virtual Environment
   • Activate the virtual environment by running the appropriate command based on your operating system:
   o On Windows:
   myenv\Scripts\activate
   o On macOS and Linux:
   source myenv/bin/activate
5. Install Required Packages
   • Install the required packages by running the following command:
   pip install -r requirements.txt
   • after that run this command
   • if you getting an error while installing requirements.txt , it might be a reason with python version installed in your computer doesn't support included libraries in requirements.txt file. so it is recommended to use python version 3.9.2 to work this well
   pipwin install gdal
   20
   These commands will install all the necessary libraries and dependencies needed for the chatbot.
6. Database Setup:
7. PostgreSQL Database Setup(if you downloaded postgres and its required extensions above, skip this step)
   o Install PostgreSQL: In order to set up the PostgreSQL database, you need to install PostgreSQL with postgis(postgres stackbuilder>Other applications> Categories> Spatial Extentions > Postgis) on the computer. You can download the appropriate version for their operating system from the official PostgreSQL website.(https://www.postgresql.org/download/). And also download PG admin in order to interact with postgres
   2.Create a Database: Once PostgreSQL is installed give a password, then you need to create a new database for the chatbot. You can use a PostgreSQL client like pgAdmin to create the database. right click in the database section and create new database. then give it a name.
   3.Database Configuration:
   Open the main root file of the project in a IDE
   o Open the Django project's settings file (settings.py). chatbotfullfilment>settings.py
   o Locate the DATABASES section and update the values to match the PostgreSQL database information. Here's an example configuration:
   DATABASES = {
   'default': {
   'ENGINE': 'django.contrib.gis.db.backends.postgis',
   'NAME': '<database_name>',#database name
   'USER': '<database_username>', # default username (postgres)
   'PASSWORD': '<database_password>', #password you given in the postgres
   'HOST': '<database_host>', #localhost
   21
   }
   }
   o You should replace <database_name>, <database_username>, <database_password>, <database_host> with the appropriate values for the provided PostgreSQL database file.
   o open psql shell that was installed with postgres
   o run the following command "psql -U username -d dbname < filename.sql"
   o replace username with postgres
   o replace dbname with your database name that was created in postgressql
   o replace filename with sql file name (botdb)
   o so the command should be like this > psql -U postgres -d "yourdatabasename"< botdb.sql
   4.Migrate the Database:
   o Run Migrations: Once the database configuration is updated, you need to run the migrations to ensure the necessary tables are created in the database. You can use the following command in the terminal or command prompt(make sure you are in the virtual environment):
   python manage.py migrate
   7.Start the Chatbot Server
   • In the command prompt or terminal, navigate to the chatbot package directory.(make sure you are in the virtual environment)
   • Run the following command to start the chatbot server:
   python manage.py runserver
   The chatbot server should now be running and listening for incoming requests.
   22
   8.Configure ngrok
   • Download ngrok from the official website (https://ngrok.com/) and follow the installation instructions for your operating system.
   • Launch ngrok and authenticate your account.
   • go to the chatbot location using ngrok command prompt
   • activate local environment using > environmentname\Scripts\activate
   • In the command prompt or terminal, run the following command to start an HTTP tunnel using ngrok:
   ngrok http <port>
   Replace <port> with the port number on which your chatbot server is running. (e.g., 8000(django))
   > Now you have generated secure http link in order to communicate between dialogflow and the server
   > 9.Set Up Webhook with Dialogflow
8. Set Up Webhook with Dialogflow
   o Get the invitaion link from the developer in order to access the agent and edit the agent as a collaborator
   o Open the chatbot project.
   o Agent name is Travello
   o Go to the "Fulfillment" section.
   o Set the webhook URL to the ngrok HTTP URL generated in Step 8. example: "https://a35b-2402-d000-8110-b3e3-d48f-af6d-b94d-ef52.ngrok-free.app/webhook/"
   o Save the changes.
   o you also have to paste the url in project settings.py directory > allowed host section like this
   ALLOWED_HOSTS = [
   23
   'a35b-2402-d000-8110-b3e3-d48f-af6d-b94d-ef52.ngrok-free.app', #just and example
   '127.0.0.1',
   ]
   10.Test the Chatbot
   o Open Telegram and search for the chatbot by its username or name.
   o You can also scan the qr code given by the developer
   o Start a conversation with the chatbot and test its functionality.
#   T r a v e l l o B o t  
 #   T r a v e l l o C h a t B o t  
 #   T r a v e l l o C h a t B o t  
 #   T r a v e l l o - C h a t B o t  
 