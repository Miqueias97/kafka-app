from kafka import KafkaProducer
from faker import Faker
import time, json, random

faker = Faker()

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    api_version=(3, 8, 0),
    value_serializer=lambda v: json.dumps(v).encode('UTF-8'),
    key_serializer=lambda k: k.encode('UTF-8')
)

def generate_temperature_data():
    return {
        'sensor_id': str(random.randint(1, 50)),
        'temperature': round(random.uniform(-10.0, 40.0), 2),
        'timestamp': faker.date_time().isoformat()
    }

if __name__ == '__main__':
    topic = 'temperature_sensor_topic'

    while True:

        data = generate_temperature_data()
        print(data)
        key = data['sensor_id']
        producer.send(topic=topic, key=key, value=data)
        time.sleep(1)