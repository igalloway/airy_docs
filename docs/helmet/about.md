# Helmet Overview

[Helmet](https://github.com/cognipilot/helmet) is the CogniPilot package distribution list, similar to [rosdistro](https://github.com/ros/rosdistro).

## Folders

* dream: This folder contains the packages lists necessary for simulation.
* install: Used to hold the install scripts for deployment. These install scripts are also used for docker image creation.
* navqplus: Used to hold releveant packages for the onboard computer.
* read\_only: Alternate urls for read only cloning using https instead of ssh.

## Cloning Helmet

```bash
cd ~/cognipilot
```

Cloning with ssh keys:

```bash
git clone git@github.com:CogniPilot/helmet.git
```

Cloning without ssh keys:

```bash
git clone https://github.com/CogniPilot/helmet.git
```

## Deploying using Native Install Script

Run the install script and follow the prompts.

```bash
./helmet/install/native_install.sh
```

## Manually building the Workspace for Software-in-the-loop Simulation

Helmet relies upon the vcs tool provided with ros. After adding the APT ROS reposities, it may be install via:

```bash
sudo apt install python3-vcstool
```

Now we can use vcs to import the relevant git repositories for our workspace.

```bash
cd ~/cognipilot
vcs import < helmet/dream/base.yaml
vcs import < helmet/dream/b3rb.yaml
```
