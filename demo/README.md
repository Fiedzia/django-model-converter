Export Django connection infromation and ORM models for use with Diesel ORM.
This is django app that provides "export" command which will generate Rust module
that can be used in Rust application to access same database as your Django project.
I've created it to complement some of my Django apps with Rust code,
while keeping models definitions in Django.



Goals:

1. Get it 100% right or die trying. Any bit of information that is not well understand should cause export to fail.
Hoping that it will somehow work and risking bugs will not be accepted.

2. Supporting broad range of popular databases, field types and options, within complexity budget.

3. Extensibility: new field types or databases should be easy to add.

4. Focus. I am more interested in supporting one way of doing things well -  maybe few if needed,
rather than allow every imaginable one, but done and documented poorly.

Its to early to say they were achieved, but this is where I am going.
