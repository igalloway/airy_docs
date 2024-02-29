# NavQPlus set up for CogniPilot with ROS 2 Humble

??? tip "Looking for instructions on how to also install on a development computer?"

    [Click here to get instructions on how to setup and configure a development computer.](../../../getting_started/install.md)

??? tip "Already previously followed all the steps to flash and configure the image on the NavQPlus and want to jump to installing CogniPilot on it?"

    [Click here to jump to installing CogniPilot on NavQPlus.](#install-cognipilot-through-included-script)

??? info "About this guide"
    These directions are written for someone with experience with embedded Linux and basic embedded computers.

## Step-by-step overview
 
1. **[Download the pre-built latest image](https://github.com/rudislabs/navqplus-images/releases/latest)** with Ubuntu[^1] 22.04 and ROS 2[^3] Humble, exact instructions for that release image are included on the [release documentation](https://github.com/rudislabs/navqplus-images/releases/latest) to use in conjunction with this guide.
   
Link to latest image: `https://github.com/rudislabs/navqplus-images/releases/latest`

2. Extract the image `navqplus-image-<version>.wic` from the compressed downloaded file `navqplus-image-<version>.wic.zstd` and flash it to the [EMMC](#flashing-the-emmc), [exact copy and paste instructions](https://github.com/rudislabs/navqplus-images/releases/latest) are on the release page.
3. [Log in for the first time](#log-in-for-the-first-time) by connecting to another computer using the [USB to UART adapter](#usb-to-uart-adapter), [ethernet adapter](#ethernet) or [centermost (USB 2) USB-C® port](#usb-c-gadget-ethernet).[^2]
4. [Configure WiFi, System User Name and Password.](#configuring-wifi-system-hostname-username-or-password)
5. [Connect to NavQPlus over WiFi](#connecting-to-navqplus-over-wifi)
6. [Install CogniPilot by running the included installer script.](#install-cognipilot-through-included-script)

## Flashing the eMMC
To flash the eMMC on the NavQPlus use the [uuu](https://github.com/rudislabs/navqplus-images/releases/latest) tool as part of the downloadable assests from the release.

Once `uuu` has downloaded make sure to set it as executable.

```bash title="Make uuu executable:"
chmod a+x uuu
```

find the [boot switches](#boot-switches) on the NavQPlus and flip them to the "Flash" mode.

Then, connect NavQPlus to the computer with the downloaded release using the leftmost (USB 1) USB-C® port and the two flash status lights should light up. 

??? picture "Flash eMMC hookup and status lights."

    ![Flash eMMC hookup and status lights.](data/flash_hookup_lights.jpg "Flash eMMC hookup and status lights")


Make sure that the NavQPlus is recognized by `uuu`.

```bash title="Check if uuu sees NavQPlus:"
./uuu -lsusb
```
??? picture "Found device with uuu."

    ![Found device with uuu.](data/uuu_ls.png "uuu found device")

If it shows that a device is connected, continue to flashing. To flash the board, use the general command below or [copy and paste the specific command](https://github.com/rudislabs/navqplus-images/releases/latest) from the release.

```bash title="Use uuu to flash eMMC with image:"
sudo ./uuu -b emmc_all navqplus-image-<version>.bin-flash_evk navqplus-image-<version>.wic
```

Once this process has finished, make sure that the flash was successful. If so, configure the [boot switches](#boot-switches) to boot from eMMC.

??? picture "Successful eMMC flash."

    ![Successful eMMC flash.](data/uuu_emmc.png "Flashed eMMC Successfully")

??? question "uuu gave a weird output abort message after flashing, did it work correctly?"

    There is a know issue where uuu will throw an assertion failed error as seen below, however, the image is flashed correctly and the remaining steps setup and install steps can be followed.
    ![UUU assertion failed.](data/uuu_assert.png "UUU assertion failed.")

## Boot Switches

NavQPlus can be configured to boot from either SD card or eMMC. It also has a flash mode that allows for to flashing either the eMMC or SD card over USB-C®. See the table below for the boot switch configuration. Note we suggest to only flash and run from eMMC and leave the SD card for external storage.

| Mode  | Switch 1 | Switch 2 |
| ----- | -------- | -------- |
|  SD   |    ON    |    ON    |
| eMMC  |    OFF   |    ON    |
| Flash |    ON    |    OFF   |


## Log in for the first time

Power on the NavQPlus by plugging in a USB-C® cable to the centermost (USB 2) USB-C® port or the 5 pin JST-GH power port if not powering over the centermost (USB 2) USB-C® port. NavQPlus will boot, and display that it is fully booted with the status LEDs on board. The 3 LEDs by the USB1 port should be on, as well as two LEDs next to the CAN bus connectors.

To log into NavQPlus, choose between using the [included USB to UART adapter](#usb-to-uart-adapter), [Industrial Ethernet](#ethernet), or [USB-C® with gadget ethernet mode](#usb-c-gadget-ethernet). The default username/password combo is as follows:

**Username: user**

**Password: user**

### USB to UART adapter
Connect the included USB to UART adapter to the UART2 port on the NavQPlus, and open a serial console application with a baud rate of 115200 8N1. Press enter if there is no output on the screen to get a log-in prompt.

```bash title="Use screen to connect over USB to UART:"
screen /dev/ttyUSB<#> 115200
```
??? tip "How to close cleanly out of `screen`."
    To exit `screen` cleanly when done press simultaneously `Ctrl Shift A` followed by typing `k` then `y`.

### Ethernet
Connect the included IX Industrial Ethernet cable to NavQPlus, and connect the RJ45 connector to another computer, switch, or router on the local network. Log into NavQPlus over SSH.

```bash title="Connect to NavQPlus over ssh:"
ssh <username>@<hostname>.local
```

```bash title="Another way to connect to NavQPlus over ssh depending on network setup:"
ssh <username>@<hostname>
```

??? tip "Changing hostname"
    Default hostname is `imx8mpnavq`. The [hostname can be changed](#change-hostname) and is suggested to be changed if running multiple NavQPlus on the same network.

### USB-C® Gadget Ethernet
The IP address of the `usb0` network interface on NavQPlus is statically assigned to 192.168.186.3. To use the USB-C® gadget ethernet to connect to the NavQPlus, assign a static IP on the connecting computers existing gadget ethernet interface. The network configuration is as follows:

**IP Address:** 192.168.186.2

**Network Mask:** 255.255.255.0

??? picture "Adding the network configuration to Network Manager."

    ![Network Manager connection profile.](data/usb_network.png "USB-C® gadget ethernet network connection")

Once USB-C® gadget ethernet interface is set up on the connected computer, connect over SSH.

```bash title="Connect to NavQPlus over ssh:"
ssh <username>@<hostname>.local
```

```bash title="Another way to connect to NavQPlus over ssh depending on network setup:"
ssh <username>@<hostname>
```

??? tip "Changing hostname"
    Default hostname is `imx8mpnavq`. The [hostname can be changed](#change-hostname) and is suggested to be changed if running multiple NavQPlus on the same network.

## Configuring WiFi, System Hostname, Username or Password

### Configuring WiFi on NavQPlus
To connect NavQPlus to a WiFi network, use the `nmcli` command. The interface is relatively straightforward, to connect with `nmcli`.

```bash title="Connect NavQPlus to WiFi using nmcli:"
sudo nmcli device wifi connect <network_name> password "<password>"
```

If struggling to connect to a network, see if the network is visible.

```bash title="Check WiFi networks visible to the NavQPlus:"
sudo nmcli device wifi list
```

Once connected to the WiFi network the NavQPlus will continue to connect to that network even after a reboot.

??? question "What WiFi network is the NavQPlus currently connected to?"

    To see what WiFi network the NavQPlus is currently connected to run previous command without `sudo`.
    
    ```bash title="Check current WiFi network NavQPlus is connected to:"
    nmcli device wifi list
    ```

    Or if running with `sudo` it will be the network preceded with a star.

### OPTIONAL - Configuring System Hostname, Username or Password

Optionally, to change the default hostname, username, or password, see below.

#### Change Hostname
```bash title="Change the hostname:"
hostnamectl set-hostname <new_hostname>
```

#### Change Username
!!! danger
    **Changing the `username` can be dangerous and possibly result in a broken system state requiring a re-flash.**
```bash title="Change the username:"
usermod -l <new_username> user
mv /home/user /home/<new_username>
```

#### Change Password
```bash title="Change the password:"
passwd
```

## Connecting to NavQPlus over WiFi
Once setup to connect over a local WiFi network, SSH into the NavQPlus.

```bash title="Connect to NavQPlus over ssh:"
ssh <username>@<hostname>.local
```

```bash title="Another way to connect to NavQPlus over ssh depending on network setup:"
ssh <username>@<hostname>
```

??? tip "Changing hostname"
    Default hostname is `imx8mpnavq`. The [hostname can be changed](#change-hostname) and is suggested to be changed if running multiple NavQPlus on the same network.

## Install CogniPilot through included script

Included in the image is an installation script that auto-updates when run. Before running make sure that the NavQPlus is connected to the internet on a network that allows it to download from github and Ubuntu servers.

In the home directory there is a simple helper script that downloads and runs the latest [CogniPilot NavQPlus installer](https://github.com/CogniPilot/helmet/blob/main/install/navqplus_install.sh).

??? tip "Cloning with ssh keys:"
    If you want to use [SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) with github on the NavQPlus you must first add or create them on the device. Otherwise you will need to answer `n` when asked to clone using already setup github ssh keys.

```bash title="Install CogniPilot on NavQPlus:"
./install_cognipilot.sh
```

???+ tip "When prompted to choose whether or not to use ssh-keys:"

    * ***y*** to [clone with ssh keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh), best for development work but only select if ssh keys are already present and setup with GitHub.
    * ***n*** to clone with https, best for users who do not plan to make modifications or develop.

???+ tip "When prompted to choose whether or not to optimize runtime performance:"

    **It is recommended to select `y` for runtime optimization when prompted.**

???+ tip "When prompted to choose a release:"

    1. ***airy*** for a stable non-development release.
    2. ***main*** for active development.

???+ tip "When prompted to choose a platform to build:"

    1. [***b3rb*** is an ackermann based mobile robotic platform.](../../../reference_systems/b3rb/about.md)
    2. ***elm4*** is a differential drive based mobile robotic platform.

??? question "Does CycloneDDS need configuring?"
    The NavQPlus Ubuntu 22.04 with ROS 2 Humble image uses CycloneDDS by default. Make sure to edit the default CycloneDDSConfig.xml to only allow the networks that are desired to connector over when trying to get maximal performance. An example of this is using only the WiFi device `mlan0` to connect to a ROS 2 Domain. To save performance remove the other default included interfaces `eth1` and `usb0` by [deleting those lines](https://github.com/rudislabs/NavQPlus-Resources/blob/36cf2b8e8befcd4265c7027d072b6a70d2148fd0/configs/CycloneDDSConfig.xml#L6-L7) from the NavQPlus local `~/CycloneDDSconfig.xml`.


[^1]: Ubuntu is a registered trademark of Canonical Ltd.
[^2]: USB-C® is a trademark of USB Implementers Forum.
[^3]: ROS 2 is governed by Open Robotics.
