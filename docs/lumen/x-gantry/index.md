Preparing x-gantry
==================

## Assemble `x-linear-axis`
---------------------------------

### Prepare `X-gantry-back` 

*  Words go here

### Install `NEMA-17-stepper-motor` onto `x-motor-mount`

*   Set `timing-pulley` height on `NEMA-17-stepper-motor` shaft with `x-pulley-spacer-jig`

*  Tighten the first `set-screw` into the flat region found on the `NEMA-17-stepper-motor` shaft, before tightening the second `set-screw`
	*   Tighten each `set-screw` to 0.6 N/M

	<img src="images/image34.jpg"/>

### Install `NEMA-17-stepper-motor` onto `x-motor-mount`

*	Orient `NEMA-17-stepper-motor` onto `x-motor-mount` so that the motor's connector is facing the backside of the print as shown in the image below

	<img src="images/motor-connector-orientation.jpg"/>

*   Bolt `NEMA-17-stepper-motor` onto x-`motor-mount` with 4x M3x8 bolts

	*   Tighten these bolts to 0.4 N/M

	<img src="images/image4.jpg"/>

### Install `XY-limit-switch-board` onto `x-motor-mount`

*  Install `XY-limit-switch-board` onto `x-motor-mount` and secure it with 2x `m3x12-self-tapping-flat-head-screws`

	<img src="images/install-xy-limit-switch-board.png" />

### Install `belt-tensioner-arm` onto `x-idler mount`

*  If you have not already done so, assemble 1x `belt-tensioner-arm`

	!!!note "For reference building this sub-assembly, visit the [Y Gantry OHAI page](../lumen/y-gantry/#prepare-belt-tensioner-arm)"

* Install 1x `M5-lock-nut` into `x-idler-mount`

	<img src="images/install-belt-tensioner-arm-nut.jpg"/>

*   Install `belt-tensioner-arm` onto `x-idler-mount`

	<img src="images/place-belt-tensioner-arm.jpg"/>

*   Bolt `belt-tensioner-arm` to `x-idler-mount` with 1x `M5x40-socket-head-bolt`
	*   Avoid over tightening the bolt! `belt-tensioner-arm` should be able to pivot smoothly without much resistance.
	*   Ensure the belt-tensioner-arm is installed correctly on x-idler-mount (IE not backwards)
		*   The acorn nut should be resting against the x-idler mount when installed correctly

	<img src="images/bolt-belt-tensioner-arm.jpg"/>

### Install `alu-extrusion` onto `x-motor-mount`

<img src="images/install-ext-into-x-motor-mount.jpg"/>

<img src="images/install-x-motor-mount-t-nut.jpg"/>

<img src="images/install-x-motor-mount-t-nut2.jpg"/>

<img src="images/install-x-motor-mount-bolt.jpg"/>

### Install `M3-t-nut-bar`

!!!warning "Inspect the `M3-t-nut-bar` to ensure that each hole has M3 threads"

*	Slide `M3-t-nut-bar` into top-side track of `alu-extrusion`

	<img src="images/install-x-tee-nut-bar.jpg"/>

### Install `x-idler-mount` onto `alu-extrusion`

*	Insert 2x `M5-t-nut` into `alu-extrusion`

	<img src="images/install-x-idler-t-nut.jpg"/>

*	Slide `x-idler-mount` onto `alu-extrusion`

	<img src="images/install-x-idler-mount-1.jpg"/>

	<img src="images/install-x-idler-mount-2.jpg"/>

*	Use `x-gantry-spacer-jig` to slide `x-idler-mount` onto `alu-extrusion` the required amount
	*	The WIP `x-linear-axis` should be sitting on `x-gantry-spacer-jig` snug - not overly tight - when `x-idler-mount` is at the correct depth

	<img src="images/install-x-idler-mount-3.jpg"/>

*	Secure `x-idler-mount` in place with 2x `M5x10-socket-head-bolt`
	* Tigthen these bolts to 0.6N/M

	<img src="images/install-x-idler-mount-4.jpg"/>
	

### Install `linear-rail-525mm`

<img src="images/install-x-linear-rail.jpg"/>

<img src="images/install-x-linear-rail-2.jpg"/>

