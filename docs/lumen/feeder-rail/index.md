# Feeder Rail (Front and Rear)
## Introduction
The purpose of these work instructions is to cover the assembly process for the LumenPnP's front and rear feeder rail. These rails are used by the LumenPnP to space its two y-gantry assemblies apart. These rails also allow for auto feeders to be installed onto the LumenPnP and electronically connected via the 50x mounted feeder slots.

## Assemble feeder-blade-set
If you have not already done so, go to [this page](/feeder-connection-kit/panelized-feeder-slot) for instructions on preparing a `feeder-blade-set` for use in the LumenPnP Feeder Rails

## Assemble front-feeder-rail
### Insert extrusion into assembly jig
1. Insert a piece of `alu-extrusion` into the `feeder-rail-asm-jig`
	<img style="height:500px;" src="img/feeder-slot-rail-2.webp">
	<img style="height:500px;" src="img/feeder-slot-rail-3.webp">
	<img style="height:500px;" src="img/feeder-slot-rail-4.webp">

### Install corner brackets
2. Loosely install a `M5x8-bolt` and `M5-t-nut` onto 2x `corner-bracket` 
	<img style="height:500px;" src="img/feeder-slot-rail-5.webp">
	<img style="height:500px;" src="img/feeder-slot-rail-6.webp">
3. Position a `corner-bracket` onto the front left side of the `alu-extrusion` previously placed in the `feeder-rail-asm-jig`
	<img style="height:500px;" src="img/feeder-slot-rail-7.webp">
	<img style="height:500px;" src="img/feeder-slot-rail-8.webp">
4. Press the `corner-bracket` downward and inward (towards the sidewall of the jig) while tightening the `M5x8-bolt` to `0.7N/M`
	<img style="height:500px;" src="img/feeder-slot-rail-9.webp">
5. Repeat the previous two steps on the opposite side of `alu-extrusion`  
	<img style="height:500px;" src="img/feeder-slot-rail-10.webp">
6. Confirm the WIP `front-feeder-rail` matches the image below
	<img style="height:500px;" src="img/feeder-slot-rail-11.webp">

### Install feeder blades
7. Collect a `feeder-blade-set` from inventory
	![](img/IMG_2607.webp)
	
10. Install `Feeder Slot Blade (#1 - #12)` onto the front left side of the `alu-extrusion`
    * Press the blade assembly downward and inward (towards the sidewall of the jig) while tightening the 5x `M5x10-bolt` to `0.7N/M`, starting with the center screw and tighening the screws in pairs moving outwards
	![](img/IMG_2608.webp)
	![](img/IMG_2609.webp)
	
11. Repeat the two previous steps to install `Feeder Slot Blade (#13 - #25)`
	![](img/IMG_2610.webp)
	![](img/IMG_2611.webp)

### Install `blade-jumper-harness`
12. Pull the WIP `front-feeder-rail` outward to remove it from `feeder-rail-asm-jig`
	![](img/IMG_2613.webp)

2. Inspect the `blade-jumper-harness`. It is **critical** that the order of the conductors in this jumper are the **exact same** for each connector when the connectors are facing the same way.
	![](img/jumper-ok.webp)
	![](img/jumper-ng.webp)
   
    !!! danger "CRITCAL"
		Even after you've checked this cable, *check it again*! It is critically important that this jumper has the exact same order of wire color for both connectors.

13. Connect `blade-jumper-harness` to the two `PH-connector` located between `Feeder Slot Blade (#1 - #12)` and `Feeder Slot Blade (#13 - #25)`
   
	![alt text](img/front-feeder-rail-wired.webp)
	![alt text](img/feeder-rail-wired-closeup.webp)

### OQC
Perform the following quality control checks:

