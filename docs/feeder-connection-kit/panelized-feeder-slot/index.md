# feeder-blade-panel (PCBA)
This section will guide the reader on how to properly create a `feeder-blade-panel (PCBA)`

## SMT
* Paste blade panels three at a time.
* Load three pasted blade panels into the Blade Lumen
* Run the job in OpenPnP
* Remove the panels and reflow them in the oven *one at a time*
* Inspect for any shorts or shifted components and rework as needed
* Add the 120R termination resistor to the 50th slot position if needed
* Place the completed `feeder-blade-panel (PCBA)` units into the yellow bin found at the blade assembly work station
	![](img/slots-in-bins3.jpeg)

## Programming
* Grab the stylus from the blade programmer
  ![](img/pgrm-slot-set-pca-14.JPG)
* Ensure that the address is set to `1`
	* You can adjust the address with the buttons to the right of the screen
* Place the spring pins of the stylus against the pads on `Slot #1`
	* Make sure the orientation matches as shown below:
		  ![](img/pgrm-slot-set-pca-15.JPG)
		  ![](img/program-blade-4.jpeg)

* Press the switch on the stylus when all spring pins are compressed against the pads
	![](img/program-blade-5.jpeg)
* Look at the screen:
	
	!!!failure "The programming step failed if you see *anything other than a `success` message*"
		* The jig is capable of detecting shorts, and will fail programming if one is detected
			* The screen will display which pin it sensed has shorted
		* If a failure is observed perform any necessary cleanup and try again
		* Note that the jig will remember the last place you left off

	!!!success "If the programmer reads `1 - SUCCESS` proceed to the next slot position"
		![](img/program-blade-3.jpeg)

* After successfully programming address `1`, repeat this step for the next 49 addresses while moving in the following order:<br> <span style="color:#FF00FF"> Pink (4th row) </span> → <span style="color:Red"> Red (2nd row) </span> → <span style="color:Green"> Green (3rd row) </span> → <span style="color:#0096FF"> Blue (1st row) </span>
	![](img/programming-blade-4.jpg)

	!!!warning "Pay **extreme attention** to avoid programming any slot with the wrong value"

## QC
Ensure your completed PCBA meets the following requirements:

- Switch the programmer to `QC Mode` and confirm that Slots #1, #13, #23, #26, #38, #48, and #50 each have a programmed value that matches the top-side silkscreen text

	!!!info "For example:"
		Confirm that Slot #26 is *actually* programmed as Slot #26

- Gold spring finger pads are free of damage

Place each quality checked `feeder-blade-panel (PCBA)` into the appropriate QC bin:

!!!success "Place all QC passing `feeder-blade-panel (PCBA)` units into the green QC bin"
	![](img/slots-in-bins1.jpeg)
	
!!!failure "Place all QC failing `feeder-blade-panel (PCBA)` units into the red QC bin"
	Be sure to label each defective unit with any issues it has
	![](img/slots-in-bins2.jpeg)

The next step is to proceed to `Feeder Blade Set Final Assembly`
