# B3RB Status Lighting and Sounds

## Status Lights
The tailights on the B3RB are used for showing the current system status and breathe to show the system is alive.
??? question "My status lights are not breathing, what's wrong?"

    * If the status lights are not breathing and there is a [startup sound](#flight-of-the-alicanto) check your board for:
        * LED connection to [SPI2 port on MR CANHUBK3](../../cerebri/boards/nxp_mr_canhubk3.md).
        * cerebri/app/b3rb/prj.conf setting for [CONFIG_CEREBRI_B3RB_LIGHTING=y](https://github.com/CogniPilot/cerebri/blob/e201ca1f44f937eae2e36f3125932a732e6b79d0/app/b3rb/prj.conf#L14)
        * cerebri/app/b3rb/prj.conf setting for [CONFIG_CEREBRI_ACTUATE_LED_ARRAY=y](https://github.com/CogniPilot/cerebri/blob/e201ca1f44f937eae2e36f3125932a732e6b79d0/app/b3rb/prj.conf#L18)
        * cerebri/app/b3rb/boards/mr_canhubk3.conf setting for [CONFIG_LED_STRIP=y CONFIG_APA102_STRIP=y](https://github.com/CogniPilot/cerebri/blob/e201ca1f44f937eae2e36f3125932a732e6b79d0/app/b3rb/boards/mr_canhubk3.conf#L5-L6)
    * If the status lights are not breathing and there is no [startup sound](#flight-of-the-alicanto) it can be a sign there was a potential power event that occurred and the PMIC triggered the FS26 watchdog.
    Steps to fix watchdog timeout:
        1. Check all wiring is plugged in correctly.
        2. Power off the board.
        4. Remove the jumper JP1 (pins 1-2 open), which is connected by default.
        5. Power on the board.
        6. Reconnect the jumper JP1 (pins 1-2 shorted).


---
### **Startup Lights**
??? lighting "[ :octicons-dot-fill-24:{.p_g} :octicons-dot-fill-24:{.p_g} :octicons-dot-fill-24:{.p_w} ]  [ :octicons-dot-fill-24:{.p_w} :octicons-dot-fill-24:{.p_g} :octicons-dot-fill-24:{.p_g} ] Startup breathing light pattern [Safety On, Disarm, Mode Unknown]."

---
### **Safety Lights**
#### Safety On Lights
??? lighting "[ :octicons-dot-fill-24:{.p_g} :octicons-dot-fill-24: :octicons-dot-fill-24: ]  [ :octicons-dot-fill-24: :octicons-dot-fill-24: :octicons-dot-fill-24:{.p_g} ] The outer set of lights are **green** when the **Safety** is **On**."

#### Safety Off Lights
??? lighting "[ :octicons-dot-fill-24:{.p_r} :octicons-dot-fill-24: :octicons-dot-fill-24: ]  [ :octicons-dot-fill-24: :octicons-dot-fill-24: :octicons-dot-fill-24:{.p_r} ] The outer set of lights are **red** when the **Safety** is **Off**."

---
### **Arming and Critical Fuel Lights**
#### Disarmed Lights
??? lighting "[ :octicons-dot-fill-24: :octicons-dot-fill-24:{.p_g} :octicons-dot-fill-24: ]  [ :octicons-dot-fill-24: :octicons-dot-fill-24:{.p_g} :octicons-dot-fill-24:] The middle set of lights are **green** when **Disarmed**."

#### Armed Lights
??? lighting "[ :octicons-dot-fill-24: :octicons-dot-fill-24:{.p_r} :octicons-dot-fill-24: ]  [ :octicons-dot-fill-24: :octicons-dot-fill-24:{.p_r} :octicons-dot-fill-24: ] The middle set of lights are **red** when **Armed**."

#### Fuel Critical Lights
??? lighting "[ :octicons-dot-fill-24: :octicons-dot-fill-24:{.p_y} :octicons-dot-fill-24: ]  [ :octicons-dot-fill-24: :octicons-dot-fill-24:{.p_y} :octicons-dot-fill-24: ] The middle set of lights are **yellow** when **Fuel is Critical**."

---
### **Mode Lights**
#### Mode Unknown Lights
??? lighting "[ :octicons-dot-fill-24: :octicons-dot-fill-24: :octicons-dot-fill-24:{.p_w} ]  [ :octicons-dot-fill-24:{.p_w} :octicons-dot-fill-24: :octicons-dot-fill-24:] The inner set of lights are **white** when **Mode Unknown**."

#### Mode Manual Lights
??? lighting "[ :octicons-dot-fill-24: :octicons-dot-fill-24: :octicons-dot-fill-24:{.p_g} ]  [ :octicons-dot-fill-24:{.p_g} :octicons-dot-fill-24: :octicons-dot-fill-24:] The inner set of lights are **green** when **Mode Manual**."

#### Mode CMD_VEL Lights
??? lighting "[ :octicons-dot-fill-24: :octicons-dot-fill-24: :octicons-dot-fill-24:{.p_b} ]  [ :octicons-dot-fill-24:{.p_b} :octicons-dot-fill-24: :octicons-dot-fill-24:] The inner set of lights are **blue** when **Mode CMD_VEL**."

#### Mode Calibration Lights
??? lighting "[ :octicons-dot-fill-24: :octicons-dot-fill-24: :octicons-dot-fill-24:{.p_y} ]  [ :octicons-dot-fill-24:{.p_y} :octicons-dot-fill-24: :octicons-dot-fill-24:] The inner set of lights are **yellow** when **Mode Calibration**."

---

---
## Status Sounds
These sounds allow for audio based system diagnosis.

---
### **Startup Sound**
#### ***Flight of the Alicanto***
??? sound "**Flight of the Alicanto** startup sound signifies the system has booted."

    <audio controls="controls">
      <source type="audio/mp3" src="../sounds/airy.mp3"></source>
    </audio>

??? question "I plugged power in but didn't hear the sound, what's wrong?"


    * If the [status lights are breathing](#startup-lights) but there is no sound check your board setup for:
        * Proper ADAP board revision (Rev C).
        * Buzzer connection to GPS port on ADAP.
        * prj.conf setting for [CONFIG_CEREBRI_ACTUATE_SOUND=y](https://github.com/CogniPilot/cerebri/blob/e201ca1f44f937eae2e36f3125932a732e6b79d0/app/b3rb/prj.conf#L19)
    * If there is no startup sound when powered on and the [status lights are not breathing](#startup-lights) there is a potential that a power event occurred and the PMIC triggered the FS26 watchdog. Steps to fix watchdog timeout:
        1. Check all wiring is plugged in correctly.
        2. Power off the board.
        4. Remove the jumper JP1 (pins 1-2 open), which is connected by default.
        5. Power on the board.
        6. Reconnect the jumper JP1 (pins 1-2 shorted).

---
### **State Change Request Sounds**
#### Rejected State Change Request

??? sound "Low tone followed by mid-high-low-mid-high sinusoid."

    <audio controls="controls">
      <source type="audio/mp3" src="../sounds/reject.mp3"></source>
    </audio>

??? question "I keep hearing this rejection sound, what is causing it?"

    * The rejection sound comes from the [Finite State Machine (FSM)](https://github.com/CogniPilot/cerebri/blob/e201ca1f44f937eae2e36f3125932a732e6b79d0/app/b3rb/src/fsm.c#L168-L244) rejecting a transition request by the request not passing the transition guards.
    * More information about the request rejection can be seen in with: 
        * `ros2 topic echo /cerebri/out/status` 
        * Electrode below the fuel gauge in the Foxglove layout. 


---
### **Mode Sounds**
#### Manual Sound
??? sound "Morse Code ***1*** for manual mode enum ***(. - - - -)***"

    <audio controls="controls">
      <source type="audio/mp3" src="../sounds/manual.mp3"></source>
    </audio>

#### CMD_VEL Sound
??? sound "Morse Code ***3*** for CMD_VEL mode enum ***(. . . - -)***"

    <audio controls="controls">
      <source type="audio/mp3" src="../sounds/cmd_vel.mp3"></source>
    </audio>

#### Calibration Sound
??? sound "Morse Code ***4*** for calibration mode enum ***(. . . . -)***"

    <audio controls="controls">
      <source type="audio/mp3" src="../sounds/calibration.mp3"></source>
    </audio>

---
### **Safety Sounds**
#### Safety Off Sound
??? sound "Morse Code ***S*** increasing long octaves ***(- - -)***"

    <audio controls="controls">
      <source type="audio/mp3" src="../sounds/safety_off.mp3"></source>
    </audio>

#### Safety On Sound
??? sound "Morse Code ***S*** decreasing long octaves ***(- - -)***"

    <audio controls="controls">
      <source type="audio/mp3" src="../sounds/safety_on.mp3"></source>
    </audio>

---
### **Arming Sounds**
#### Arm Sound
??? sound "Morse Code ***A*** mid-high tone ***(. -)***"

    <audio controls="controls">
      <source type="audio/mp3" src="../sounds/arm.mp3"></source>
    </audio>

#### Disarm Sound
??? sound "Morse Code ***A*** mid-low tone ***(. -)***"

    <audio controls="controls">
      <source type="audio/mp3" src="../sounds/disarm.mp3"></source>
    </audio>

---
### **Connection Loss Sounds**
#### Joy Input Loss Sound
??? sound "Morse Code ***E*** every 3 seconds ***( . )*** (sounds only after safety is off)."

    <audio controls="controls">
      <source type="audio/mp3" src="../sounds/joy_loss.mp3"></source>
    </audio>

---
### **Fuel Status Sounds**
#### Fuel Low Sound
??? sound "Morse Code ***EK*** every 10 seconds ***( . - . - )***"

    <audio controls="controls">
      <source type="audio/mp3" src="../sounds/fuel_low.mp3"></source>
    </audio>

#### Fuel Critical Sound
??? sound "Morse Code ***EK*** continuous ***( . - . - )***"

    <audio controls="controls">
      <source type="audio/mp3" src="../sounds/fuel_critical.mp3"></source>
    </audio>

