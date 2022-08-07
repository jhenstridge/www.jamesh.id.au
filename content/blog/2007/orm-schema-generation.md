---
title: 'Schema Generation in ORMs'
slug: orm-schema-generation
date: 2007-09-28T18:05:04+08:00
tags: ['Launchpad', 'Storm', 'Ubuntu']
---

When [Storm](https://storm.canonical.com/) was released, one of the
comments made was that it did not include the ability to generate a
database schema from the Python classes used to represent the tables
while this feature is available in a number of competing
[ORMs](http://en.wikipedia.org/wiki/Object-relational_mapping "Object-relational mapping").
The simple reason for this is that we haven\'t used schema generation in
any of our ORM-using projects.

Furthermore I\'d argue that schema generation is not really appropriate
for long lived projects where the data stored in the database is
important. Imagine developing an application along these lines:

1.  Write the initial version of the application.
2.  Generate a schema from the code.
3.  Deploy one or more instances of the application in production, and
    accumulate some data.
4.  Do further development on the application, that involves
    modifications to the schema.
5.  Deploy the new version of the application.

In order to perform step 5, it will be necessary to modify the existing
database to match the new schema. These changes might be in a number of
forms, including:

-   adding or removing a table
-   adding or removing a column from a table
-   changing the way data is represented in a particular column
-   refactoring one table into two related tables or vice versa
-   adding or removing an index

Assuming that you want to keep the existing data, it isn\'t enough to
simply represent the new schema in the updated application: we need to
know how that new schema relates to the old one in order to migrate the
existing data.

For some changes like addition of tables, it is pretty easy to update
the schema given knowledge of the new schema. For others it is more
difficult, and will often require custom migration logic. So it is
likely that you will need to write a custom script to migrate the schema
and data.

Now we have two methods of building the database schema for the
application:

1.  generate a schema from the new version of the application.
2.  generate a schema from the old version of the application, then run
    the migration script.

Are you sure that the two methods will result in the same schema? How
about if we iterate the process another 10 times or so? As a related
question, are you sure that the database environment your tests are
running under match the production environment?

The approach we settled on with Launchpad development was to only deal
with migration scripts and not generate schemas from the code. The
migration scripts are formulated as a sequence of SQL commands to
migrate the schema and data as needed. So to set up a new instance, a
base schema is loaded then patched up to the current schema. Each patch
leaves a record in the database that it has been applied so it is
trivial to bring a database up to date, or check that an application is
in sync with the database.

When the schema is not generated from the code, it also means that the
code can be simpler. As far as Python ORM layer is concerned, does it
matter what type of integer a field contains? Does the Python code care
what indexes or constraints are defined for the table? By only
specifying what is needed to effectively map data to Python objects, we
end up with easy to understand code without annotations that probably
can\'t specify everything we want anyway.

---
### Comments:
#### michele - <time datetime="2007-09-28 19:02:12">5 Sep, 2007</time>

Hi James,

I totally agree, anyway I do think that a python (or other language)
based solution to schema definition and evolution could be very handy.
But I\'m 100% sure that such a tool doesn\'t belong to an ORM and even
more to it\'s \"mapping layer\". It should be a completely standalone
tool (not constrained to storm, sqlalchemy, \...) that allows you to
define tables, columns, versioning and migrations using only python
constructs, that way you could support different dbs within a single
dsl.

---
#### [riffraff](http://riffraff.blogsome.com) - <time datetime="2007-09-29 00:07:08">6 Sep, 2007</time>

well \$ORM\_FOR\_FAMOUS\_RUBY\_FRAMEWORK has pure ruby migration scripts
so that the schema can be evolved easily withouth touching SQL, and the
definition of the initial schema is just the first migration.\
I don\'t think that there is anything wrong with defining the schema in
SQL, but it seems close to what michele is suggesting in the above
comment.

---
#### Björn - <time datetime="2007-09-29 06:33:20">6 Sep, 2007</time>

Interesting article. It would also be interesting to know why you wrote
yet another Python ORM when there are already are so many other
excellent ones available. Storm vs. SQLObject or Storm vs. SQLAlchemy..
The linked site doesn\'t answer. Could be a topic for another article
maybe?

---
#### [Daniel Spiewak](http://www.codecommit.com/blog) - <time datetime="2007-10-02 01:06:52">2 Oct, 2007</time>

Sounds like database migrations are what you\'re looking for.
ActiveRecord (ORM for Rails) provides these, as does ActiveObjects and a
few other ORMs. They can be a bit weird at times, especially on
databases without flexible DDL ALTER statements. However, they take care
of a lot of the issues you enumerated.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2007-10-02 12:28:31">2 Oct, 2007</time>

Note that this article was about why we hadn\'t implemented schema
generation (as SQLObject has with SQLObject.createTable() and SQLAlchemy
has with Metadata.create\_all()). My point is that it seems
counter-productive to provide a feature that is only suitable for toy
projects, and the user will have to give up on as they progress.

The Ruby ActiveRecord system looks well designed, and much closer to
what I\'d want to use. That said, describing migrations in Python or
Ruby code doesn\'t really appeal to me: SQL seems to do a fine job for
the majority of migrations.

---
#### Robert Ahrens - <time datetime="2007-10-05 22:51:22">5 Oct, 2007</time>

I personally find the \*lack\* of schema generation to be an explicit
feature of STORM.

I\'m looking at building a set of Python webpages to expose an
administrative interface to an existing db-driven app. Without knowing
\*too\* much about STORM, it seems like its design aims will really
facilitate my placing an ORM layer atop an existing db, whereas with
schema-generating ORMs I feel like this is a bolted on feature and
involves some swimming upstream.

Nonetheless, I\'m pretty new to looking at Python ORMs and would be
happy to be disabused of these notions by a more knowledgeable party.

---
