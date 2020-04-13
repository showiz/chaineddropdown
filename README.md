# chaineddropdown
Two examples of chained dropdown [ForeingKey and ManyToMany]
Using AJAX and Django 3.0

Here I present two kind of examples for different situations.
1) Person example: Who has to fill a form with the options 'Country' and 'City'
2) File example: For those who need to download a file for a selecting a 'Subject' and a 'Teacher'

In both examples the steps to follow are:

Step 1) Create a CreateView (class) in Views.py --------> (PersonView and FileView)
Step 2) Create a function to call the chained dropdown (def) in Views.py --------> (load_cities and load_teachers)
Step 3) Indicate the urls for the CreateView and for the load functions in urls.py --------> (PersonView|FileView and load_cities|load_teachers)
Step 4) Create a form filtered for both cases in forms.py --------> (PersonForm and FileForm)
Step 5) Create a HTML for the dropdown load ---------> (dropdowncities.html and dropdownteachers.html)
Step 6) Create a HTML form in wich we will use AJAX to make the calls ---------> (person_example.html and file_example.html)


* The ForeignKey example is an upgrade for the example in 
https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html

* The ManyToMany example is a propety of Héctor Valdés (showiz) for free use. 

* See the project in: 
https://swzdropdown.pythonanywhere.com/
