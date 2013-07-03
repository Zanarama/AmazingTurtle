create table orgs(
orgid int not null auto_increment primary key,
name varchar(255) not null,
registerdt datetime not null
);

create table suborgs(
suborgs int not null auto_increment primary key,
name varchar(255) not null,
registerdt datetime not null
);

create table sessions(
sessionid int not null auto_increment primary key,
startdt datetime not null,
stopdt datetime not null,
name varchar(255) not null,
description text not null
);

create table classes(
classid int not null auto_increment primary key,
name varchar(255) not null,
description not null,
ownerid int not null,
foreign key (ownerid) references instructor(instructorid)
);

create table users(
userid int not null primary key,
firstname varchar(255) not null,
lastname varchar(255) not null,
registerdt datetime not null,
);

create table permissions(
permissionsid int not null primary key,
isadmin bool not null,
isinstructor bool not null
);

create table mazes(
mazeid int not null primary key,
mazecode text not null,
creationdt datetime not null,
userid int not null,
foreign key (userid) references users(userid)
);

create table programs(
programid int not null primary key,
programcode text not null,
createdt datetime not null,
userid int not null,
foreign key (userid) references users(userid)
);

