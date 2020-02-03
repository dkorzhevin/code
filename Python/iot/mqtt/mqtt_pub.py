import paho.mqtt.client as mqtt


broker_ip = 'broker.hivemq.com'
broker_port = 1883
mqtt_topic = 'mytest/topic'
payload = '{"message":"Hello World"}'

def on_connect(client, obj, flags, rc):
    # self.master.subscribe(mqtt_topic)
    print("connected" + str(rc))


def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def mqtt_pub(client, payload): #function to publish payload to a topic
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect(broker_ip, broker_port, 60)
    client.publish(mqtt_topic, payload)
    print('MESSAGE PUB [x] ' + payload)


if __name__ == '__main__':
    client = mqtt.Client()
    mqtt_pub(client, payload)
