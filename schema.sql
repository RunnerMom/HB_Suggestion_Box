create table Students (
    id integer primary key autoincrement,
    first_name varchar(64) not null,
    last_name varchar(64) not null,
    github varchar(64) not null
);


create table Posts (
    id integer primary key autoincrement,
    title varchar(64) not null,
    body varchar(1024) not null,
    author varchar(64) not null,
    created_at varchar(32) not null
);

create table Votes (
    id integer primary key autoincrement,
    voter_id varchar(64) not null,
    post_id varchar(64) not null
);
