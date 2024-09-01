Preparing x-gantry
==================

## Create `x-linear-axis` subassembly
---------------------------------

### Prepare `x-gantry-back`

####  Install fasteners

*	Remove any stringing from the print with a heat gun
*	Insert 4x `m5-hex-nut` into the following region

	<img src="images/nut1-x-gantry-back.jpg"/>

*	Insert 5x `m5-hex-nut` into the following region
	* Add a drop of `blue-loctite` into each of these pockets to permanently secure each nut in place
	<img src="images/nut2-x-gantry-back.jpg"/>

#### Check `top-camera` focus

*   Use `top-camera-focus-jig` to check focus of `top-camera`

*   Connect `top-camera-focus-jig` to a laptop and open a native camera viewing application

	<img src="images/image36.jpg"/>

*   Remove `lens-cap` from `top-camera`

*   Install the `top-camera` fully into the `top-camera-focus-jig`, plugging the USB cable into the camera module afterwards

	<img src="images/image56.jpg"/>

*   In Photobooth, change the selected camera to `LumenPnP Top` to view the camera feed from  `top-camera`

	<img src="images/image60.jpg"/> 

!!!success "If the datum-board is sharp and nicely focused continue onward"

	<img src="images/image48.jpg"/>

!!!failure "If the datum-board is blurry and out of focus, follow instructions below"

	<img src="images/image39.jpg"/>

	*   Loosen `set-screw` on side of lens body

		<img src="images/image21.jpg"/>

	*   Rotate camera lens until live view shows `datum-board` as focused as possible

		<img src="images/image48.jpg"/>

	*   Once the camera is refocused, tighten `set-screw` to preserve the adjustments

*   Remove the `top-camera` from `top-camera-focus-jig` and immediately replace `lens-cap`

#### Install `top-camera` and `top-ring-light` into `x-gantry-back`

*   Install `top-camera` into x-gantry-back

	<img src="images/x-gantry-back-install-camera.jpg"/>

*   Install `top-ring-light` into `top-light-mount`

	<img src="images/install-ring-light.jpg"/>

*   Install `top-light-mount` onto back of `x-gantry-back`

	<img src="images/install-top-light-mount1.jpg"/>

*   Secure `top-light-mount` in place with 2x `M3x12-self-tapping-flat-head`

	<img src="images/screw-in-top-light-mount.jpg"/>

### Prepare `NEMA-17-stepper-motor` for `x-linear-axis`

*   Set `timing-pulley` height on `NEMA-17-stepper-motor` shaft with `x-pulley-spacer-jig`

*  Tighten the first `set-screw` into the flat region found on the `NEMA-17-stepper-motor` shaft, before tightening the second `set-screw`
	*   Tighten each `set-screw` to 0.6 N/M

	<img src="images/image34.jpg"/>

### Install `NEMA-17-stepper-motor` onto `x-motor-mount`

*	Orient `NEMA-17-stepper-motor` onto `x-motor-mount` so that the motor's connector is facing the backside of the print as shown in the image below

	<img src="images/motor-connector-orientation.jpg"/>

*   Bolt `NEMA-17-stepper-motor` onto x-`motor-mount` with 4x `M3x8-bolt`

	*   Tighten these bolts to 0.4 N/M

	<img src="images/image4.jpg"/>

### Install `XY-limit-switch-board` onto `x-motor-mount`

*  Install `XY-limit-switch-board` onto `x-motor-mount` and secure it with 2x `m3x12-self-tapping-flat-head-screw`

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

*	Insert `alu-extrusion` into `x-idler-mount`, using light force as necessary

	<img src="images/install-ext-into-x-motor-mount.jpg"/>

*	Insert 2x `M5-t-nut` into `alu-extrusion`

	<img src="images/install-x-motor-mount-t-nut.jpg"/>

	<img src="images/install-x-motor-mount-t-nut2.jpg"/>

*	Secure `alu-extrusion` in place with 2x `M5x10-socket-head-bolt`
	* Tigthen these bolts to 0.6N/M

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

*	Roughtly position `linear-rail-525mm` onto top-side of `alu-extrusion`

	<img src="images/install-x-linear-rail.jpg"/>

*	Place a `linear-rail-2020-alignment-jig` on both ends of `linear-rail-525mm`
	*	Do not cover any bolt holes with the jig

	<img src="images/install-x-linear-rail-2.jpg"/>

*	Visually center `linear-rail-525mm` between `x-motor-mount` and `x-idler-mount`
*	Slide the `M3-t-nut-bar` to line up with the rail's bolt hole pattern
*	Starting from the `x-motor-mount` side, lightly snug a `M3x8-bolt` into every other bolt hole on `linear-rail-525mm`
	*	Move the `linear-rail-carriage` out of the way as needed
	
	<img src="images/install-x-linear-rail-3.jpg"/>

