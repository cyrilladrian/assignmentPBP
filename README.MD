
URL : (im still struggling deploying my app through the adaptable.io)

Question 1: How do you Implement the tasks in the checklist
A. Create a django project 
1. activate the virtual environment
2. pip install the requirements 
3. create the django project using the django-admin startproject [project name]
4. add '*' to the allowed host in the settings.py

B. Create an app with the name main on that project 
1. run the python manage.py startapp main
2. open the settings.py file in the project directory and add main to the INSTALLED_APPS list

C. Create a URL routing configuration to access the main app
1. create the urls.py in the main app directory 
2. code the urls.py in the main app directory
3. open the urls.py in the project directory and import the include library
4. add the url pattern that directs to the main inside the urlpattern list 

D. Create a model on the main app with name Item and these mandatory attributes
1. modifying the models.py file in the main application directory, taking account of the mandatory attributes
2. run the python manage.py makemigrations
3. run the python manage.py migrate 


C. Create a function in views.py that returns an HTML template containing your application name, your name, and your class.
1. create the template directory
2. create an html that contains placeholder for the name, class, npm, and app name 
3. inside the views.py file in the main app directory, import render and add the show main function according to the templates inside the HTML file 


E. Create a routing in urls.py to map the function in views.py to an URL
1. open the url.py inside the project directory and add path to the main view within the url patterns. 
2. runserver in order to make sure the HTML file works as intended 

F. Deploy your app to Adaptable so it can be accessed through the internet
1. push all the project to github
2. push the new app button inside the adaptable.io
3. connect adaptable.io to github
4. choose the project repository
5. choose the python app template and postgre sql
6. adjust the python version
7. In the Start Command section, enter the command python manage.py migrate && gunicorn shopping_list.wsgi
8. enter the application name
9. check the http listener port and click the deploy app button

Question 2: Create a diagram explaining the flow of client requests to a django web and its response

![Alt text](image.png)

Question 3: What is the purpose of a virtual environment? Can we create a Django web app without a virtual environment?
A virtual environment is a self-contained directory that contains a specific Python interpreter and a set of libraries and packages. Its purpose is to manage and isolate python dependency for many different python project. Technically we can create a django project without virtual environment. However, it can leads into multiple problems such as: dependency conflicts, version control issues, and security risks. 


Question 4: What is MVC, MVT, and MVVM? Explain the differences between the three

MVC (Model-View-Controller), MVT (Model-View-Template), and MVVM (Model-View-ViewModel) are design patterns or architectural patterns used in software development, particularly in the context of developing user interfaces (UI) for applications.  While MVC, MVT, and MVVM are all architectural patterns used for structuring software applications, they differ in how they handle the separation of concerns between the Model, View, and the component responsible for handling user interactions and presentation logic. Each pattern has its strengths and is suitable for different types of applications and development contexts.
