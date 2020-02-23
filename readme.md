Logs Analysis Project - Udacity Full Stack Web Developer Nanodegree
DESCRIPTION
For this project, my task was to create a reporting tool that prints out reports( in plain text) based on the data in the given database. This reporting tool is a Python program using the psycopg2 module to connect to the database. This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:

What are the most popular three articles of all time?
Who are the most popular article authors of all time?
On which days did more than 1% of requests lead to errors?
RUNNING THE PROGRAM
To get started, I recommend the user use a virtual machine to ensure they are using the same environment that this project was developed on, running on your computer. You can download Vagrant and VirtualBox to install and manage your virtual machine. Use vagrant up to bring the virtual machine online and vagrant ssh to login.

## Requirements

[Link for Python 3] (https://www.python.org/download/releases/3.0/) - Code is using version 3.6.4 \
[For Vagrant installation] (https://www.vagrantup.com/) - A virtual media creator and manager \
[VirtualBox for the virtual machine] (https://www.virtualbox.org/) - An open source virtualization product. \
[Git] (https://git-scm.com/) - Open source version control system

Follow the steps below:

Download and install Vagrant and VirtualBox.
You can download this fsnd-virtual-machine. It is a configured vagrant file.

You will replace this database with news [newsdata.sql] (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).


Open Git Bash and start the virtual machine with 'vagrant up', enter cd vagrant to do this.

Use `vagrant ssh 'to continue after loading vagrant required files.

You will use 'psql -d news -f newsdata.sql` to load the database type.

Use the `logs_analysis.py` command to run the python program that brings the query results. this python file will output the desired output.

Load the database using psql -d news -f newsdata.sql.

Connect to the database using psql -d news.

Create the Views given below. Then exit psql.

Now execute the Python file - python logs_analysis.py.

CREATE THE FOLLOWING VIEWS FOR QUESTION 2 AND QUESTION 3:
