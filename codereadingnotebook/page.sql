create table page(
    page_id integer auto_increment,
    PRIMARY KEY (page_id),
    title char(200),
    belong_id integer,
    FOREIGN KEY (belong_id) REFERENCES belong (belong_id),
    created_at datetime,
    updated_at datetime
);