*	Torque the rail mounting bolts to specification in sequence beginning with the bolts at the center of the rail and working towards each end.
	*	A torque wrench set to 0.5N/M must be used when tighening these bolts

	<img src="images/install-x-linear-rail-4.jpg"/>

*	Remove the `linear-rail-2020-alignment-jig` from both ends of `linear-rail-525mm`
*	Slide the `linear-rail-carriage` back and forth a few times, checking to see that it travels smoothly and consistently

### Install GT2-belt and x-gantry-back
* Route a 1.5m-long piece of `GT2-belt` through `x-gantry-back`
	
	!!!info "Belt routing step-by-step"
		* Start by running the belt through the left-side slot on `x-gantry-back` and leave 75mm of extra belt poking out
		* Run it through the extrusion towards the `x-motor-mount`
		* Wrap it around the `timing-pulley`
		* Run it back through the extrusion towards the `x-idler-mount`
		* Wrap it around the `idler-pulley`
		* Run it back through the extrusion towards the `x-motor-mount` again
		* Have the belt exit through the right-side slot on `x-gantry-back`

	<img src="images/install-x-GT2-belt.jpg"/>

* Slide the `x-gantry-back` onto the `linear-rail-carriage` while pulling slack out of the `GT2-belt`

	<img src="images/install-x-GT2-belt-2.jpg"/>
	
* Bolt `x-gantry-back` to the `linear-rail-carriage` with 4x `M3x16-bolt`
	*   Tighten each bolt to 0.5 N/M
	*	Push `x-gantry-back` inward towards the `linear-rail-carriage` while tightening the mounting bolts to align it

	!!!warning "Ensure that `x-gantry-back` sits flush against `linear-rail-carriage` without any visible gaps"

	<img src="images/bolt-x-gantry-back-to-linear-rail.jpg"/>

* Use `belt-clamp` with 2x `M5x10-bolt` to clamp the left-side of the `GT2-belt` to the `x-gantry-back`
	* Tighten each `M5x10-bolt` to 0.5 N.M

	<img src="images/bolt-belt-clamp1-to-x-gantry-back.jpg"/>
	<img src="images/bolt-belt-clamp1-to-x-gantry-back-2.jpg"/>

### Tension belt

* Pull the right-side `GT2-belt` tightly towards `x-motor-mount`
* Use `belt-clamp` with 2x `M5x10-bolt` to clamp the right-side `GT2-belt` to the `y-gantry`
	* Tighten each `M5x10-bolt` to 0.5 N.M

	<img src="images/bolt-belt-clamp2-to-x-gantry-back.jpg"/>

* Rotate the `M3x16-bolt` clockwise on `belt-tensioner-arm` installed on `x-idler-mount` to tension the `GT2-belt`
	* This will cause the `belt-tensioner-arm` to pull the `idler-pulley` away from `x-idler-mount` adding desired tension to the `GT2-belt`

	<img src="images/tension-x-belt-1.jpg"/>
	<img src="images/tension-x-belt-2.jpg"/>


* Trim the loose `GT2-belt` on either side of the `x-gantry-back`
	* For the `x-motor-mount` side of the `x-gantry-backy` print, trim loose `GT2-belt` until flush against `belt-clamp`
	* For the `x-idler-mount` side of the `x-gantry-back` print, trim loose `GT2-belt` until approx. 15mm of `GT2-belt` remains past `belt-clamp`

	<img src="images/trim-x-belt.jpg"/>

### Confirm progress
*	Check that finsihed `x-linear-axis` matches the image shown below before proceeeding
<img src="images/finished-x-linear-axis.jpg"/>



## Create `x-gantry-front` subassembly

### Prepare `NEMA-17-stepper-motor` for z-axis

*   Set `timing-pulley` height on `NEMA-17-stepper-motor` shaft with jig

	*   The 1st set-screw tightened must contact the flat region of the motor’s shaft
		*   Tighten both set screws to 0.4 N/M

		<img src="images/image58.jpg"/>

		<img src="images/image57.jpg"/>

### Prepare `z-belt-subassembly`

*   Prepare `z-gantry-backplate-right`
	*   	Drill out the limit switch striker bolt hole on `z-gantry-backplate-right` with a 2.5mm drill bit

		<img src="images/image9.jpg"/>

	*   Install 1x `M3x16-flathead-bolt` into `z-gantry-backplate-right` to a depth that roughly matches the image shown below
		*   This screw depth will be precisely adjusted in later steps

		<img src="images/image51.jpg"/>

