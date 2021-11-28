from kafka import KafkaConsumer
import sys
## default topic
topic = "my-topic"
if len(sys.argv) > 2:
    raise Exception("Maximum 1 parameter allowed | 1 paramter topic expected. Default : my-topic")
if len(sys.argv) == 2:
    topic = sys.argv[1]
'''
startConsumerService

paramters 
topic  String | Default "my-topic"

Starts consuming messages on given topic
'''

def startConsumerService(topic=topic):
    ## To consume latest messages and auto-commit offsets
    consumer = KafkaConsumer(topic,
                             bootstrap_servers= ['localhost:9092'])
                             
    ## Other ways to create a KafkaConsumer (For more info, visit https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html?highlight=kafkaconsumer)
    ## comment line starting with single # represents a commented codeline. 
    ## consume earliest available messages, don't commit offsets
    #KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)

    ## consume json messages
    #KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii')))

    ## consume msgpack
    #KafkaConsumer(value_deserializer=msgpack.unpackb)

    ## StopIteration if no message after 1sec
    #KafkaConsumer(consumer_timeout_ms=1000)

    ## Subscribe to a regex topic pattern
    #consumer = KafkaConsumer()
    #consumer.subscribe(pattern='^awesome.*')
 
                             
    for message in consumer:
        ## message value and key are raw bytes -- decode if necessary!
        ## e.g., for unicode: `message.value.decode('utf-8')`
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                              message.offset, message.key,
                                              message.value))

        

startConsumerService(topic)