# kafka
Reading continuously at consumer while sending messages from producer | Python API to start with Apache Kafka

# Requirements

Docker, python 2.7

# Note
Tested on Windows 10 \
Should also work on linux

# Run
Be ready to open multiple terminals \
Dowload this repository and extract \
kafka is the root folder for this project \
Open new terminal = terminal in kafka root folder \
Make sure docker is installed and running \
Make sure python 2.7 is installed and path variables are rightly set

## Run Kafka Server in Docker Container

Open new terminal and run \
``` docker run -p 2181:2181 -p 9092:9092 -e ADVERTISED_HOST=127.0.0.1  -e NUM_PARTITIONS=10 johnnypark/kafka-zookeeper ``` 

## Run Consumer Service

Open new terminal and run \
``` python .\consumer.py test-topic ``` 

## Run Producer Service

Open new terminal and run \
``` python .\producer.py test-topic nish kam```

## Output
You recieve detailed message at consumer terminal with key as "nish" and value as "kam". 
