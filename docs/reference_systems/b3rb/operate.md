# B3RB Operation Overview

To operate the B3RB platform:

1. [Follow the B3RB setup guide](#following-the-b3rb-setup-guide).
2. [Run Electrode for B3RB](#running-electrode-for-b3rb).
3. [Launch `b3rb_bringup` on B3RB's NavQPlus](#launching-b3rb_bringup-on-the-navqplus).
4. [Understand the lights and sounds of the B3RB for fast diagnosis](#understanding-the-lights-and-sounds-of-the-b3rb-for-fast-diagnosis).
5. [Navigate Using the electrode interface](#navigating-using-the-electrode-interface).

## Following the B3RB setup guide

Make sure to have first followed the [B3RB setup guide](./setup.md).

## Running Electrode for B3RB

Choose and run the desired [Electrode backend for B3RB](./electrode.md).

## Launching `b3rb_bringup` on the NavQPlus

Shell into the NavQPlus ([typically over WiFi](../../cranium/compute/navqplus/setup.md#connecting-to-navqplus-over-wifi)).

Run the B3RB launch file.

```bash title="Run B3RB launch file." 
ros2 launch b3rb_bringup robot.launch.py
```

## Understanding the lights and sounds of the B3RB for fast diagnosis

[Using the lights and sounds on the B3RB](./status.md) is a useful way to determine the system's current status regardless of Electrode running.

## Navigating Using the electrode interface

### Video example of using B3RB
??? video "Example of using B3RB with electrode running foxglove-studio."

    <video controls>
      <source src="../videos/b3rb_electrode.mp4" type="video/mp4">
    </video>