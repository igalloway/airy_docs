# Installation for development computer

???+ tip "Looking for instructions on how to also install on a NavQPlus?"
    
    [Click here to get instructions on how to setup and configure a NavQPlus](../cranium/compute/navqplus/setup.md).
    Continue this guide for installing CogniPilot on a native development computer.

## Requirements

* [Ubuntu 22.04 host environment.](https://ubuntu.com/download/desktop)
* Stable internet connection for downloading and installing packages.

This may work on other environments but only Ubuntu 22.04 is officially supported.

## Optional before installing
### Setup SSH keys on host and GitHub

If planning to develop and make changes to code it is suggested to set up ssh keys, however, it is not strictly required to do so.

* Ensure that [ssh keys are setup](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) on host computer and GitHub to be able to clone the CogniPilot repositories with ssh.

### Setup GPG keys on host and GitHub

* Optionally [setup gpg keys](https://docs.github.com/articles/generating-a-gpg-key/) on host computer and GitHub to sign commits.

## Use CogniPilot universal installer
??? info "Using Docker instead."

    If preffering to use docker, there is a [Docker Development Container](advanced/docker.md) that may be used instead.

To install CogniPilot on a system run the following to download the universal installer and run it (**follow the prompts in the installer**):

```bash
sudo apt-get update
sudo apt-get install git wget -y
mkdir -p ~/cognipilot/installer
wget -O ~/cognipilot/installer/install_cognipilot.sh https://raw.githubusercontent.com/CogniPilot/helmet/main/install/install_cognipilot.sh
chmod a+x ~/cognipilot/installer/install_cognipilot.sh
/bin/bash ~/cognipilot/installer/install_cognipilot.sh
```

???+ tip "When prompted to choose a release:"

    1. ***airy*** for a stable non-development release.
    2. ***main*** for active development.

???+ tip "When prompted to choose installer type select **1** for **native**:"

    1. ***native*** select this for installing on development computer
    2. ***navqplus*** only if installing on a NavQPlus image that does not already have the installer on it.
    [Click here for the proper way to install on a NavQPlus.](../cranium/compute/navqplus/setup.md)

???+ tip "When prompted to choose whether or not to use ssh-keys:"

    * ***y*** to [clone with ssh keys](#setup-ssh-keys-on-host-and-github-optional), best for development work but only select if ssh keys are already present and setup with GitHub.
    * ***n*** to clone with https, best for users who do not plan to make modifications or develop.


## Build the workspace

???+ tip "The `build_workspace` script:"

     * Sets up the workspaces using vcs and yaml files provided in [helmet](../helmet/about.md).
     * Builds [Cranium](../cranium/about.md) ROS 2 workspace.
     * Builds [Cerebri](../cerebri/about.md) (Zephyr RTOS native_sim) for software-in-the-loop simulation.
     * Builds [Cyecca](../tools/cyecca/about.md) (control/estimation software).
     * Builds [Electrode](../electrode/about.md) ROS 2 workspace (ground station software).

To build the workspace run (**follow the prompts in the workspace builder**):

```bash
build_workspace
```

???+ tip "When prompted to choose whether or not to use ssh-keys:"

    * ***y*** to [clone with ssh keys](#setup-ssh-keys-on-host-and-github-optional), best for development work but only select if ssh keys are already present and setup with GitHub.
    * ***n*** to clone with https, best for users who do not plan to make modifications or develop.

???+ tip "When prompted to choose a platform to build:"
    
    1. ***b3rb*** is an ackermann based mobile robotic platform with simulation.
    2. ***elm4*** is a differential drive based mobile robotic platform with simulation.


## Platforms

Currently supported platforms in this release are B3RB and ELM4.

### Using a real platform:

* [**B3RB** hardware guide.](../reference_systems/b3rb/hardware.md)
* **ELM4** hardware guide coming soon.

### Simulating a platform:

* [**B3RB** simulation guide.](../reference_systems/b3rb/simulation.md)
* **ELM4** simulation guide coming soon.

## Convenience Scripts
### docs script

???+ tip "The `docs` script:"

     * Downloads and builds the documentation repositories for the documentation currently being read so that contributions can be made easily.
     * Allows for selection of documents to be served with mkdocs.

To view the docs offline locally or to contribute to them run (**follow the prompts for the correct docs**):

```bash
docs
```

???+ tip "When prompted to choose whether or not to use ssh-keys:"

    * ***y*** to [clone with ssh keys](#setup-ssh-keys-on-host-and-github-optional), best if contributing to the documentation but only select if ssh keys are already present and setup with GitHub.
    * ***n*** to clone with https, best for users who do not plan to contribute and only want a local viewer.

???+ tip "When prompted to choose a doc to build:"
    
    1. ***airy*** is the [airy developers guide site](https://airy.cognipilot.org).
    2. ***overview*** is the [release overview site](https://cognipilot.org).

??? question "I ran the command where are the docs?"

    [Click here to access the locally built docs on 0.0.0.0:8000](http://0.0.0.0:8000/)


### cyecca script

???+ tip "The `cyecca` script:"

     * Starts a JupyterLab instance for Cyecca to aid in developing control and estimation algorithms.

To [develop algorithms with cyecca](../tools/cyecca/about.md) run:

```bash
cyecca
```
