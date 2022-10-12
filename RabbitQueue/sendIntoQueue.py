from ast import Bytes
import pika

def sender(order):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='orders')
    channel.basic_publish(exchange='', routing_key='orders', body=str(order))
    print(f" [x] Sent {order}")
    connection.close()