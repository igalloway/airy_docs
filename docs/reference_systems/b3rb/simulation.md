# B3RB Simulation

## Run B3RB SIL (in JupyterLab terminal or Bash directly)

```bash
ros2 launch b3rb_gz_bringup sil.launch.py
```

!!! attention
    **If running on a machine with a more powerful graphics card optionally run more gaphics intensive depot world:**
```bash
ros2 launch b3rb_gz_bringup sil.launch.py world:=depot
```

## Simulation

Example of simulation running (depot world).

![B3RB Depot world simulation](images/b3rb_depot.png "B3RB Depot world simulation")

!!! attention
    **Use a joystick controller ([Logitech F310](https://www.logitechg.com/en-us/products/gamepads/f310-gamepad.940-000110.html) suggested) to control vehicle modes.**

## Select a Mode:

![F310](images/f310.jpg "F310")

* **A**: manual
* **X**: cmd_vel (nav2)
* **B**: auto (other cmd_vel)
* **Y**: calibration

### Manual Mode:

* **Left stick** Up/Down: throttle
* **Right stick** Left/Right: steering

### Nav2 (cmd_vel) Mode:

* Click **2D Pose Goal** and select desired location on RVIZ2 map.

### Auto Mode

* Click **2D Pose Goal** and select desired location on RVIZ2 map.

## Arming

* **START**: arm
* **BACK**: disarm


