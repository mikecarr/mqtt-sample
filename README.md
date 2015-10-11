# MQTT Client Sample
Playing with MQTT which I plan to use in my home automation/IOT project.

## MQTT Server
* Running RabbitMQ with MQTT Plugin
  * Docker Rabbit MQ with MQTT Plugin enabled
    * https://github.com/agco/docker-rabbitmq-mqtt
  * Docker run command:

    ```
    $ docker run -d -p 1883:1883 -p 5672:5672 -p 15672:15672 docker-rabbitmq-mqtt
    ```
  * RabbitMQ Console with MQTT Plugin
    ![RabbitMQ Console]
    (images/rmq-queue-view.png)

## References
* Sample Code
  * https://sakshambhatla.wordpress.com/2014/08/11/simple-mqtt-broker-and-client-in-python/
* MQTT
  * http://mqtt.org/
  * Arduino Library
    * http://pubsubclient.knolleary.net/
    * https://github.com/knolleary/pubsubclient

