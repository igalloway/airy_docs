# B3RB Simulation

Simulation uses [gazebo garden](https://gazebosim.org/home) to simulate sensors and physics in the ["dream" worlds](../../dream/worlds/worlds.md).

## Run Electrode

To visualize and control navigation [run electrode with the preffered backend set with the gui option](../../electrode/about.md).

For electrode with the [foxglove backend](../../electrode/foxglove.md) for simulation run:
```bash
ros2 launch electrode electrode.launch.py gui:=foxglove
``` 
??? question "How do I open the foxglove studio viewer?"

    [Click here for more information on how to get foxglove studio and open it.](../../electrode/foxglove.md)

??? question "I opened foxglove, what do I connect it to for simulation?"

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

!!! tip "**If running on a machine with a powerful graphics card optionally run the more gaphics intensive [depot world](../../dream/worlds/worlds.md#depot-world).**"

    ```ros2 launch b3rb_gz_bringup sil.launch.py world:=depot```

## Video example of using the simulation
??? video "Example of using simulation with electrode running foxglove."

    <video controls>
      <source src="../videos/b3rb_depot_foxglove.mp4" type="video/mp4">
    </video>




