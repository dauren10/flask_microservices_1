#amqps://qlcexzxa:iFceMBpIaMuHMyDMYNNPFtiy9GRhNmOD@goose.rmq2.cloudamqp.com/qlcexzxa
import pika, json

params = pika.URLParameters('amqps://qlcexzxa:iFceMBpIaMuHMyDMYNNPFtiy9GRhNmOD@goose.rmq2.cloudamqp.com/qlcexzxa')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)
    #id = json.loads(body)
    #print(id)
    #product = Product.objects.get(id=id)
    #product.likes = product.likes + 1
    #product.save()
    #print('Product likes increased!')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()