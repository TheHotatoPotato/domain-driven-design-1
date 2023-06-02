drop table if exists items cascade;
drop table if exists todolist cascade;

create table todolist (
    id uuid primary key,
    date_created timestamp default current_timestamp
);

create table items (
    id uuid primary key,
    todolist_id uuid,
    title varchar(255),
    body varchar(255),
    completed boolean default false,
    FOREIGN KEY (todolist_id) REFERENCES todolist(id),
    date_created timestamp default current_timestamp
);