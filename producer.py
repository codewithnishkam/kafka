from kafka import KafkaProducer
from kafka.errors import KafkaError
import sys

## default topic, key, value
topic = "my-topic"
key = None
value = None

## Check command line parmeters for producer class
if len(sys.argv) > 4:
    raise Exception("Maximum 3 parameters allowed.")
if len(sys.argv) <= 1:
    raise Exception("Minmimum 1 parameter required | required parameter value.")
if len(sys.argv) == 2:
    ## When only one parameter given it is considered as value and a message with this value is published on default topic.
    value = sys.argv[1]
if len(sys.argv) == 3:
    ## When two parameters are given then first parameter is topic and second paramter is value. So that message with value is published on given topic.
    topic = sys.argv[1]
    value = sys.argv[2]
if len(sys.argv) == 4:
    ## When three parameters given then first parameter is topic and second paramter is key and third parameter is value. Message with Key and Value is published at given topic. 
    topic = sys.argv[1]
    key = sys.argv[2]
    value = sys.argv[3]
    
   
'''
startProducerService

paramters 
topic  String | Default "my-topic"
key    String | Default None
value  String | Default None 

Produces message with key and value on given topic
'''
def startProducerService(topic=topic, key = key, value= value):
    ## Intitiating KafkaProducer. Vist here to read more. https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    ## Asynchronous by default
    future = producer.send(topic, value, key)

    ## Block for 'synchronous' sends
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        ## Decide what to do if produce request failed...
        raise Exception("Kafka Error")
        pass
        
    ## block until all async messages are sent
    producer.flush()
    
startProducerService(topic, key, value)  