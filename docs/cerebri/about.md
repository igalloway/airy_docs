# About Cerebri

[Cerebri](https://github.com/cognipilot/cerebri/tree/airy) is a correct by construction autopilot. This software paradigm simplifies the verifcation and validation task through the consideration of ease of verification during code creation.

The verification approach relies on the faithful synthesis of mathematical control laws for a given vehicle dynamic model interacting with a finite state machine. A layered approach is used to ensure robustness of the sytem.

### Layers of Verificaiton and Validation

* MISRA C compliance. Follow closely the industry best practices as defined in the [MISRA C](https://en.wikipedia.org/wiki/MISRA_C) standard. The verification of the high levels of system operation use the low level operating system and drivers as a foundation.
* On top of the the solid operating system and drivers, create control and estimation methods that interact with a given dynamic model. For interested readers, see this [paper](https://arxiv.org/abs/2211.03310) of one such robust control strategy.

## ZROS Publish and Subscribe Library

After considering both the [rclc](https://github.com/ros2/rclc) library and [ZBUS](https://docs.zephyrproject.org/latest/services/zbus/index.html), it was determined to be advantageous to construct a tailored publish/subscribe library for use in Cerebri.

### Comparison to Other Libraries

| Library | Thread-safe | Misra C | Community Base | Separate Read/Write Locks | Lines of Code |
| --------| ----------- | ------- | -------------- | ------------------------- | ------------- |
| rclc    | no          | no      | large          | N/A                       | ~29k |
| ZBUS    | yes         | yes     | small          | no                        | 1409 |
| ZROS    | yes         | yes     | new library    | yes                       | 748  |

While Cerebri was initially built around ZBUS, it was found too limiting due to the available topic listener and subscriber implementations. Instead of providing callback functions where the topic data structure is in context, ZROS signals the subscribers that a new message is availabe. It is then up to the subscriber to process the data. This is similar to a ZBUS subscriber, but it uses signals instead of message queues. In ZROS, it is imperative that the latest sensor data is available to each node, but skipping packets between nodes is acceptable. All messages describing the state of the vehicle are stateful, so dropping one message is not critical. This is also the goal for all input to the system. It should be assuemd that packets will be lost, and the requests of the user should be a state that is continually sent at a periodic rate.

Cerebri is constructed using a set of reusable nodes. These nodes communicate using topics. ZROS is thread-safe and leverages a read semaphore and a write mutex lock on each topic. This allows multiple subscribers to read the data simultaneously.

## General Structure

In order to simplify the verification process, the vehicle management firmware is divided into various subcomponents.

* **Operating Systeam**: Cerebri leverages the Zephyr RTOS, which is working towards [MISRA C compliance](https://www.zephyrproject.org/zephyr-rtos-moves-towards-misra-compliance/).
* **drivers**: The drivers are low level operating system code to talk with various sensors, actuators etc. Drivers are primarily maintained in upstream Zephyr.
* **lib**: The [libraries](https://github.com/CogniPilot/cerebri/tree/25497bf9960c6ca74e98c1709d34c756ac4395a9/lib) in Cerebri are divided into application specific folders. The libraries are typically reusable modules that may be incorporated into an application. They interface the low level drivers with the ZROS library.
    * ***actuate***: Deals with actuating motors, servos, sound, lights etc.
    * ***core***: Common application code and system workqueues.
    * ***dream***: Simulation specific modules.
    * ***sense***: Interfaces sensor drivers with the ZROS module
    * ***synapse***: Communicaiton based modules
* **app**: The application folder is where the vehicle finite state machine, control, and estimation code reside. By tailoring these components to a specific vehicle and use case it makes it more flexible for users to adapt and it also makes the verification tasks simpler as there is less code dealing with generalizations and abstractions to allow reuse on multiple vehicles.

This structure allows for focus on the applications specific code for verification and validation. The state machine of the [B3RB](../reference_systems/b3rb/about.md) for example is written so that it can be easily adapted for [model checking](https://en.wikipedia.org/wiki/Model_checking). The algorithms in [`Cyecca`](../tools/cyecca/about.md) can also be analyzed with a dynamic model of the system to provide the mechanisms for hybrid model checking.
