CREATE SOURCE CONNECTOR IF NOT EXISTS JDBC_SOURCE_POSTGRES_01 WITH (
    'connector.class'= 'io.confluent.connect.jdbc.JdbcSourceConnector',
    'connection.url'= 'jdbc:postgresql://postgres:5432/root',
    'connection.user'= 'root',
    'connection.password'= 'secret',
    "mode"='incrementing',
    'topic.prefix'= 'topic1_postgres_',
    "table.whitelist"='food_coded, comfort_food_reasons_coded'
);

CREATE SOURCE CONNECTOR IF NOT EXISTS JDBC_SOURCE_POSTGRES_02 WITH (
    'connector.class'= 'io.confluent.connect.jdbc.JdbcSourceConnector',
    'connection.url'= 'jdbc:postgresql://postgres:5432/root',
    'connection.user'= 'root',
    'connection.password'= 'secret',
    "mode"='incrementing',
    'topic.prefix'= 'topic1_postgres2_',
    "table.whitelist"='comfort_food_reasons_coded'
);


CREATE SINK CONNECTOR `elasticsearch-sinkfood` WITH(
    "connector.class"='io.confluent.connect.elasticsearch.ElasticsearchSinkConnector',
    "connection.url"='http://elasticsearch:9200',
    "tasks.max"= '1',
    "topics"= 'topic1_postgres_food_coded',
    "type.name"= 'listing',
    "key.ignore"= 'true');

CREATE SINK CONNECTOR `elasticsearch-sinkfood-1` WITH(
    "connector.class"='io.confluent.connect.elasticsearch.ElasticsearchSinkConnector',
    "connection.url"='http://elasticsearch:9200',
    "tasks.max"= '1',
    "topics"= 'topic2',
    "type.name"= 'listing',
    "key.ignore"= 'true');


CREATE TABLE comfort_food_reasons_coded (
    id BIGINT PRIMARY KEY,
    LABEL VARCHAR
) WITH (
    KAFKA_TOPIC = 'comfort_food_reasons_coded', 
    VALUE_FORMAT = 'AVRO',
    PARTITIONS = 1,
    REPLICAS = 1
);

INSERT INTO comfort_food_reasons_coded (id, LABEL) VALUES (1, 'stress');
INSERT INTO comfort_food_reasons_coded (id, LABEL) VALUES (2, 'boredom');
INSERT INTO comfort_food_reasons_coded (id, LABEL) VALUES (3, 'depression/sadness');
INSERT INTO comfort_food_reasons_coded (id, LABEL) VALUES (4, 'hunger');
INSERT INTO comfort_food_reasons_coded (id, LABEL) VALUES (5, 'laziness');
INSERT INTO comfort_food_reasons_coded (id, LABEL) VALUES (6, 'cold weather');
INSERT INTO comfort_food_reasons_coded (id, LABEL) VALUES (7, 'happiness');
INSERT INTO comfort_food_reasons_coded (id, LABEL) VALUES (8, 'watching tv');
INSERT INTO comfort_food_reasons_coded (id, LABEL) VALUES (9, 'none');

SET 'auto.offset.reset' = 'earliest';




