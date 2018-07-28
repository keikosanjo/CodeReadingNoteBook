create table relation(
    relation_id integer auto_increment,
    PRIMARY KEY (relation_id),
    code_link TEXT,
    memo TEXT,
    created_at datetime,
    updated_at datetime
);
