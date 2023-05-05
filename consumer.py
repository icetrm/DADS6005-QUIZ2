from kafka import KafkaConsumer
from json import loads
from fastavro import reader
consumer = KafkaConsumer(
    'topic3_2',
     bootstrap_servers=['localhost:29092'],
     value_deserializer=lambda x: loads(x),
     auto_offset_reset='earliest',
     consumer_timeout_ms=5000
)

print(consumer)
for message in consumer:
    print(message)
#     print(f'KEY: {message.key} => {message.value}')