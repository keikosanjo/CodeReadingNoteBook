create table page(
    id integer auto_increment,
    PRIMARY KEY (id),
    title char(200),
    belong_id integer,
    FOREIGN KEY (belong_id) REFERENCES belong (id),
    created_at datetime,
    updated_at datetime
);
