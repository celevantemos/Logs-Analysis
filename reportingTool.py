#! /usr/bin/python2.7.3

import psycopg2

DBNAME = "news"


def get_query_result(query):
    '''
    This function connects to the database.
    Parameters: query which is a statement to run an sql query
    Returns: It returns the result of the query
    '''
    db = psycopg2.connect("dbname = " + DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def get_most_popular_articles():
    '''
    Returns top three most popular articles
    '''
    query = '''
        SELECT title,
        count(*) AS views
        FROM log
        JOIN articles
        ON log.path = concat('/article/',articles.slug)
        GROUP BY articles.title
        ORDER BY views DESC
        limit 3;
    '''
    answer = get_query_result(query)
    print "\nTop three articles according to page views\n"
    num_listing = 1
    for article in answer:
        number = str(num_listing) + " - "
        title = article[0] + " "
        views = "with a total views of " + str(article[1])
        print number + title + views
        num_listing += 1



def get_most_popular_article_authors():
    '''
    Returns top three most popular authors
    '''
    query = '''
        SELECT authors.name, COUNT(*) as total
        FROM authors
        JOIN articles ON authors.id = articles.author
        JOIN log
        ON log.path = concat('/article/', articles.slug)
        GROUP BY authors.name
        ORDER BY total DESC
        LIMIT 3;
    '''
    print "\nTop authors by page views\n"
    answer = get_query_result(query)

    print "\nTop authors by page views\n"
    num_listing = 1
    for author in answer:
        number = str(num_listing) + " - "
        author_name = author[0] + " --- "
        views = str(author[1])
        print number + author_name + views
        num_listing += 1



def get_error_by_days():
    '''
    Returns request percentage for days with more than 1% error
    '''
    query = '''
        SELECT requests.day,
        (errors.total_error * 100.0/requests.total_requests)
        AS percent
        FROM (
            SELECT to_char(time, 'DD/MM/yyyy') AS day, count(*) AS total_error
            FROM log WHERE status like ('404%')
            GROUP BY to_char(time, 'DD/MM/yyyy')
        ) AS errors
        JOIN (
            SELECT to_char(time, 'DD/MM/yyyy') AS day, count(*)
            AS total_requests
            FROM log
            GROUP BY to_char(time, 'DD/MM/yyyy')
        ) AS requests
        ON errors.day = requests.day
        WHERE ((errors.total_error * 100.0/requests.total_requests) > 1.0)
        ORDER BY percent;
    '''
    answer = get_query_result(query)

    print "\nRequests with days more than 1% error\n"
    for days in answer:
        date = days[0]
        percentage_error = str(round(days[1], 2)) + "% error"
        print date + " --- " + percentage_error


print "Please wait while calculating the results ......."
get_most_popular_articles()
get_most_popular_article_authors()
get_error_by_days()