* Install both `z-gantry-backplate-left` and `z-gantry-backplate-right` onto `gt2-belt-loop`
	*   Place a `gt2-belt-loop` onto the `z-belt-alignment-jig`
	*   Place `z-gantry-backplate-left` and `z-gantry-backplate-right` onto the `z-belt-alignment-jig` to align them correctly on the `gt2-belt-loop`
	*   Twist `z-gantry-backplate-left` upwards to pull the completed `z-belt-subassembly` off of the `z-belt-alignment-jig`
	*   Use a dull knife or other tool to push the `gt2-belt-loop` all the way down into the cavity of each `z-gantry-backplate-####`

	!!!note "TO DO: Add info about LOCTITE 435 Usage"

### Install `M5-lock-nut` into `x-gantry-front`

*   Use an arbor press to install an `M5-lock-nut` into backside of `x-gantry-front`

	<img src="images/image38.jpg"/>

### Install 2x `linear rail` onto `x-gantry-front`

*   Install 2x `linear-rail` by aligning them against the bumps found on `x-gantry-front`

	*   Uses 3x `M3x12-self-tapping-button-head` per `linear-rail`
	*   Tighten each bolt to 0.5 N/M

	<img src="images/image44.jpg"/>

	<img src="images/align-rail.jpg"/>

	<img src="images/image67.jpg"/>

### Install `z-axis-limit-switch`

*   Secure with 2x `M3x12-self-tapping-button-head`
*   Make sure each limit switch clicks and feels normal when actuated

	<img src="images/image22.jpg"/>

	<img src="images/image63.jpg"/>

### Install z-axis belt drive components

*   Secure `idler-pulley` onto `x-gantry-front`  with 1x `M5x25-bolt`, tigthend enough that the pulley can rotate freely without resistance
*   Check that the pulley can only rotate - it should not be able to move up and down if the bolt is tightened correctly

	<img src="images/image20.jpg"/>

*   Begin by placing `z-belt-subassembly` onto  `x-gantry-front`

	*   The `z-gantry-backplate-right` should fit over the right `linear-rail-carriage`, and the same goes for the left-side

	*	The `gt2-belt-loop` should wrap around the `idler-pulley`

	<img src="images/image66.jpg"/>

*   Install the `NEMA-17-stepper-motor` by angling it into the `z-belt-subassembly`

	*   The limit switch connector will be at a 45º from the motor’s connector when everything is in the proper position.

	<img src="images/image7.jpg"/>

*   Bolt `NEMA-17-stepper-motor` onto `x-gantry-front` with 4x `M3x8-bolt`

	*   Leave the bolts loose for now

	<img src="images/image1.jpg"/>

*   Tension `gt2-belt-loop` by pulling the motor upwards before tightening the mounting bolts to 0.5 N/M

	*   The belts should feel much firmer now - to test manually move the z-axis back and forth while inspecting the belts for sag when changing directions
	*   You should be able to pluck the belt like a bass string

		<img src="images/image8.jpg"/>

		<img src="images/image13.jpg"/>

*	The `x-gantry-front` should now match the image shown below:

	<img src="images/checkpoint.jpg"/>

### Install 2x `z-gantry` 

*   Loosely attach a `z-gantry` onto the left-side `linear-rail-carriage` with 4x `M3x8-bolt` per side
	<img src="images/bolt-left-head.jpg"/>

*   Align `z-gantry` paralell to `linear-rail` by lightly pressing it outward, while tigtening the mounting bolts
	*   Tighten bolts to 0.3 N/M, moving in a star pattern

	<img src="images/image26.jpg"/>

*	Repeat this process to attach the second `z-gantry` to the right-side `linear-rail-carriage`

	<img src="images/2x-z-gantry-installed.jpg"/>

### Install `NEMA11-hollow-shaft-stepper`

*   Bolt `NEMA11-hollow-shaft-stepper` onto left-side `z-ganty`
	*   Attach with 4x M2.5x8 bolts
	*   Torque each bolt to 0.3 N/M

	<img src="images/bolt-nema11-1.jpg"/>

	<img src="images/bolt-nema11-2.jpg"/>

### Install toolhead components
*	Slide `nozzle-mask` onto `nozzle-holder` as shown in the image below

	<img src="images/slide-nozzle-mask.jpg"/>

*	Place `rotary-pneumatic-adapter` into `rotary-pneumatic-adapter-socket`
	*  Attach the custom socket to a torque driver if you have not already done so
	*  Set the torque driver to `0.5 N/M` for the following steps

	<img src="images/image10-render.jpg"/>
	<img src="images/image10.jpg"/>

