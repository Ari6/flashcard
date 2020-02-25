# Flash card app

# Memos for development

## Functions
* Qustions
	* Questions can be public or private. 
* Multiple questions
    * You can choose multiple questions from 2 - 8 choices.
* Typing questions
    * You can make typing questions.
    * Can select case sensitive or not.
* Import csv
    * You can import data from csv format.
* Logs
    * What you have done, result, time, times.
* Login
	* Basic login functions
	* Setting up for questions, import, etc.

## Model

Question| |
-|- |
id | primary key
type | int 
sidea | text 
sideb | text 
user | foreign key to User
group | foreign key to Group
create | datetime
update | datetime

Group | - |
- | - |
id | primary key
g_name | string
create | datetime
update | datetime
visible | int

User - Django default

Log | |
- | -
id | primary key
User | foreign key
Questioin | foreign key
last_time_correct | boolean
continuous_correct | int
correct_count | int
show_count | int

Config | |
- | -
remember_threshhold | int
