from workshop_helper import make_connection

connection = make_connection()

channel = connection.channel()

channel.exchange_declare(exchange='broadcast_chat', exchange_type='fanout')

queue_result = channel.queue_declare(queue='', exclusive=True)
queue_name = queue_result.method.queue

channel.queue_bind(queue=queue_name, exchange='broadcast_chat')


def send(routing_key, message):
    channel.basic_publish(
        exchange='broadcast_chat',
        routing_key=routing_key,
        body=message,
    )

def listen():
    def on_message(chan, method, properties, body):
        print(' ['+ method.routing_key + ']: ' + str(body, 'utf-8'))

    channel.basic_consume(
        queue=queue_name,
        on_message_callback=on_message,
        auto_ack=True,
    )

    channel.start_consuming()


#listen(channel, 'chat')

# send('The great and powerful wizard of Oz', "You had the courage all along")
