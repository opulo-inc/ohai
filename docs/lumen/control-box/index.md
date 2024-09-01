# LumenPnP Control Box
## Introduction
The purpose of these work instructions is to cover the assembly process for the LumenPnP's Control Box. This assembly is used by the LumenPnP to contain its microcontroller and pneumatics system.

## Prepare `control-box`

- Remove support material from the 3D printed `control-box`
	![alt text](img/IMG_1870.JPG)
	![alt text](img/IMG_1871.JPG)

- Glue 2x `M5-hex-nut` into the `control-box`

	![alt text](img/IMG_1881.JPG)
	![alt text](img/IMG_1882.JPG)
	![alt text](img/IMG_1883.JPG)

## Prepare pneumatics

### Right-side pneumatic system
- Perform the following steps:
	- Connect `vacuum-pump` to `solenoid-valve` with a 70mm piece of `6x4-soft-pvc-tubing-blue`
	- Connect `solenoid-valve` to `reduction-tee-4-6-4` with a 60mm piece of `6x4-soft-pvc-tubing-blue`
	- Adhere a `Right Valve` label to the end of the `solenoid-valve` wire

![alt text](img/right-pnumatics-annotated.JPG)
![alt text](img/IMG_1873.JPG)
![alt text](img/IMG_1874.JPG)
![alt text](img/IMG_1876.JPG)
![alt text](img/IMG_1877.JPG)

### Left-side pneumatic system
- Perform the following steps:
	- Connect `vacuum-pump` to `solenoid-valve` with a 70mm piece of `6x4-soft-pvc-tubing-red`
	- Connect `solenoid-valve` to `reduction-tee-4-6-4` with a 60mm piece of r`6x4-soft-pvc-tubing-red`
	- Adhere a `Left Valve` label to the end of the `solenoid-valve` wire

![alt text](img/left-pnumatics-annotated.JPG)
![alt text](img/IMG_1878.JPG)
![alt text](img/IMG_1879.JPG)


## Install pneumatics systems into `control-box`

### Install left-side pneumatic system

- Suspend the `vacuum-pump` in the control-box with 2x `rubber-band`, matching the arrangement shown below
	![alt text](img/IMG_1885.JPG)
- Click the `solenoid-valve` into the mounting receptacle as shown below
	![alt text](img/IMG_1884.JPG)
- Slide the `reduction-tee-4-6-4` into the mounting bracket found next to vacuum line inlet
	![alt text](img/IMG_1886.JPG)
	![alt text](img/IMG_1887.JPG)

### Install right-side pneumatic system
Repeat the above process to install the right-side pneumatic system 

![alt text](img/IMG_1888.JPG)
![alt text](img/IMG_1889.JPG)


## Bolt 2x `reduction-tee-4-6-4` to `control-box`
- Use 2x `m3x30-socket-head` and 2x `m3-hex-nut` to attach  2x `reduction-tee-4-6-4` to `control-box`
	![alt text](img/IMG_1890.JPG)
	![alt text](img/IMG_1892.JPG)
	![alt text](img/IMG_1893.JPG)

## Perform cable management
- Tuck the Left Valve and Right Valve cables into to the cable management feature on the back wall of `control-box`
	- Route the Left Valve wire underneath the tubing

	![alt text](img/IMG_1895.JPG)

- Tuck the Left Pump and Right Pump cables into the back corner of the `control-box`

	![alt text](img/IMG_1896.JPG)
	![alt text](img/IMG_1897.JPG)


## Connect vacuum lines to `motherboard-rev05`
- Prepare a 180mm piece of `pu-tube-4x2.5-blue` and `pu-tube-4x2.5-red`
- Gather 1pcs `motherboard-rev05` from inventory

	![alt text](img/IMG_1898.JPG)

- Connect the tubes
	- Connect `pu-tube-4x2.5-blue` to the vacuum sensor labled `Right Vac` 
	- Connect `pu-tube-4x2.5-red` to the vacuum sensor labeled `Left Vac` 
	
	![alt text](img/IMG_1900.JPG)

- When completed the assembly should resemble the image shown below:

	![alt text](img/IMG_1899.JPG)

## Screw `motherboard-rev05` into `control-box`
- Place motherboard-rev05 into `control-box` while sliding the USB and barrel jack ports into the cutouts on the left side of the print 
	![alt text](img/IMG_1901.JPG)
	![alt text](img/IMG_1902.JPG)

- Install motherboard-rev05 into `control-box` with 4x `m3x12-button-head-self-tapping-screw`
	- Set the torque driver to ~1.5 to avoid stripping a screw hole
![alt text](img/IMG_1906.JPG)
![alt text](img/IMG_1903.JPG)
![alt text](img/IMG_1907.JPG)


## Connect a vacuum line to each `reduction-tee-4-6-4`

- Route the vacuum lines underneath the back right motherboard standoff before plugging each tube into its respective `reduction-tee-4-6-4`
	![alt text](img/IMG_1908.JPG)
	![alt text](img/IMG_1909.JPG)

## Perform cable management
- Connect the Left Pump, Right Pump, Left Valve, and Right Valve cables into the corresponding ports on `motherboard-rev05`
	![alt text](img/IMG_1910.JPG)
- Run the cables back along the pathway between the two rows of connectors
- Add a `zip-tie` around all four cables to keep them well managed
	![alt text](img/IMG_1911.JPG)

## Serialize `control-box`
- Place a lid on control-box-asm
	
	!!!warning "Confirm that both buttons click when pressed"
	
	![alt text](img/IMG_2016.JPG)
- Slide a `box-sn-label` between `control-box` and `control-box-lid`
	![alt text](img/IMG_2017.JPG)
- Flip the `control-box-asm` over and adhere a matching `machine-serial-label` to the `control-box`  
	![alt text](img/IMG_2014.JPG)
	![alt text](img/IMG_2015.JPG)
	
!!!success "You may now proceed to Gundam Testing!"
