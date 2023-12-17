# B3RB Simulation

Simulation uses [gazebo garden](https://gazebosim.org/home) to simulate sensors and physics in the ["dream" worlds](../../dream/worlds/worlds.md) that connects to Cerebri running ontop Zephyr RTOS native_sim.

## Before running simulation

Before running the simulation for the first time make sure to have first followed the [installation for development computer guide](../../getting_started/install.md). Once at [building the workspace](../../getting_started/install.md#build-the-workspace) make sure to select `1. b3rb` for the platform. This will also build Cerebri for native_sim so the section below **["Build Cerebri for `native_sim`"](#build-cerebri-for-native_sim)** can be skipped if the `build_workspace` script was just run. If other images have been built in Cerebri since running the script make sure to follow **["Build Cerebri for `native_sim`"](#build-cerebri-for-native_sim)**

## Build Cerebri for `native_sim`

To build [Cerebri for native_sim (posix)](../../cerebri/about.md) make sure the Zephyr RTOS build environment is up to date. There is a convenience script that by default builds the `native_sim` enviroment that should be run before the  with west is up to date

## Run Electrode

To visualize and control navigation [run electrode with the preffered backend set with the gui option](../../electrode/about.md).

For electrode with the [foxglove backend](../../electrode/foxglove.md) for simulation run:
```bash
ros2 launch electrode electrode.launch.py gui:=foxglove
``` 
??? question "How do I open the foxglove studio viewer?"

    [Click here for more information on how to get foxglove studio and open it.](../../electrode/foxglove.md)

??? question "I opened foxglove, how do I connect it to the simulation?"

    After launching the foxglove websocket bridge by passing to electrode `gui:=foxglove`
    connect to it on `ws://localhost:8765`
    ![Connect foxglove with simulation websocket](images/foxglove_simulation_socket.png "Connect foxglove with simulation web socket")

??? picture "Example of depot world simulation with electrode running foxglove."

    ![B3RB Depot world simulation with foxglove](images/b3rb_depot_foxglove.png "B3RB Depot world simulation with foxglove")


For electrode with the [rviz2 backend](../../electrode/rviz2.md) for simulation run:
```bash
ros2 launch electrode electrode.launch.py gui:=rviz
``` 
??? picture "Example of depot world simulation with electrode running rviz2."

    ![B3RB Depot world simulation with rviz2](images/b3rb_depot_rviz.png "B3RB Depot world simulation with rviz2")


## Run B3RB SIL

The default dream world for B3RB is the [basic map world](../../dream/worlds/worlds.md#basic-map-world).
Run the default simulation with:
```bash
ros2 launch b3rb_gz_bringup sil.launch.py
```

??? question "My ROS 2 cerebri_bringup node is showing an error and is keeping simulation from running."

    If the simulation launch script is throwing an error about cerebri_bringup make sure that [cerebri is built, installed and sourced properly for `native_sim`](#build-cerebri-for-native_sim).

!!! tip "**If running on a machine with a powerful graphics card optionally run the more gaphics intensive [depot world](../../dream/worlds/worlds.md#depot-world).**"

    ```ros2 launch b3rb_gz_bringup sil.launch.py world:=depot```

## Video example of using the simulation
??? video "Example of using simulation with electrode running foxglove."

    <video controls>
      <source src="../videos/b3rb_depot_foxglove.mp4" type="video/mp4">
    </video>