<img src="images/install-x-linear-rail-3.jpg"/>

<img src="images/install-x-linear-rail-4.jpg"/>

*	Remove the `linear-rail-2020-alignment-jig` from both ends of `linear-rail-525mm`

*	 Slide the `linear-rail-carriage` back and forth a few times, checking to see that it travels smoothly and consistently

### Install GT2-belt

<img src="images/install-x-GT2-belt.jpg"/>

<img src="images/install-x-GT2-belt-2.jpg"/>


*	Bolt `x-gantr-back` to the linear-rail-carriage with 4x `M3x16-socket-headbolt`
	*	Tighten each bolt to 0.6 N/M
	*	Push `x-gantry-back` inward towards the `linear-rail-carriage` while tightening the mounting bolts to align it

	<img src="images/bolt-x-gantry-back-to-linear-rail.jpg"/>

<img src="images/bolt-belt-clamp1-to-x-gantry-back.jpg"/>

<img src="images/bolt-belt-clamp1-to-x-gantry-back-2.jpg"/>

<img src="images/bolt-belt-clamp2-to-x-gantry-back.jpg"/>

<img src="images/trim-x-belt.jpg"/>

<img src="images/finished-x-linear-axis.jpg"/>

## Prepare x-gantry-front assembly

### Top-camera-assembly preparation

*   Use the top-camera-focus-jig to pre-focus top-cameras

*   Connect top-camera-focus-jig to a laptop and open a native camera viewing application

	<img src="images/image36.jpg"/>

*   Remove the top-camera lens cap
*   Loosen the set screw found on the side of the lens body that locks the focus

	<img src="images/image21.jpg"/>

*   Install the top-camera fully into the top-camera-focus-jig, plugging the USB cable into the camera module afterwards

	<img src="images/image56.jpg"/>

*   In Photobooth, change the selected camera to PnP Top to view the camera feed of the top-camera. The setup should now look like the following image

	<img src="images/image60.jpg"/> 

*   Rotate the camera lens until the live viewport shows the datum board as focused as possible

	<img src="images/image39.jpg"/>
	
	<img src="images/image48.jpg"/>
	
	!!! info "Camera view before and after focusing shown above"
	 	
*   Once the camera is focused, tighten the set screw to lock in the adjustments
*   Put a red dot on the camera PCB with a sharpie to denote that the camera has passed testing

	<img src="images/image41.jpg"/>

*   Remove the top-camera from the top-camera-focus-jig and immediately replace the lens cap.

### Assemble the top-camera-assembly

*   Installing top-ring-light into top-light-mount
	*   Place the ring light facing downwards into the top-light-mount.
	*   The LEDs will shine down, and the white plastic wire connector will face upwards.
	<img src="images/image45.jpg"/>
	<img src="images/image50.jpg"/>

*   Place top-camera-mount above top-light-mount, ensuring that the tab from the top-light-mount fits onto the side opposite the arms on the top-camera

	*   These two prints will pinch the top ring light in place

	<img src="images/image2.jpg"/>

*   Install top-camera into top-camera-mount. 
	*   Make sure the connector on the back side of the camera is between the two arms of the top-camera-mount.

	<img src="images/image47.jpg"/>

*   Secure the whole stack in place with four M2.5x20mm screws in the outer four holes 
	*   Do not put the screws through the inner holes with metal circles around them
	*   Tighten the screws enough so that all parts are tightly held together, however be cautious as these screws are threading directly into the plastic

	<img src="images/image27.jpg"/>

### X-gantry-front preparation

*   Install hex nuts into x-gantry-front, being sure to utilize the x-gantry-front-nut-plate fixture when installing hardware into the backside of the print.

*   Press an M5 nyloc hex nut into the backside of x-gantry-front

<img src="images/image38.jpg"/>

*   Install the 8x M3 hex nuts into the backside of the x-gantry-front, use a narrow tool to ensure that these pieces are fully inserted into the 3D print.

<img src="images/image55.jpg"/>

<img src="images/image11.jpg"/>

*   Insert the 2x hex nuts used for tension adjustment deep into the print, stopping once the threads are fully visible from the intersecting bolt hole

<img src="images/image25.jpg"/>

