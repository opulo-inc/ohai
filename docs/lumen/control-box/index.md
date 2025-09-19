# LumenPnP Control Box

## Introduction

The purpose of these work instructions is to cover the assembly process for the LumenPnP's Control Box. This assembly is used by the LumenPnP to contain its microcontroller and pneumatics system.

!!!warning "If you are preparing a `diy-control-box` for individual sale you must also follow the [steps listed in  DIY Control Box](https://ohai.opulo.io/diy-components/diy-control-box)."
	If you are making a DIY Control Box - follow these docs like normal until the `Gundam Testing` section before going to the above link.

## Prepare `control-box`

- Remove support material from the 3D printed `control-box`
	![alt text](img/IMG_1870.webp)
	![alt text](img/IMG_1871.webp)

- Glue 2x `M5-hex-nut` into the `control-box`

	![alt text](img/IMG_1881.webp)
	![alt text](img/IMG_1882.webp)
	![alt text](img/IMG_1883.webp)

## Prepare pneumatics

### Right-side pneumatic system

- Perform the following steps:
	- Connect `vacuum-pump` to `solenoid-valve` with a 70mm piece of `6x4-soft-pvc-tubing-blue`
	- Connect `solenoid-valve` to `reduction-tee-4-6-4` with a 60mm piece of `6x4-soft-pvc-tubing-blue`
	- Adhere a `Right Valve` label to the end of the `solenoid-valve` wire

![alt text](img/right-pnumatics-annotated.webp)
![alt text](img/IMG_1873.webp)
![alt text](img/IMG_1874.webp)
![alt text](img/IMG_1876.webp)
![alt text](img/IMG_1877.webp)

### Left-side pneumatic system

- Perform the following steps:
	- Connect `vacuum-pump` to `solenoid-valve` with a 70mm piece of `6x4-soft-pvc-tubing-red`
	- Connect `solenoid-valve` to `reduction-tee-4-6-4` with a 60mm piece of r`6x4-soft-pvc-tubing-red`
	- Adhere a `Left Valve` label to the end of the `solenoid-valve` wire

![alt text](img/left-pnumatics-annotated.webp)
![alt text](img/IMG_1878.webp)
![alt text](img/IMG_1879.webp)

## Install pneumatics systems into `control-box`

### Install left-side pneumatic system

- Suspend the `vacuum-pump` in the control-box with 2x `rubber-band`, matching the arrangement shown below
	![alt text](img/IMG_1885.webp)
- Click the `solenoid-valve` into the mounting receptacle as shown below
	![alt text](img/IMG_1884.webp)
- Slide the `reduction-tee-4-6-4` into the mounting bracket found next to vacuum line inlet
	![alt text](img/IMG_1886.webp)
	![alt text](img/IMG_1887.webp)

### Install right-side pneumatic system
Repeat the above process to install the right-side pneumatic system

![alt text](img/IMG_1888.webp)
![alt text](img/IMG_1889.webp)

## Bolt 2x `reduction-tee-4-6-4` to `control-box`

- Use 2x `m3x30-socket-head` and 2x `m3-hex-nut` to attach  2x `reduction-tee-4-6-4` to `control-box`
	![alt text](img/IMG_1890.webp)
	![alt text](img/IMG_1892.webp)
	![alt text](img/IMG_1893.webp)

## Perform cable management
- Tuck the Left Valve and Right Valve cables into to the cable management feature on the back wall of `control-box`
	- Route the Left Valve wire underneath the tubing

	![alt text](img/IMG_1895.webp)

- Tuck the Left Pump and Right Pump cables into the back corner of the `control-box`

	![alt text](img/IMG_1896.webp)
	![alt text](img/IMG_1897.webp)

## Connect vacuum lines to `motherboard-rev05`

- Prepare a 145mm piece of `pu-tube-4x2.5-blue`
- Prepare a 165mm piece of `pu-tube-4x2.5-red`
- Gather 1pcs `motherboard-rev05` from inventory

	![alt text](img/IMG_1898.webp)

- Connect the tubes
	- Connect `pu-tube-4x2.5-blue` to the vacuum sensor labled `Right Vac`
	- Connect `pu-tube-4x2.5-red` to the vacuum sensor labeled `Left Vac`

	![alt text](img/IMG_1900.webp)

- When completed the assembly should resemble the image shown below:

	![alt text](img/IMG_1899.webp)

## Screw `motherboard-rev05` into `control-box`

- Place motherboard-rev05 into `control-box` while sliding the USB and barrel jack ports into the cutouts on the left side of the print
	![alt text](img/IMG_1901.webp)
	![alt text](img/IMG_1902.webp)

- Install motherboard-rev05 into `control-box` with 4x `m3x12-button-head-self-tapping-screw`
	- Set the torque driver to ~1.5 to avoid stripping a screw hole
![alt text](img/IMG_1906.webp)
![alt text](img/IMG_1903.webp)
![alt text](img/IMG_1907.webp)

## Connect a vacuum line to each `reduction-tee-4-6-4`

- Route the vacuum lines underneath the back right motherboard standoff before plugging each tube into its respective `reduction-tee-4-6-4`
	![alt text](img/IMG_1908.webp)
	![alt text](img/IMG_1909.webp)

## Perform cable management

- Connect the Left Pump, Right Pump, Left Valve, and Right Valve cables into the corresponding ports on `motherboard-rev05`
	![alt text](img/IMG_1910.webp)
- Run the cables back along the pathway between the two rows of connectors
- Add a `zip-tie` around all four cables to keep them well managed
	![alt text](img/IMG_1911.webp)

!!!success "You may now proceed to Gundam Testing!"

## Gundam Testing

- Install `control-box-asm` into Gundam
	![alt text](img/connect-gundam5.webp)
	![alt text](img/connect-gundam6.webp)
- Remove `control-box-lid` and set it aside
	![alt text](img/connect-gundam1.webp)
- Connect the vacuum tubes, being sure to match the colors up correctly
	![alt text](img/connect-gundam7.webp)
	![alt text](img/connect-gundam4.webp)
- Begin to connect the Gundam jig's cables into `motherboard-rev05`
	![alt text](img/connect-gundam8.webp)
	![alt text](img/connect-gundam3.webp)
	![alt text](img/connect-gundam2.webp)
- Proceed to connect USB-B cable to the motherboard.
- Hold the `BOOT` button on the motherboard, and plug in the 24v DC barrel jack while holding it. After two seconds, you can stop pressing `BOOT`.
- In a new terminal window, type `flashmarlin` to install the firmware onto the motherboard.
- Once complete, press the `RESET` button on the motherboard.
- Open the Gundam test software.
  - If it's not already open, in a new terminal window, just type `gundam`.

- Select the “REV05-Mobo.json” test from the dropdown menu, then hit “Run Test”.

- Perform each of the tests in Gundam, and follow the prompts.

- If some of the tests fail, continue through the rest of the test until every test has been run.

- The last test is assigning the control box a serial number. **Only perform this test if all others have passed.** We only want to assign a serial number to a working control box.
  - This text just prompts you for a serial number. Grab a new serial number sticker from the sheet and a new 4"x6" label from the pile, ensuring the serial numbers match, and input the serial number into the prompt for the test.

- Unplug the USB and Power cables from the control box.

- Unplug all of the cables and pneumatics from the control box.
- Put the serial number sticker in the recess in the back of the control box

	![alt text](img/IMG_2015.webp)

- Fit a lid on the control box, and make sure the 4"x6" label is sandwiched between the box and the lid.

	![alt text](img/IMG_2017.webp)

- Check that both buttons click well.

!!!success "The control box has passed Gundam QC testing!"
