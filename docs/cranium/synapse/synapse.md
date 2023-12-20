# Synapse Overview

Synapse is the general communication layer of CogniPilot. The goal of synapse is to provide an easily usable pub/sub mechanism which is efficient and easily extendible by users.

## Synapse Protobuf

* [Synapse Protobuf](https://github.com/CogniPilot/synapse_protobuf) defines the messages for CogniPilot in the Protobuf language. These messages are ROS compliant and NanoPB compliant.
* Protobuf provides both a message definition format and a serialization format. One advantage of the protobuf serialization compared to CDR serialiation embedded in ROS is that the message fields are optional and can be enabled with binary flags.
* CDR serialization support is being considered in B-Mythical to simplify ROS integration.

## Synapse TinyFrame

* [Synapse TinyFrame](https://github.com/MightyPork/TinyFrame) is a [TinyFrame](https://github.com/MightyPork/TinyFrame) based library for creating data frames to be sent over serial interfaces such as UART, telenet, and sockets. Checksums and mutex are configurable using the [TF\_Config.h](https://github.com/CogniPilot/synapse_tinyframe/blob/672c6d30d5e8cc24f720edd3b915889dc0bc5fab/include/synapse_tinyframe/TF_Config.h).
* Synapse TinyFrame allows for a simple point to point protocol using the known topic key values pairs defined in [SynapseTopic.h](https://github.com/CogniPilot/synapse_tinyframe/blob/672c6d30d5e8cc24f720edd3b915889dc0bc5fab/include/synapse_tinyframe/SynapseTopics.h). This is in contrast to protocols such as zenoh where key value pairs are negotiated. This saves the overhead of the negotiation phase, but if more advanced communication topologies are needed, a synapse\_zenoh is planned in the next release.

## Synapse ROS

* [Synpase ROS](https://github.com/CogniPilot/synapse_ros) is a bridge between the ROS pub/sub system and the Synapse TinyFrame + Synapse Protobuf based link to Cerebri. This allows communication between the more advanced algorithms in Cranium with the low level estimation and control algorithms running within Cerebri.

## Synapse GZ

* [Synpase GZ](https://github.com/CogniPilot/synapse_gz) is a bridge between the gazebo pub/sub system and the Synapse TinyFrame + Synapse Protobuf based link to Cerebri. This allows direct communication between the Gazebo simulator and Cerebri which is more effiecient for Software In the Loop (SIL) simulation.

## Synapse Msgs

* [Synapse Msgs](https://github.com/CogniPilot/synapse_msgs) contains standard ROS messages that were created to more easily interface with CogniPilot systems such as Cerebri.

## Example: Adding a New Message

Create a new file: ~/cognipilot/cranium/src/synapse\_protobuf/proto/my\_msg.proto
```proto
syntax = "proto3";
package synapse.msgs;

import "header.proto";
import "vector3.proto";
import "quaternion.proto";

message MyMsg {
	Header header = 1;
	Quaternion my_quaternion = 2;
	repeated double my_array_of_doubles = 3;
}
```

Create a new nanopb options file: ~/cognipilot/cranium/src/synapse\_protobuf/proto/my\_msg.options
```proto
synapse.msgs.MyMsg.my_array_of_doubles max_count:9
```

Add topic for your message in [~/cognipilot/cranium/src/synapse\_tinyframe/include/synapse\_tinyframe/Synapse Topic.h](https://github.com/CogniPilot/synapse_tinyframe/blob/672c6d30d5e8cc24f720edd3b915889dc0bc5fab/include/synapse_tinyframe/SynapseTopics.h)

* Consider adding to synapse\_ros and synapse_\gz message handling if required.
* Rebuild cranium.
* Push synapse\_protobuf and synapse\_tinyframe to your git repository.
* Update west in Cerebri to point to your git repository: [west.yml](https://github.com/CogniPilot/cerebri/blob/25497bf9960c6ca74e98c1709d34c756ac4395a9/west.yml#L32)
* Add to Cerebri [ZROS topic](https://github.com/CogniPilot/cerebri/blob/25497bf9960c6ca74e98c1709d34c756ac4395a9/lib/synapse/topic/src/synapse_topic_list.c#L110).
* Add ROS to Cerebri Listener if necessary [see code](https://github.com/CogniPilot/cerebri/blob/25497bf9960c6ca74e98c1709d34c756ac4395a9/lib/synapse/ethernet/synapse_ethernet.c#L159). 
* Add Cerebri to ROS Publisher if necessary [see code](https://github.com/CogniPilot/cerebri/blob/25497bf9960c6ca74e98c1709d34c756ac4395a9/lib/synapse/ethernet/synapse_ethernet.c#L306)

```
cd ~/cognipilot/cranium
colcon build --symlink-install
```


