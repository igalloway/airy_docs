# Installation for development computer

## Requirements

* Ubuntu 22.04 host environment

This may work on other environments but only Ubuntu 22.04 is officially supported.

## Setup SSH keys on Host and GitHub

* Ensure that you have [setup your ssh keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) on host computer and GitHub to be able to clone the CogniPilot repositories.

## Setup GPG keys on Host and GitHub (Optional)

* Optionally you can also [setup your gpg keys](https://docs.github.com/articles/generating-a-gpg-key/) on host computer and GitHub to sign your commits.

## Install Git

```bash
sudo apt install git
```

## Docker Option

If preffering to use docker, there is a [Docker Development Container](advanced/docker.md) that may be used.

## Clone Helmet

```bash
mkdir -p ~/cognipilot
cd ~/cognipilot
git clone -b airy git@github.com:cognipilot/helmet
```

## Run Install Script (If not using docker)

```bash
~/cognipilot/helmet/install/native_install.sh
. ~/.profile
```

## Convenience Script Examples

### build\_b3rb\_SIL

```bash
build_b3rb_sil
```

This command executes the script [build_b3rb_SIL](https://github.com/CogniPilot/helmet/blob/main/install/resources/build_b3rb_sil).

This script:

 * Sets up the vcs workspaces based on yaml files provided in helmet.
 * Builds the cranium ROS 2 workspace
 * Builds Cerebri native_posix software-in-the-loop simuliation
 * Builds Cyecca (control/estimation software)
 * Builds Electrode (ground station software)

### docs

```bash
docs
```

This command executes the script [docs](https://github.com/CogniPilot/helmet/tree/main/install/resources).

This script:

* Downloads and builds the documentation repository for the documentation currently being read so that contributions can be made easily.


### cyecca

```bash
cyecca
```

This script:

* Starts a JupyterLab instance for Cyecca to aid in developing algorithms.


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

![B3RB Depot world simulation](data/b3rb_depot.png "B3RB Depot world simulation")

!!! attention
    **Use a joystick controller ([Logitech F310](https://www.logitechg.com/en-us/products/gamepads/f310-gamepad.940-000110.html) suggested) to control vehicle modes.**

## Select a Mode:

![F310](data/f310.jpg "F310")

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