*   Install tensioner bar onto x-gantry-front

### x-gantry-toolhead assembly

*   Install linear-rails by aligning them against the bumps on x-gantry-front

	*   Uses 3x M3x14 bolts per rail
	*   Tighten each bolt to 0.5 N/M

	<img src="images/image44.jpg"/>

	<img src="images/image67.jpg"/>

*   Install z-axis limit switch onto x-gantry-front

	*   Mounts with 2x M3x8 bolts and 2x M3 hex nuts on backside (should be already installed by now)
	*   Make sure each limit switch clicks and feels normal when actuated

	<img src="images/image22.jpg"/>

	<img src="images/image63.jpg"/>

*   Install idler-pulley onto x-gantry-front

	*   Use 1x M5x25 bolt and torque with a 4mm hex driver
	*   Check that the pulley can rotate freely without resistance
	*   Check that the pulley can only rotate - it should not be able to move up and down if the bolt is tightened correctly

	<img src="images/image20.jpg"/>
	<img src="images/image62.jpg"/>

*   Prepare z-belt-subassembly

	*   Prepare z-gantry-backplate-left
	*   Drill out the limit switch striker bolt hole on z-gantry-backplate-left with a 2.5mm drill bit
	
		<img src="images/image9.jpg"/>

	*   Install an M3x16 Flathead bolt into z-gantry-backplate-left to a depth that roughly matches the image shown below
		*   This screw depth will be precisely in later steps

		<img src="images/image51.jpg"/>

	*   Place a gt2-belt-loop onto the z-belt-alignment-jig
	*   Place z-gantry-backplate-left and z-gantry-backplate-right onto the z-belt-alignment-jig to align them correctly on the gt2-belt-loop
	*   Twist z-gantry-backplate-left upwards to pull the completed z-belt-subassembly off of the z-belt-alignment-jig
	*   Use a dull knife or other tool to push the gt2-belt-loop all the way down into the cavity of each z-ganry-backplate

*   Set timing-pulley height on NEMA 17 stepper motor shaft with jig

	*   The 1st set screw tightened  must contact the flat region of the NEMA 17 motor’s shaft
		*   Tighten both set screws to 0.4 N/M

		<img src="images/image58.jpg"/>

		<img src="images/image57.jpg"/>

*   Install NEMA 17 stepper motor and belts onto the x-gantry-front subassembly

	<img src="images/image37.jpg"/>

	*   Begin by placing the gt2-belt-loop w/attached z-gantry-backplates onto the x-gantry-front subassembly

	*   The z-gantry-backplate-right should fit over the right linear rail’s carriage, and the same goes for the left side

		<img src="images/image66.jpg"/>

	*   Install the NEMA 17 stepper motor by angling it into the belt-loop

	*   The limit switch connector will be at a 45degree angle from  the z-axis stepper motor’s connector when everything is in the proper position.

		<img src="images/image7.jpg"/>

	*   Bolt NEMA 17 stepper motor onto x-gantry-front with 4x M3x8 bolts

	*   Leave the bolts loose for now

		<img src="images/image1.jpg"/>

	*   Tension belt-loop by pulling the stepper motor upwards before tightening its mounting bolts to 0.5 N/M

		*   The belts should feel much firmer now - to test manually move the z-axis back and forth while inspecting the belts for sag when changing directions
		*   You should be able to pluck the belt like a bass string

			<img src="images/image8.jpg"/>

			<img src="images/image13.jpg"/>

*   Attach z-gantry-left and z-gantry-right onto each respective linear rail carriages + z-gantry-backplate with 4x M3x8 bolts per side

	*   Align each z-gantry to be parallel with the linear-rail by lightly pressing it outward with your hand, away from the mid-plane of the x-gantry-subassembly
		*   As these bolts are tightend ensure that the z-gantry doesn’t collide with the z-idler’s bolt head
	*   Tighten bolts to 0.3 N/M, moving in a star pattern

		<img src="images/image26.jpg"/>

