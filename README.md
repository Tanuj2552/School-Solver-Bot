# School-Solver-Bot
school solver is a tutoring website
It is a simple web scraping bot, that displays a text message on your screen, when a new question is added in the school solver.

For this to work, you should have the following installed in your system.

1) Python3 (https://www.youtube.com/watch?v=uDbDIhR76H4) & pip (https://phoenixnap.com/kb/install-pip-windows)

2) you must also install requests, bs4, turtle, tkinter modules which can be installed using

    ```
    pip install -r requirements.txt
    ```
    The above command can be used only if you clone this repository.
    Else the following commands must be executed in the CMD (Command Prompt) 
    ```
    pip install requests
    ```
    ```
    pip install bs4
    ```
    ```
    pip install tk
    ```
    ```
    pip install turtle
    ```
    
After this, all you have to do is to run the code from any of your IDE's or text editors.. or terminal

This detects when there is a new question and shows you a tkinter gui, where you can choose the option to see the question or not see it.

1) if you choose to see the question, a turtle window opens, displaying basic info about the questions. And if you click on the turtle window, the code again runs normally and continues to fetch for new questions.
2) if you choose the option, not to see the question, then also the code runs normally to fetch new questions.
3) You need not run the code everytime, you just have to run it once.

NOTE: This code is still in basic development stage, I am trying to add more features to it.

Feel free to pull request and inform about any errors in the code :)