*   Install `nozzle-holder` and `rotary-pneumatic-adapter` onto `NEMA11-hollow-shaft-stepper`
	*  Begin by loosely threading `nozzle-holder w/attached nozzle-mask` onto the `NEMA11-hollow-shaft-stepper` (on the side closest to the `idler-pulley`)
	*  Install `rotary-pneumatic-adapter` onto `NEMA11-hollow-shaft-stepper` (on the side closest to the motor's cable connector)
	*  Place a 16mm wrench onto the flats found on `nozzle-mask`
	*  Tighten the toolhead components onto the `NEMA11-hollow-shaft-stepper` by torquing the `rotary-pneumatic-adapter`

	<img src="images/tighten-toolhead.jpg"/>

*   Repeat above process to attach a `pneumatic-toolhead-assembly` to the left-side `z-gantry`

	<img src="images/x-gantry-front-done1.jpg"/>

## Install `x-gantry-front` onto `x-linear-axis`

*	Use 4x `M5x10-bolt` to attach `x-gantry-front` onto `x-linear-axis`
	*	Move the toolheads out of the way as needed
	*	Torque each bolt to `0.8 N/M`

	![alt text](images/bolt-x-gantry-front-1.jpg)
	![alt text](images/bolt-x-gantry-front-2.jpg)
	![alt text](images/bolt-x-gantry-front-3.jpg)

## Gundam test `x-gantry`

*   Ensure that the Gundam motherboard is unplugged from 24vDC power
*   Check that `x-gantry` fits correctly on `x-gantry-spacer-jig`
*   Slide a `M5x25-bolt` into the `x-gantry` from either side of `x-gantry-spacer-jig` to prevent it from falling during testing
*   Bolt down the test jig’s drag chain onto `x-gantry-back` with 1x `M5x16-bolt`
*   Connect the test jig’s `xy-limit`, `z-limit`, `x-motor`, and `z-motor` cables into x-gantry
*   Connect the Gundam motherboard to 24vDC power and then press reset on Gundam motherboard
*   Connect the motherboard to the Gundam test software
*   Begin testing the `x-gantry` by running various macros:

	*   Check X-Home

		*   If the toolhead is moving very slow, the stepper drivers may not have initialized properly - try restarting the motherboard again

	*   Check X-Movement Speed

		*   Ensure that no weird sounds are heard, if so consult with team for debugging steps
		*   Adjust the tightness of the belts and each tensioner-bar as needed to pass this test
		
	*   Test Z-Home

		*   Check that the z-belt is adequately tensioned and adjust if necessary - you shouldn’t be able to twist the belt too much
		*   Adjust the M3x16 bolt either up or down as needed, until the z-gantrys are aligned vertically after homing
			*   This can be checked by sliding a brass shim across the top of the motor while checking to see if it sits higher/lower than the top surface of the adjacent motor
			*   Repeat this test and continue adjusting the M3x16 bolt until the alignment appears to be perfect
		
	*   Test Z-Movement Speed

!!! failure   "If issues arrise, continue rerunning tests and reworking the x-gantry"

!!! success  "Once everything is passing, proceed with the following steps"

*   Remove `x-gantry` from Gundam
	*   Disconnect Gundam motherboard from 24vDC power
	*   Unplug the test jig’s `xy-limit`, `z-limit`, `x-motor`, and `z-motor` cables from `x-gantry`
	*   Unscrew `drag-chain mounting hardware` from `x-gantry`
	*   Remove the 2x `M5x25-bolt` used to keep `x-gantry` on `x-gantry-spacer-jig`

## QC Checklist
Inspect the completed `x-gantry` for the following criteria:

* `GT2-belt` has been trimmed to appropriate length (flush on 1 side, 15mm on the other)
* Camera is installed with two bolts
* Camera lens cap is present
* The wire connectors on both `NEMA-11-stepper-motor` units face away from each other, sitting adjacent to their respective cable strain relief points
* Each `nozzle-holder` has been lubricated and fit-tested with a nozzle
* `Z-belt-loop` feels appropriately tensioned when plucked
* Each `z-gantry` moves smoothly when actuated back-and-forth by hand
* 1x `M5-hex-nut` are installed in `x-gantry-back` for use with `drag-chain` attachment
* `NEMA-17-stepper-motor` wire connector faces towards `z-limit-switch`
* `Linear-rail` is centered atop `aluminum-extrusion`
* `x-idler-mount` and `x-motor-mount` are secured to `alu-extrusion` with 2x `M5x10-bolt` per side
* `Tensioner-arm` is installed on `x-idler-mount` in the correct orientation (IE acorn-nut facing touches print)
* `Timing-pulley` is tightened down and at proper height
* `GT2-belt` lays flat and is roughly centered in the `alu-extrusion` channels
* `GT2-belt` has been correctly tensioned
* `X-gantry-toolhead` moves smoothly when actuated back and forth by hand


!!!success "If all checks pass, place completed `x-gantry` on shelf for peer-review and pack-out."
