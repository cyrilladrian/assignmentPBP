[ASSIGNMENT 2]
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


[ASSIGNMENT 3]
1.  What is the difference between POST form and GET form in Django?
The difference of POST and GET in Django mainly is on the purpose. POST is primarily used for submitting data to the server. When you submit a form using POST, the form data is included in the request body. This is suitable for sensitive or large amounts of data, such as when creating a new record in a database. Whereas, GET is primarily used for retrieving data from the server. When you submit a form using GET, the form data is appended to the URL as query parameters. This method is suitable for search queries and filtering data but should not be used for sensitive or large data.

2. What are the main differences between XML, JSON, and HTML in the context of data delivery?
One of the difference of XML, JSON, and HTML is in the format or the structure/format of the language. XML uses a hierchichal data that acts as a tree and represent the tags such like and object entities. JSON is a lightweight, human-readable format that uses key-value pairs to represent data.  HTML is a markup language that uses tags to structure content for web browsers. In other words, XML is a versatile markup language for structured data, JSON is a lightweight and efficient format for data interchange, and HTML is primarily used for defining the structure and presentation of web content.

3.  Why is JSON often used in data exchange between modern web applications?
JSON's combination of simplicity, efficiency, cross-platform compatibility, and community support makes it an excellent choice for data exchange in modern web applications. Its role is especially prominent in the development of web APIs, single-page applications, and microservices architecture.

4.  Explain how you implemented the checklist above step-by-step (not just following the tutorial).
    1. Activate the virtual environment 
    2. Create the base.html file in the root directory 
    3. Adjust the main.html file from the previous assignment 
    4. In the main directory create a form.py file that accepts new item data 
    5. In the views.py at main folder, create a "create_product" function that automatically add new product when the form is submitted 
    6. Modify the "show_main" function in views.py
    7. add the new url path to access the previously made and imported function 
    8. add the new HTML template in the main directory called the create_product.html 
    9. Show the added data from the form by creating table inside the main.html file
    10. Create show_xml function and add its path to the urlpattern
    11. Create the show_json function and add its path to the urlpattern 
    12. Create the show_json_by_id and show_xml_by_id function and add their path to the urlpattern 
    13. Check the request and response via Postman 

5.  Access the five URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md.
    1. XML 
        ![Alt text](image-1.png)

    2. JSON
        ![Alt text](image-2.png)

    3. HTML 
        ![Alt text](image-3.png)

    4. JSON by id 
        ![Alt text](image-4.png)

    5. XML by id 
        ![Alt text](image-5.png)

[ASSIGNMENT 4 ]
1.  What is UserCreationForm in Django? Explain its advantages and disadvantages.
"UserCreationForm" is a built in form class provided by the Django authentication framework that simplifies the process of creating a new user account. Advantages: ease of use, integration with authentication, highly customizable, built in validation, and includes various security features. Whereas the disadvantages are limited flexibilities, frontend customization, and assumes default user model. 

2. What is the difference between authentication and authorization in Django application? Why are both important?
Authentication is about verifying the user's identity while authorization is about granting or denying access to the user. Furthermore, authentication typically involves the use of credentials, biometric, or other identity verfication methods; Authorization relies on permissions and access control lists (ACLs) to determine what actions a user is allowed to perform. Both are important for security purposes since together, they provide a security framework that ensures that only authorized and authenticated users can access certain parts of the application or perform specific actions.

3. What are cookies in website? How does Django use cookies to manage user session data?

Cookies are small pieces of data that a web server sends to a user's web browser and are stored locally on the user's machine. They commonly used to store informations about the user's interactions. When a user logs in to a website, a session cookie is created and stored on their device. This cookie contains a unique identifier that the server uses to associate subsequent requests from the same user with their session data on the server. This enables the server to maintain user-specific information, such as authentication status, shopping cart contents, or user preferences, throughout the user's visit to the site.

4. Are cookies secure to use? Is there potential risk to be aware of?
Although cookies are fundamental component of web development and are generally safe to use, like any other technology cookies comes with potential security risks. Few of them are: (1) storing sensitive information such as passwords or personally identifiable informations, directly in cookies is a significant security risks. (2) If session identifiers are not adequately protected, attackers may attempt to hijack a user's session by stealing their session cookie. (3) Excessive tracking and use of cookies for profiling user behavior can raise privacy concerns.

5.  Explain how you implemented the checklist above step-by-step (not just following the tutorial).
    1. Create register function in views.py 
    2. Create HTML file of the register function
    3. Add new path url of the register function to the urlpatterns 
    4. Create login function 
    5. Create login.html
    6. Add new path url of the login function to the urlpatterns
    7. Create logout function
    8. modify the main.html template 
    9. add path of the logout to the urls.py  
    10. add the login required to the show main function 
    11. modify the login user function so that it would required the user to sign in. 
    12. add the last login entity to the models 
    13. modify the logout user so that it would record the cookies 
    14. modify the main.html to show the recorded last login session 
    15. connect the product model to the user model 
    
