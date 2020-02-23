#! /usr/bin/env python3

import psycopg2

DBNAME = "news"

request_1 = "What are the most popular articles of all time?"

query_1 = (""" 
			SELECT title,
				count(*) AS num
			FROM articles
			JOIN log ON articles.slug = substring(log.path, 10)
			GROUP BY title
			ORDER BY num DESC
			LIMIT 3;
			""")

request_2 = "Who are the most popular article authors of all time?"

query_2 = (""" 
			SELECT authors.name,
				count(*) AS num 
			FROM articles
			JOIN authors ON articles.author = authors.id
			JOIN log ON articles.slug = substring(log.path, 10)
			WHERE log.status LIKE '200 OK'
			GROUP BY authors.name
			ORDER BY num DESC; 
			""")

request_3 = "On which days more than 1% of the requests led to error?"

query_3 = ("""
            SELECT All_Get.date,
               round((100.0*Fail_Get.fail)/(All_Get.all)) AS errors
            FROM
               (SELECT to_char(TIME, 'Mon DD, YYYY') AS date,
                       count(*) AS ALL
                FROM log
                GROUP BY to_char(TIME, 'Mon DD, YYYY')) AS All_Get,

                (SELECT to_char(TIME, 'Mon DD, YYYY') AS date,
                    count(*) AS fail
                FROM log
                WHERE status='404 NOT FOUND'
                GROUP BY to_char(TIME, 'Mon DD, YYYY')) AS Fail_Get
             WHERE All_Get.date=Fail_Get.date
               AND ((100*Fail_Get.fail)/(All_Get.all)) > 1;
               """)


# Connect to the database and feed query to extract results


def get_queryResults(sql_query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(sql_query)
    results = c.fetchall()
    db.close()
    return results


result1 = get_queryResults(query_1)
result2 = get_queryResults(query_2)
result3 = get_queryResults(query_3)


# Create a function to print query results


def print_results(q_list):
    for i in range(len(q_list)):
        title = q_list[i][0]
        res = q_list[i][1]
        print("\t" + "%s - %d" % (title, res) + " views")
    print("\n")


def print_results3(q_list3):
    for i in range(len(q_list3)):
        title3 = q_list3[i][0]
        res3 = q_list3[i][1]
        print("\t" + "%s - %d" % (title3, res3) + "% views")
    print("\n")


print(request_1)
print_results(result1)
print(request_2)
print_results(result2)
print(request_3)
print_results3(result3)

