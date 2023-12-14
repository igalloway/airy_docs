# B3RB Platform Overview

## Example of Navigation
<video controls>
  <source src="../videos/b3rb.mp4" type="video/mp4">
</video>

## Status Sounds

These sounds allow for audio based system diagnosis.

### **Startup Sound**
---
#### ***Flight of the Alicanto***
Startup sound signifies the system has booted.

<audio controls="controls">
  <source type="audio/mp3" src="../sounds/airy.mp3"></source>
</audio>

### **State Change Request Sounds**
---
#### Rejected State Change Request
Low tone followed by mid-high-low-mid-high sinusoid.

<audio controls="controls">
  <source type="audio/mp3" src="../sounds/reject.mp3"></source>
</audio>

### **Mode Sounds**
---
#### Manual Sound
Morse Code ***1*** for mode enum ***(. - - - -)***

<audio controls="controls">
  <source type="audio/mp3" src="../sounds/manual.mp3"></source>
</audio>

#### CMD_VEL Sound
Morse Code ***3*** for mode enum ***(. . . - -)***

<audio controls="controls">
  <source type="audio/mp3" src="../sounds/cmd_vel.mp3"></source>
</audio>

#### Calibration Sound
Morse Code ***4*** for mode enum ***(. . . . -)***

<audio controls="controls">
  <source type="audio/mp3" src="../sounds/calibration.mp3"></source>
</audio>

### **Safety Sounds**
---
#### Safety Off Sound
Morse Code ***S*** increasing long octives ***(- - -)***

<audio controls="controls">
  <source type="audio/mp3" src="../sounds/safety_off.mp3"></source>
</audio>

#### Safety On Sound
Morse Code ***S*** decreasing long octives ***(- - -)***

<audio controls="controls">
  <source type="audio/mp3" src="../sounds/safety_on.mp3"></source>
</audio>

### **Arming Sounds**
---
#### Arm Sound
Morse Code ***A*** mid-high tone ***(. -)***

<audio controls="controls">
  <source type="audio/mp3" src="../sounds/arm.mp3"></source>
</audio>

#### Disarm Sound
Morse Code ***A*** mid-low tone ***(. -)***

<audio controls="controls">
  <source type="audio/mp3" src="../sounds/disarm.mp3"></source>
</audio>

### **Connection Loss Sounds**
---
#### Joy Input Loss Sound
Morse Code ***E*** every 3 seconds ***( . )*** (sounds only after safety is off).

<audio controls="controls">
  <source type="audio/mp3" src="../sounds/joy_loss.mp3"></source>
</audio>

### **Fuel Status Sounds**
---
#### Fuel Low Sound
Morse Code ***EK*** every 10 seconds ***( . - . - )***

<audio controls="controls">
  <source type="audio/mp3" src="../sounds/fuel_low.mp3"></source>
</audio>

#### Fuel Critical Sound
Morse Code ***EK*** continuous ***( . - . - )***

<audio controls="controls">
  <source type="audio/mp3" src="../sounds/fuel_critical.mp3"></source>
</audio>

