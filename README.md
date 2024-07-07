# pytest-pratice

#### install pytest library using 'pip install pytest'

#### the file for which you wants to write tests is recommended to have the same name as the file.

* for example i want to write test for the file named 'my_functions.py'
* then best practice is to have the same name as the code file preceded by the word 'test'. e.g:  'test_my_function.py'

* similarly if the function name is 'add()'. 
* best practice is that function name should be preceded by the test 'test_add()'
* **NOTE**: function name can be anything , but it is good to have the same or related name as the code file preceded by 'test'

**one of the advantage of this approach is that tests file are automatically detected**

* to run an individual test:  `pytest 'relative path of the file' `

 
