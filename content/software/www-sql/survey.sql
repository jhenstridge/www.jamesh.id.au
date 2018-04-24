<html>
<head>
<title>WWW-SQL Survey</title>
</head>
<body bgcolor="#FFFFFF">
<!sql setdefault domain "$REMOTE_HOST">
<!sql setdefault platform "other">
<!sql connect><!sql database james>
<!sql query "select lcase(right('$domain',3))" q1>
<!sql query "update country set users=users+1 where domain='total' or domain='@q1.0'">
<!sql if $AFFECTED_ROWS = 0>
<!sql query "insert into country values ('$@q1.0', 1)">
<!sql endif>
<!sql free val>
<!sql query "update platform set users=users+1 where platform='$platform'">
<!sql if $AFFECTED_ROWS = 0>
<!sql query "insert into platform values ('$platform', 1)">
<!sql endif>
<!sql close>
<H1>Results Submitted</H1>
Thank you for submitting your results.  To get a list of results, please see
the <a href="results.sql">results page</a>.  Other wise, go back to the
<a href="index.html">WWW-SQL Site</a>.
</body>
</html>

