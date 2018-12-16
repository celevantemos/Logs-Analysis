# Overview
This project is answering three questions regarding a news paper website. These questions are:
1) **What are the most popular three articles of all time?** Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

2) **Who are the most popular article authors of all time?** That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3) **On which days did more than 1% of requests lead to errors?** The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

## Set Up:
* Install [Vagrant](https://www.vagrantup.com/)
* Install [VirtualBox](https://www.virtualbox.org/)
* python 2.7.3
* Download the database used [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
* Put the newsdata.sql file into the vagrant directory after expanding the compressed file
* Copy and paste the project into the vagrant directory as well

### Virtual Machine:
1) run (vagrant up) to build vm for first time
2) run vagrant ssh to connect
3) go to current directory that the project is in

### Start Virtual Machine and Load data into database:
* Navigate in _Terminal_ to the vagrant directory
* Run ```vagrant up``` to start the VM for the first time
* Once done, run ```vagrant ssh``` everytime you need to connect
* Now, navigate to the project directory in _Terminal_ ```cd /vagrant/ProjectBackEnd/```
* load data using ```sql -d news -f newsdata.sql```

### Run the project:
You must be in the directory that the project is in to run the project
_Run_ ```python reportingTool.py```

### Expected Output:
>Please wait while calculating the results .......

>Top three articles according to page views

>1 - Candidate is jerk, alleges rival with a total views of 338647
>2 - Bears love berries, alleges bear with a total views of 253801
>3 - Bad things gone, say good people with a total views of 170098

>Top authors by page views

>1 - Ursula La Multa --- 507594
>2 - Rudolf von Treppenwitz --- 423457
>3 - Anonymous Contributor --- 170098

>Requests with days more than 1% error

>17/07/2016 --- 2.26% error
