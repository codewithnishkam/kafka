from kafka import KafkaConsumer
import sys
## standard host and port offered by docker image running kafka server 
bootstrap_servers= ['localhost:9092']
## default topic
topic = "my-topic" #default topic
if len(sys.argv) > 2:
    raise Exception("Maximou one parameter | topic expected. Default : my-topic")
if len(sys.argv) == 2:
    topic = sys.argv[1]
def startConsumerService(bootstrap_servers, topic):
    ## To consume latest messages and auto-commit offsets
    consumer = KafkaConsumer(topic,
                             bootstrap_servers= ['localhost:9092'])
    
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

        

startConsumerService(bootstrap_servers, topic)