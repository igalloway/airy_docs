# B3RB Setup

Overview of setup for the B3RB platform:

1. [Put together the physical B3RB platform](#putting-together-the-physical-b3rb-platform).
2. [Setup a development machine for B3RB](#setup-a-development-machine-for-b3rb).
3. [Setup the NavQPlus on B3RB](#setup-the-navqplus-on-b3rb).
4. [Build and flash the Cerebri image for B3RB](#build-and-flash-the-cerebri-image-for-b3rb).

## Putting together the physical B3RB platform

Please follow the links in the [hardware overview](./hardware.md).

## Setup a development machine for B3RB

Please follow the the [getting started guide for development computers](../../getting_started/install.md).

## Setup the NavQPlus on B3RB

Please follow the the [NavQPlus setup guide](../../cranium/compute/navqplus/setup.md).

## Build and flash the Cerebri image for B3RB

If choosing to use the stable Airy release, make sure Cerebri is on the airy branch.

??? question "How do I know what branch Cerebri is on?"

	```bash title="Check cerebri branch."
	cd ~/cognipilot/ws/cerebri
	git status
	```
	Which should return:
	```bash
	On branch airy
	Your branch is up to date with 'origin/airy'.

	nothing to commit, working tree clean
	```
	If it does not show that perform a `git checkout`:
	```bash title="Checkout airy branch on cerebri."
	git checkout airy
	```

### Check for updates on Cerebri

```bash title="Update Cerebri."
cd ~/cognipilot/ws/cerebri
git pull
```

### Make sure Cerebri's Zephyr dependencies are up to date with `west`

```bash title="Updating Cerebri's Zephyr dependencies with west."
cd ~/cognipilot/ws/cerebri
west update
```

### Build Cerebri B3RB image for MR CANHUBK3 with `west`

```bash title="Building Cerebri B3RB image with west."
cd ~/cognipilot/ws/cerebri
west build -b mr_canhubk3 app/b3rb -p
```

### Flash Cerebri B3RB image with `west` to MR CANHUBK3

Make sure [Segger JLink](https://www.segger.com/downloads/jlink/) is on your system and the MR CANHUBK3 is connected to the JLink programmer.

```bash title="Flashing MR CANHUBK3 with the Cerebri B3RB image using west."
cd ~/cognipilot/ws/cerebri
west flash
```
