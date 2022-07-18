## NAME
LIBRARY SYSTEM
## DESCRIPTION
This project is designrd by a django framework, sqlite database and bootstrap.It is a web based application.
## TABLE OF CONTENT
Setup
Technologies used
Usage
Project status
Acknowledgements
Contributors
License
Contact
## SETUP
1. Install [virtualenv](https://docs.python.org) on your machine:
* __For windows__:  
```
$ python -m pip install virtualenv
```
* __For Linux and Mac OS__:  
```
$ pip install virtualenv 
```
2. Create a directory called LMS and move into that directory:   
```
$ mkdir LMS
$ cd LMS
```

3. Clone this projects public repository from [gitlab](https://gitlab.com):  
```
$ git clone http//gitlab.com/fearless5/library.git
```

4. Change the current working directory into the cloned projects directory:  
```
$ cd g5-library-system
```

5. Create a new virtual environment to manage the projects local modules:  
```
$ virtualenv lms-env

6. A new folder lms-env will be created in the current directory.  
* __On Windows activate the environment using:__   
```
$ lms-env\Scripts\activate
```

* __On linux and Mac OS activate the environment using:__   
```
$ source lms-env/bin/activate  
```

You should see the name __lms-env__ in brackets on your terminal line eg    
```
$(lms-env)user@laptop:~$
```

6. Install the project dependencies:  
```
$ pip install -r requirements.txt
```

7. Start the project using:    
```
$ python manage.py runserver
```


```
## TECHNOLOGIES USED
Python -- 3.8 and above
pip -- 22.0 and above
Sqlite -- 3.9 and above
Django -- 4.0
Bootstrap -- 4.0

## USAGE
This should be used by a student to access available books and librarian to post the available and unavailable books.
It should save student's time and also reduce on the commotion in the library.
It should enable the librarian to follow up students that have borrowed the books.

## ACKNOWLEDGEMENT
This project was inspired by DR WAKOOLI PETER.
This project was based on various django tutorials.
Many thanks to MOSH a tutor of django on youtube.  
 
 ## CONTRIBUTORS
 NAKALANZI VIVIAN
 NALULE DIANA
 KATALEMWA JAVIOUS
 BASIIMA COLLINELIOUS

 ## LICENSE
 It is an open source project.

 ## PROJECT STATUS
 The project is in progress.

 ## CONTACT
 Created by group 20. 








