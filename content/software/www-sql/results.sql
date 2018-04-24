<html>
<head>
<title>WWW-SQL Survey Results</title>
</head>
<body bgcolor="#FFFFFF">
<H1>WWW-SQL Survey Results</H1>
<!sql connect>
<!sql database james>
<!sql query "select users from country where domain='total'" tot>
<!sql query "select domain, users from country where domain <> 'total' and users <> 0 order by users desc limit 10" q1>
<!sql query "select platform, users from platform order by users desc limit 10" q2>
There are a total of <!sql print "@tot.0"> www-sql users who have completed
this survey (which has been running since 1st September 1997).  The
top 10 countries with www-sql users in them are:
<!sql qtable q1>

<p>The top ten platforms that www-sql runs on are:
<!sql qtable q2>
<!sql free tot><!sql free q1><!sql free q2>
<!sql close>
<p>Thank you for your interest.
<hr>
<a href="index.html">Back to the WWW-SQL Site</a>
<p>This page written by James Henstridge
(<a href="mailto:james@daa.com.au">james@daa.com.au</a>)
</body>
</html>

