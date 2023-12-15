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

