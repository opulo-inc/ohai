# Outgoing Quality Control (OQC)

## Test Feeder with Gundam

1. Launch the Gundam Application by entering the command `main.py` into the `gundam` terminal within VS Code

  	![](img/oqc-1.JPG)
  	![](img/oqc-37.JPG)

2. Load feeder into the `gundam-qc-jig` by installing it onto the orange feeder slot 

  	![](img/oqc-29.JPG)
  	![](img/oqc-28.JPG)

3. In the Gundam application window, click "Scan Ports" and choose the `/dev/tty/ACM0` device ID from the drop-down list
 
  	![](img/oqc-34.JPG)
  	![](img/oqc-33.JPG)
  	
4. If required, choose `REV09-feeder.json` from the `Test to Run` drop-down menu
	
	`TO DO CONFIRM WHAT THE REAL TEST LIST NAME WILL BE FOR MASS PRODUCTION`
	
5. Click the `Run Test` button found at the bottom of the Gundam application window
6. Input the following information when the application prompts for data input:
	* `Please input the unit serial` - Leave this field blank
	* `Please input the unit source version` - Enter the current production revision number (`v1.0.0` for example)
7. The Gundam application will now display a list of tests to run in sequential order
 	* Follow the Gundam test prompts to step through the testing process

  	![](img/oqc-27.JPG)

!!!failure "If any of the tests have failed, rework the feeder as needed to address issues"
	If a feeder is failing to pass Gundam checks after more than 10 minutes of rework activity, set it aside and revisit later
!!!success "Proceed onward if all tests show `PASS` results" 
	  	![](img/oqc-8.JPG)

## Install feeder-rev-sticker
* Adhere a `feeder-rev-sticker` onto the motherboard in the marked region

 	 ![](img/sticker-12.PNG)
 	 ![](img/sticker-9.JPG)

## Install 8mm-feeder-sticker
1. Install `feeder-sticker-application-jig` on the backside of the feeder
	* It should sit snug on the feeder without being able to move around
	!!!info "`feeder-sticker-application-jig` is now grey instead of green"

     ![](img/sticker-1.JPG)
     ![](img/sticker-2.JPG)
2. Adhere the right-side of `8mm-feeder-sticker` to the feeder while using the top-left corner pocket of `feeder-sticker-application-jig` to align it into position
     ![](img/sticker-3.JPG)
     ![](img/sticker-4.JPG)
	  ![](img/sticker-5.JPG)
	  
3. Remove the `feeder-sticker-application-jig` and rub the sticker to ensure it is fully adhered to the `feeder-frame-8mm`
	  ![](img/sticker-6.JPG)
	  
## Cosmetic Inspection
After completing all prior assembly and testing work, CHECK EVERY BULLET on EVERY FEEDER:

* Release Lever moves freely with a snappy action
* Release Lever does NOT move laterally
* Flexture buttons click easily and are not mushy
* Reset button clicks easily
* Fiducial board is inserted
* Fiducial board does NOT have any excess glue
    * ![](img/fid-bad-glue-1.jpg)
    * ![](img/fid-bad-glue-2.jpg)
* Diffusion board is inserted in the correct orientation
* All screws are flush with the print/PCB they're mounted into
* All nuts are flush and perpendicular to their screws
* Drive motor is flush with the back face of the frame
* Cosmetic sticker has been applied over the drive motor
* Version number sticker has been applied to the PCB

!!!success "If all final checks are OK, the feeder may proceed forward to packout"