*   Prepare pneumatic-toolhead-assembly
	*   Install a `nozzle-holder` and `rotary-pneumatic-adapter` onto `NEMA11-hollow-shaft-stepper`
		*  Use a torque driver w/custom `rotary-pneumatic-adapter-socket` and 8mm wrench to tighten these components onto the motor shaft
		*  Set the torque driver to `0.5 N/M` for this step
		*  Use the 8mm wrench to hold the `nozzle-holder` stationary while applying torque from the `rotary-pneumatic-adapter`side
		*  The `rotary-pneumatic-adapter` should be installed closer to the motor's cable connector

		<img src="images/image31.jpg"/>
		<img src="images/image10.jpg"/>
		<img src="images/image54.jpg"/>
		<img src="images/image30.jpg"/>

	*   Install 2x pneumatic-toolhead-assembly onto x-gantry-front-subassembly

	*   Bolt pneumatic-toolhead-assembly onto left side z-ganty
		*   Attach with 4x M2.5x8 bolts
		*   Torque each bolt to 0.3 N/M

		<img src="images/image23.jpg"/>

		<img src="images/image40.jpg"/>

	*   Repeat above process to attach a pneumatic-toolhead-assembly to the right side z-gantry

		<img src="images/image69.jpg"/>

### X-gantry final assembly

*   Precut GT2 belt to ### length
*   Run gt2-belt through x-gantry-linear axis and connect both ends to x-gantry-back

*   Fully depress the x-axis belt tensioner arm before tightening down the belt with 2x belt-clamps with 2x M5x10mm socket head screws per clamp.
*   Use brass bar to route the belt through the extrusion and ends of the axis

*   Install x-gantry-front-subassembly onto x-gantry-linear-axis, connecting it to previously installed x-gantry-back

<img src="images/image3.jpg"/>

*   Step #1 - Hold the x-gantry-back subassembly against the x-gantry-linear-axis subassembly for the following steps to happen easier
*   Step #2A - Fully insert 2x M5x40 bolts through the upper counterbored M5 bores in x-gantry-front
*   Step #2B - Happening basically simultaneously with the previous step, align 2x roller-space and 2x v-wheels onto the previously inserted M5x40 bolts

 <img src="images/image5.jpg"/>

*   Step #3 - Move the x-gantry-front-subassembly backward into the x-gantry-back-subassembly, paying attention to keeping the upper 2x v-wheels aligned on the x-gantry-linear-axis’s 2020-v-groove extrusion

<img src="images/image16.jpg"/>


!!!note
	Rotate everything upside down for the following steps

*   Step #4A - Lower 2x v-wheels up until they rest loosely against the 2020 v-groove extrusion, they should also each be aligned so that each wheel is concentric to the raised nubs on the x-gantry’s tensioner-bars.

*   Note that the 2x tensioner-bar pieces may not be vertically aligned very well by this point, so this process may be tricky

<img src="images/image33.jpg"/>

<img src="images/image24.jpg"/>

*   Step #4B -

	*   Adjust the vertical alignment of the 2x tensioner-bar pieces
	
	*   This is done by tightening or loosening the 4x M3x30 adjustment bolts until you can peer straight through the lower counterbored M5 bores in x-gantry-front and past the hex-nut slot found on x-grant-back
	*   This may take a few minutes so be patient!
	*   Tighten and loosen all 4x M3x30 bolts as a set, taking care to never make a single bolt more than a few turns away from any other bolt
	
	*   Fully insert 2x M5x40 bolts into the lower counterbored M5 bores in x-gantry-front, through both v-wheels, and stopping within two hex-nut slots found on x-gantry-back
	
	*   Manipulate the z-gantry pieces as needed to avoid interference with the bolts
	
	<img src="images/image14.jpg"/>
	
	<img src="images/image68.jpg"/>
	
	*   Tension x-gantry v-wheels and x-axis belt tensioner arm
	
	*   Tighten the 4x M3x30 bolts until the toolhead-assembly can smoothly move along the x-gantry-linear-axis, without resistance
	
	*   Grab the toolhead-assembly and try twisting it in many directions, if you feel any play or looseness tighten the appropriate M3x30 bolts until the play dissipates
	
	<img src="images/image18.jpg"/>
	
	*   Tighten the 2x lower M5x40 bolts to 0.1 N/M to lock-in the calibrated v-wheel tension
	*   Tension the belt to 0.03 N/M \*\* need to confirm \*\*
	
	<img src="images/image70.jpg"/>


