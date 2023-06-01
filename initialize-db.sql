drop table if exists items cascade;
drop table if exists todolist cascade;

create table todolist (
    id uuid primary key,
    day_added timestamp default current_timestamp
);

create table items (
    id uuid primary key,
    todolist_id uuid,
    FOREIGN KEY (todolist_id) REFERENCES todolist(id),
    day_added timestamp default current_timestamp
);