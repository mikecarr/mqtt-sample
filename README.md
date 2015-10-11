# MQTT Client Sample
Playing with MQTT which I plan to use in my home automation/IOT project.

## MQTT
MQTT is a machine-to-machine (M2M)/"Internet of Things" connectivity protocol. It was designed as an extremely lightweight publish/subscribe messaging transport. It is useful for connections with remote locations where a small code footprint is required and/or network bandwidth is at a premium

* Simple
  * TCP Based
  * Asynchronous
  * Payload agnostic
  * Pub/Sub

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

## Security
* ?


## References
* Sample Code
  * https://sakshambhatla.wordpress.com/2014/08/11/simple-mqtt-broker-and-client-in-python/
* MQTT
  * RabbitMQ Adapter
    * https://www.rabbitmq.com/mqtt.html
  * http://mqtt.org/
  * http://www.embedded101.com/Develop-M2M-IoT-Devices-Ebook
  * Android
    * https://github.com/mqtt/mqtt.github.io/wiki/mqtt_on_the_android_platform
    * http://dalelane.co.uk/blog/?p=1599
  * Arduino Library
    * http://pubsubclient.knolleary.net/
    * https://github.com/knolleary/pubsubclient
  * IOS
    * https://github.com/mqtt/mqtt.github.io/wiki/mqtt_on_ios

