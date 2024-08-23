# Chapter 1 

<img src="https://media1.giphy.com/media/TrhpJt1hFqgCI/200w.gif?cid=6c09b952034xdcm0udz441w16o9jp0tkvhno8nsomvz8wqow&ep=v1_gifs_search&rid=200w.gif&ct=g" />  

## 1.1 Programming (general)  
**Input**:
Receives data  
**Process**:
Performs computations on that data  
**Output**:
Program puts that data somewhere. 

There are a sequence of steps and an order a program must follow. 
!!! info " "
    When reading a book, you open the book a certain way depending on your region and you start to read words from left to right to ingest sentences as you read from top to bottom. You can say there is an order of operations here.  

??? tip "YouTube Video"
    Here is an example where a parent teaches their kids how to write a process in sequential logical steps.  
    Metaphorically, the father can be the computer, the document will be the program.  

    (Ctrl + Click to open in new tab)  
    https://www.youtube.com/watch?v=cDA3_5982h8

--- 

## 1.2 Programming using Python  
**Python Interpreter**:
Program that executes code written in the python programming language.  

??? example "🦖 Example"

    I started my Python Interpreter using windows CMD/PowerShell with below snippet.  
    (Python should start up if PATH variables were setup on installation.)  
    Note - You can't start a "Python Application" just by installing Python, you 
    have to start Python from another software like an **IDE** (1) or from your **CMD** (2).  
    { .annotate }  

    1. **Integrated Development Environment (IDE)**  
    Examples of IDE's are VSCode, Sublime, IDLE, Thonny, Spyder, and Python Interpreter using CMD. 
    2. **Command Prompt** (CMD)  
    Default command-line interpreter for the OS.  
    I strongly suggest learning how to use your command prompt.  
    Watch this to get started! 👉 [YouTube Tutorials](https://www.youtube.com/watch?v=MBBWVgE0ewk&list=PL6gx4Cwl9DGDV6SnbINlVUd0o2xT4JbMu) 

    ```
    python
    print('Hello World!')
    ```  
    
    ![PythonInterpreter](../../img/Chapter1/PythonInterpreter.png "This screenshot is using python interpreter within the CMD")

**Interactive Interpreter:**
Program that allows to execute one line of code at a time.  

**Code**:
Code is a common word for the textual representation of a program (and hence programming is also called coding).  

**Line**:
Row of text.  

**Prompt**:
">>>", this indicates the interpreter is ready to accept code.  

**Statement**:
A statement is a program instruction.  

**Expressions**:
Expressions are code that return a value when evaluated; for example, the code wage * hours * weeks is an expression that computes a number.  

```
wage = 20
hours = 40
weeks = 52
salary = wage * hours * weeks
print(salary)
```

**Variables**:
The names wage, hours, weeks, and salary are variables, which are named references to values stored by the interpreter.  

**Assignment**:
A new variable is created by performing an assignment using the = symbol.  


??? question "Variables - Why is this is awesome!?"

    Now you can refer to your previous assignments 🤯.  
    1. If you put a paragraph in writing and assign that paragraph to a variable, you don't have to copy and paste that paragraph every single time to refer to it.  
    2. You can change and evolve the variable, refer to an old input to add something new.  
    
    !!! info  " "
        below is **pseudo code** (1), not **Pandas** (2) Syntax.
        { .annotate }

        1. Informal notation of programming language. 
        2. Python Library, think excel + sql for Python.  

    df =  

    | person | age |  
    | ------ | --- |  
    | Harry  | 12  |  

    Lets add one more row to df

    newRow =  

    | person | age |  
    | ------ | --- |  
    | Ron    | 13  | 

    df + newRow = 

    | person | age |  
    | ------ | --- |  
    | Harry  | 12  |  
    | Ron    | 13  | 

    df = df + newRow  

**print()**:
Print() function displays variables or expression values.

**Comments**:
Characters such as "#" denote comments, which are optional but can be used to explain portions of code to a human reader.  

```
# See <-- HashtagComment, subscribe, It means the interpreter will ignore this line of code. Write all the notes within the same line. If you make the person scroll to read, its already too long. Please create another comment line.
storeThisValue = 13
itDoesntMatterWhatYouCallMe = '13'
butItKindOfDoes = ':)'  
```  

!!! abstract "Formatting & Standards"  

    There is a standard way of writing so we all can be in unison to understand each other's code.  
    [PEP 8 Style Guide](https://peps.python.org/pep-0008/#:~:text=The%204%2Dspace%20rule%20is%20optional%20for%20continuation%20lines.&text=(Also%20see%20the%20discussion%20of,or%20after%20binary%20operators%20below.))  

---

## 1.3 Basic input and output  
Python by itself comes with built in functions you can use. 

??? info "metaphor"  

    Similar to excel, you use SUM(), COUNT(), etc to do aggregations. These are built in functions that come with Excel.  

```
print()
```

In python, we utilize print to output data in text or in a string format.  

??? question "Why print()?"

    <img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjd6aWV0bnZsMnFzdmJhc2hncHF1YXc1cWh0cHk0amh2cmpkbHg5aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0Iy1U0KU3rBaewjm/giphy.gif' width= 200/>  

    - We can display outputs of lines sequentially to better debug if needed  
    - To display any outputs, when you run code in automation, you don't need to see outputs for everything. Unless you want to be a rebel.  
    - Display warnings, notes, etc.  

### Keeping output on the same line
Notice the "WOW" ending separator.  
end: adds on a string the the end of your print statement  

```
print('This is one line.', end= 'WOW')
print('This is a second line.', end= ' ')
print('This is a third line.')
```

### Moving output to the next line
newline character:
\n  

??? question "What is an Escape Sequence?"

    <img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWU3ajNrcGM1NmdheTVmbzh2YmtqMGwxcm9nMGdlZHZ3cjAwdTk3diZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0OWistc2HUjf6PKM/giphy.gif'/ width= 200 />  
    Note the backslash is an escape sequence.  
    An escape sequence is a string that has a special meaning, like the newline character "\n", that always starts with a backslash "\".  
    Other escape sequences exist, such as "\t" to insert a tab, or "\\" to print an actual backslash character.

```
print('This is one line.', end= '\n')
print('This is a second line.', end= ' ')
print('This is a third line.')
```

### Basic input
The input() function:
is used to read input from a user. The statement best_friend = input() will read text entered by the user, and assign the result as a new string to the best_friend variable.  
The input() function causes the program to wait until the user has entered text and pushed the return key.  

```
input('Write something here to show as a notification before a user puts input')

# You don't need to have a string as a parameter like below, notice this is a comment because of #

input()
```

??? example "🦖 Example - input()"

    Have a user input a value and store it as a variable for later use.  
    Ex. Get users body weight, age, sex, and height to calculate BMI.

!!! info "Note"

    Just remember input() receives everything as a string.  
    If you want to store as an integer, you must convert.  

---

## 1.4 Errors  
<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTNxZm1ueHY0anc2bHRoYmZvY2VkajVxb3Bjcnlzbjl3N2FiYnh1YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/r3xBH1FXWz0h55CVtj/giphy.gif' width=200 />

Syntax Errors:
Violates the programming language rules. Basically Python does not understand what you want to do.  

Runtime Errors:
Syntax is correct, however the operation is impossible to run.  

Crash:
Abrupt termination of a program  

??? example "🦖 Example - Error"

    The error pinpoints to the line where the error occurred and labels the error accordingly.  
    ![PythonInterpreter](../../img/Chapter1/Errors.png)

### Common Error Types

|Error type|Description|  
|-|-| 
|SyntaxError|The program contains invalid code that cannot be understood.|  
|IndentationError|The lines of the program are not properly indented.|  
|ValueError|An invalid value is used, which can occur if giving letters to int().|  
|NameError|The program tries to use a variable that does not exist.|  
|TypeError|An operation uses incorrect types, which can occur if adding an integer to a string.|  

Logic Errors / Bugs:
Errors that run correctly but not behave as intended.  

??? example "🦖 Example - Logic Error"

    <img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGRid3lxa3oxdTAwc2FqYWJ6MW9qa2Mwc2o5czBpcDUxb3hjODM4aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WiCO2uZK05Klc1d28q/giphy.gif' />  
    You fat fingered some numbers on a spreadsheet, therefore your numbers are off.  
    Everything ran correctly, however the output is not as intended.  

---

## 1.5 Development environment  
Integrated Development Environment (IDE)  
Any development of code is usually conducted in an IDE.  

Some Software you can download to code in Python:  

1. [VSCode](https://code.visualstudio.com/)
2. [Sublime Text](https://www.sublimetext.com/)
3. [IDLE, Python Interpreter](https://www.python.org/)
4. [Thonny](https://thonny.org/)
5. [Spyder](https://www.spyder-ide.org/)
6. [Jupyter Notebooks](https://jupyter.org/)  

---  

## 1.6 Computers and programs (general)  
## 1.7 Computer tour  
## 1.8 Language history  
## 1.9 Why whitespace matters  
## 1.10 Python example: Salary calculation  
## 1.11 Additional practice: Output art  