## Test x-gantry on Gundam jig

*   Ensure that the Gundam motherboard is unplugged from 24vDC power
*   Check that the x-gantry fits correctly on the x-gantry-spacer-jig
*   Slide a bolt into the x-gantry on either side of x-gantry-spacer-jig to prevent it from falling during testing
*   Bolt down the test jig’s drag-chain onto x-gantry-back-subassembly with 2x M5x16 bolts
*   Connect the test jig’s z-limit-switch, x-motor, and z-motor cables to the x-gantry being tested on the x-gantry-spacer-jig
*   Connect the Gundam motherboard to 24vDC power and then press reset on the motherboard
*   Connect the motherboard to the Gundam test software
*   Begin testing the x-gantry by running various macros

*   Check X-Home

	*   If the toolhead is moving very slow, the stepper drivers may not have initialized properly - try restarting the motherboard again

*   Check X-Movement Speed

	*   Ensure that no weird sounds are heard, if so consult with team for debugging steps
	*   Adjust the tightness of the belts and each tensioner-bar as needed to pass this test
	
*   Test Z-Home

	*   Check that the z-belt is adequately tensioned and adjust if necessary - you shouldn’t be able to twist the belt too much
	*   Adjust the M3x16 bolt either up or down, if needed, provided the z-gantries are not aligned vertically after homing,
	
	*   This can be checked by sliding a brass shim across the top of the motor while checking to see if it sits higher/lower than the top surface of the adjacent motor
	
	*   Repeat this test and continue adjusting the M3x16 bolt until the alignment appears to be perfect
	
*   Test Z-Movement Speed

!!! failure   "If issues arrise, continue rerunning tests and reworking the x-gantry"

!!! success  "Once everything is passing, proceed with the following steps"

*   Remove x-gantry from Gundam
	*   Disconnect Gundam motherboard from 24vDC power
	*   Unplug the test jig’s z-limit-switch, x-motor, and z-motor cables from the x-gantry being tested on the x-gantry-spacer-jig
	*   Unscrew the drag-chain mounting hardware from the x-gantry being tested on the x-gantry-spacer-jig
	*   Remove the 2 M5x25 bolts used initially for keeping the x-gantry from falling off the x-gantry-spacer-jig


## Install top-camera-assembly
*   Install top-camera and Light subassembly onto x-gantry
	*   Use two M3x14mm screws to mount the top-camera and Light subassembly onto the back of the X Gantry Back.

	<img src="images/image19.jpg"/>

	<img src="images/image49.jpg"/>

## QC Checklist
Inspect the completed `x-gantry` for the following criteria:

* `GT2-belt` has been trimmed to appropriate length (flush on 1 side, ~1/2" - 3/4" on the other)
* Camera is installed with two bolts
* Camera lens cap is present
* The wire connectors on both `NEMA-11-stepper-motor` units face away from each other, sitting adjacent to their respective cable strain relief points
* Each `nozzle-holder` has been lubricated and fit-tested with a nozzle
* `Z-belt-loop` feels appropriately tensioned when plucked
* Each `z-gantry` moves smoothly when actuated back-and-forth by hand
* 2x `M5-hex-nut` are installed in `x-gantry-back` for use with `drag-chain` attachment 
* `NEMA-17-stepper-motor` wire connector faces towards `drag-chain` mounting location on `x-gantry-back`
* `Linear-rail` is centered atop `aluminum-extrusion`
* `x-idler-mount` and `x-motor-mount` are secured to `600mm-alu-extrusion` with 2x `M5x10-bolt` per side
* 2x `M5-hex-nut` are installed in `x-motor-mount` for use with the `x-motor-cable-guide`
* `Tensioner-arm` is installed on `x-idler-mount` in the correct orientation (IE acorn-nut facing touches print)
* `Timing-pulley` is tightened down and at proper height
* `GT2-belt` lays flat and is roughly centered in the `600mm-alu-extrusion` channels
* `GT2-belt` has been correctly tensioned
* `X-gantry-toolhead` moves smoothly when actuated back and forth by hand


!!!success "If all checks pass, bring the completed `x-gantry` to the shelf for peer-review and pack-out."
