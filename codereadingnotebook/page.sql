create table page(
    page_id integer auto_increment,
    PRIMARY KEY (page_id),
    title char(200),
    relation_id integer,
    FOREIGN KEY (relation_id) REFERENCES relation (relation_id),
    created_at datetime,
    updated_at datetime
);