* Feeder blades are installed sequentially from left to right
* Wiggle the installed blades to ensure no screws are loose, retightening any if needed
* Ensure the print is free of defects and fits flush to `alu-extrusion
* The 2x installed `corner-bracket` pieces are flush to the `alu-extrusion`
* Confirm `blade-jumper-harness` is installed into the blades
* Tug on the connectors to ensure they're fully connected
* Ensure the wire color order is the same for both connectors on the jumper harness

!!!success "If all checks pass, bring the completed `front-feeder-rail` to the shelf for peer-review and pack-out."

## Assemble rear-feeder-rail
This section of the work instruction will be a little less detailed than the above section on `front-feeder-rail` as it builds off the same process.

### Insert extrusion into assembly jig
1. Insert a piece of `alu-extrusion` into the `feeder-rail-asm-jig`
	<img style="height:500px;" src="img/feeder-slot-rail-2.webp">
	<img style="height:500px;" src="img/feeder-slot-rail-3.webp">
	<img style="height:500px;" src="img/feeder-slot-rail-4.webp">

### Install corner brackets
1. Loosely install a `M5x8-bolt` and `M5-t-nut` onto 4x `corner-bracket` 
	<img style="height:500px;" src="img/feeder-slot-rail-32.webp">
	<img style="height:500px;" src="img/feeder-slot-rail-33.webp">
2. Position a `corner-bracket` onto the front left side of the `alu-extrusion`
	<img style="height:500px;" src="img/feeder-slot-rail-7.webp">
	<img style="height:500px;" src="img/feeder-slot-rail-8.webp">
3. Press the `corner-bracket` downward and inward (towards the sidewall of the jig) while tightening the `M5x8-bolt` to `0.7N/M`
	<img style="height:500px;" src="img/feeder-slot-rail-9.webp">
4. Repeat the previous two steps on the opposite side of `alu-extrusion`  
	<img style="height:500px;" src="img/feeder-slot-rail-10.webp">
5. Confirm the WIP `rear-feeder-rail` matches the image below before proceeding to install 2x `corner-bracket` on the backside of the `alu-extrusion`
	<img style="height:500px;" src="img/feeder-slot-rail-11.webp">
6.	Position a `corner-bracket` onto the back right side of the `alu-extrusion`
	
	<img style="height:500px;" src="img/feeder-slot-rail-35.webp">

7. Press the `corner-bracket` downward and inward (towards the sidewall of the jig) while tightening the `M5x8-bolt` to `0.7N/M`
	<img style="height:500px;" src="img/feeder-slot-rail-36.webp">
	<img style="height:500px;" src="img/feeder-slot-rail-37.webp">
8. Repeat the previous two steps to install a `corner-bracket` onto the back left side of `alu-extrusion`  
	<img style="height:500px;" src="img/feeder-slot-rail-38.webp">
9. Confirm the WIP `rear-feeder-rail` matches the image below
	<img style="height:500px;" src="img/feeder-slot-rail-39.webp">

### Install feeder blades

2. Install `Feeder Slot Blade (#26 - #37)` onto the left side of `alu-extrusion`
    * Press the blade downward and inward (towards the sidewall of the jig) while tightening the 5x `M5x10-bolt` to `0.7N/M`, starting with the center screw and tighening the screws in pairs moving outwards
	
	![](img/IMG_2608.webp)
	![](img/IMG_2609.webp)

3. Repeat the two previous steps to install `Feeder Slot Blade (#38 - #50)`
	![](img/IMG_2610.webp)
	![](img/IMG_2611.webp)

### Install `blade-jumper-harness`
1. Pull the WIP `rear-feeder-rail` outward to remove it from `feeder-rail-asm-jig`
	![](img/IMG_2619.webp)

2. Inspect the `blade-jumper-harness`. It is **critical** that the order of the conductors in this jumper are the **exact same** for each connector when the connectors are facing the same way.
	![](img/jumper-ok.webp)
	![](img/jumper-ng.webp)
   
    !!! danger "CRITCAL"
		Even after you've checked this cable, *check it again*! It is critically important that this jumper has the exact same order of wire color for both connectors.

3.  Connect `blade-jumper-harness` to the two `PH-connector` located between `Feeder Slot Blade (#26 - #37)` and `Feeder Slot Blade (#38 - #50)`

	![alt text](img/rear-feeder-rail-wired.webp)
	![alt text](img/feeder-rail-wired-closeup.webp)

### OQC
Perform the following quality control checks:

* Feeder blades are installed sequentially from left to right
* Wiggle the installed blades to ensure none are loose, retightening any if needed
* The 2x installed `corner-bracket` pieces are flush to the `alu-extrusion`
* The 4x installed `corner-bracket` pieces are flush to the `alu-extrusion`
* Confirm `blade-jumper-harness` is installed into the blades
* Tug on the connectors to ensure they're fully connected
* Ensure the wire color order is the same for both connectors on the jumper harness

!!!success "If all checks pass, bring the completed `rear-feeder-rail` to the shelf for peer-review and pack-out"
