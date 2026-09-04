---
zoduki: true
---

Preparing x-gantry
==================

## Prepare `x-gantry-back`

###  Install backside fasteners

*	Insert 4x `m5-hex-lock-nut` into the following region

	<img src="images/nut1-x-gantry-back.webp"/>
	
###  Install frontside fasteners

*	Insert 5x `m5-hex-nut` into the following region

	<img src="images/nut2-x-gantry-back.webp"/>
	
### Prep for top camera focus

*   Acquire `top-camera-focus-jig` and connect `top-camera-focus-jig` to a laptop and open a native camera viewing application

	<img src="images/image36.webp"/>

*   Remove `lens-cap` from `top-camera`

*   Install the `top-camera` fully into the `top-camera-focus-jig`, plugging the USB cable into the camera module afterwards

	<img src="images/image56.webp"/>

### Inspect the image and adjust

*   In Photo Booth, change the selected camera to `LumenPnP Top` to view the camera feed from  `top-camera`

	<img src="images/image60.webp"/> 

- Rotate camera lens until live view shows `datum-board` as focused as possible

	<img src="images/image48.webp"/>

	<img src="images/image39.webp"/>

### Remove Camera and Replace Cover

*   Remove the `top-camera` from `top-camera-focus-jig` and immediately replace `lens-cap`

### Install Top Camera

*   Install `top-camera` into `x-gantry-back`

	<img src="images/x-gantry-back-install-camera.webp"/>

### Install Top Light

*   Install `top-ring-light` into `top-light-mount`

	<img src="images/install-ring-light.webp"/>

*   Install `top-light-mount` onto back of `x-gantry-back`

	<img src="images/install-top-light-mount1.webp"/>

### Secure Top Light

*   Secure `top-light-mount` in place with 2x `M3x12-self-tapping-flat-head`

	<img src="images/screw-in-top-light-mount.webp"/>

### Prepare `NEMA-17-stepper-motor` for `x-linear-axis`

*   Set `timing-pulley` height on `NEMA-17-stepper-motor` shaft with `x-pulley-spacer-jig`

*  Tighten the first `set-screw` into the flat region found on the `NEMA-17-stepper-motor` shaft, before tightening the second `set-screw`

*   Tighten each `set-screw` to 0.5 N/M

	<img src="images/image34.webp"/>

### Install `NEMA-17-stepper-motor` onto `x-motor-mount`

*	Orient `NEMA-17-stepper-motor` onto `x-motor-mount` so that the motor's connector is facing the backside of the print as shown in the image

	<img src="images/motor-connector-orientation.webp"/>

*   Bolt `NEMA-17-stepper-motor` onto x-`motor-mount` with 4x `M3x8-bolt`

	<img src="images/image4.webp"/>

	!!!note "Torque Spec"

		Tighten these bolts to 0.5 N/M

### Install `XY-limit-switch-board` onto `x-motor-mount`

*  Install `XY-limit-switch-board` onto `x-motor-mount` and secure it with 2x `M3x8mm-self-tapping-flat-head-screw`

	<img src="images/install-xy-limit-switch-board.webp" />

* Tighten each screw in place with the electic torque driver

* If needed, clipping the ends off the pins of the right angle switch on `XY-limit-switch-board` helps the pcb sit flat against the print.

### Install nut into into `x-idler mount`

* Install 1x `M5-lock-nut` into `x-idler-mount`

	<img src="images/install-belt-tensioner-arm-nut.webp"/>

### Install Belt Tension Arm onto X Idler Mount

*   Install `belt-tensioner-arm` onto `x-idler-mount` as shown

	<img src="images/place-belt-tensioner-arm.webp"/>

	!!! danger "Insert the correct direction"

		The acorn nut should be resting against the x-idler mount when installed correctly

*   Bolt `belt-tensioner-arm` to `x-idler-mount` with 1x `M5x40-socket-head-bolt`

	!!! danger "Don't Overtighten"

		`belt-tensioner-arm` should be able to pivot smoothly without much resistance.

	<img src="images/bolt-belt-tensioner-arm.webp"/>

### Install `alu-extrusion` onto `x-motor-mount`

*	Insert `alu-extrusion` into `x-idler-mount`, using light force as necessary

	<img src="images/install-ext-into-x-motor-mount.webp"/>

*	Insert 2x `M5-t-nut` into `alu-extrusion`

	<img src="images/install-x-motor-mount-t-nut.webp"/>

	<img src="images/install-x-motor-mount-t-nut2.webp"/>

*	Secure `alu-extrusion` in place with 2x `M5x10-socket-head-bolt`

	!!!note "Torque Spec"

		Tighten these bolts to 0.5 N/M

	<img src="images/install-x-motor-mount-bolt.webp"/>

### Install `M3-t-nut-bar`

!!!warning "Inspect the `M3-t-nut-bar` to ensure that each hole has M3 threads"

*	Slide `M3-t-nut-bar` into top-side track of `alu-extrusion`

	<img src="images/install-x-tee-nut-bar.webp"/>

### Install `x-idler-mount` onto `alu-extrusion`

*	Insert 2x `M5-t-nut` into `alu-extrusion`

	<img src="images/install-x-idler-t-nut.webp"/>

*	Slide `x-idler-mount` onto `alu-extrusion`

	<img src="images/install-x-idler-mount-1.webp"/>

	<img src="images/install-x-idler-mount-2.webp"/>

### Secure X Gantry Spacing

*	Use `x-gantry-spacer-jig` to slide `x-idler-mount` onto `alu-extrusion`. The `x-linear-axis` should be sitting on `x-gantry-spacer-jig` snug - not overly tight - when `x-idler-mount` is at the correct depth

	<img src="images/install-x-idler-mount-3.webp"/>

*	Secure `x-idler-mount` in place with 2x `M5x10-socket-head-bolt`

	<img src="images/install-x-idler-mount-4.webp"/>

	!!! note
		Tighten these bolts to 0.5N/M
	

### Align `linear-rail-525mm`

*	Roughly position `linear-rail-525mm` onto top-side of `alu-extrusion`

	<img src="images/install-x-linear-rail.webp"/>

*	Place a `linear-rail-2020-alignment-jig` on both ends of `linear-rail-525mm`. Do not cover any bolt holes with the jig

	<img src="images/install-x-linear-rail-2.webp"/>

*	Visually center `linear-rail-525mm` between `x-motor-mount` and `x-idler-mount`

*	Slide the `M3-t-nut-bar` to line up with the rail's bolt hole pattern

### Load Screws for the 525mm linear rail

*	Starting from the `x-motor-mount` side, lightly snug a `M3x8-bolt` into every other bolt hole on `linear-rail-525mm`

	<img src="images/install-x-linear-rail-3.webp"/>

*	Move the `linear-rail-carriage` out of the way as needed

### Attach the 525mm linear rail

*	Tighten the rail mounting bolts to in the sequence shown in the image, starting in the center.
	
	<img src="images/install-x-linear-rail-4.webp"/>

	!!! note
		A torque wrench set to 0.5N/M must be used when tightening these bolts

### Remove the jigs and check movement

*	Remove the `linear-rail-2020-alignment-jig` from both ends of `linear-rail-525mm`
*	Slide the `linear-rail-carriage` back and forth a few times, checking to see that it travels smoothly and consistently

## Routing Belt

### Install GT2-belt and x-gantry-back
*  Using a 1.5m-long piece of `GT2-belt`:
	* Start by running the belt through the left-side slot on `x-gantry-back` and leave 75mm of extra belt poking out
	* Run it through the extrusion towards the `x-motor-mount`
	* Wrap it around the `timing-pulley`
	* Run it back through the extrusion towards the `x-idler-mount`
	* Wrap it around the `idler-pulley`
	* Run it back through the extrusion towards the `x-motor-mount` again
	* Have the belt exit through the right-side slot on `x-gantry-back`

	<img src="images/install-x-GT2-belt.webp"/>

	<img src="images/install-x-GT2-belt-2.webp"/>


### Attach X gantry back to rail carriage

* Slide the `x-gantry-back` onto the `linear-rail-carriage` while pulling slack out of the `GT2-belt`

	<img src="images/install-x-GT2-belt-2.webp"/>

*   Apply threadlocker to 4x `M3x16-bolt`

*   Tighten each bolt to 0.5 N/M. Push `x-gantry-back` into the `linear-rail-carriage` while tightening the mounting bolts to align it.
	<img src="images/bolt-x-gantry-back-to-linear-rail.webp"/>

	!!! warning
		Ensure that `x-gantry-back` sits flush against `linear-rail-carriage` without any visible gaps

### Affix Belt Clamps

* Use `belt-clamp` with 2x `M5x10-bolt` to clamp the left-side of the `GT2-belt` to the `x-gantry-back`

	<img src="images/bolt-belt-clamp1-to-x-gantry-back.webp"/>

* Tighten each `M5x10-bolt` to 0.5 N.M

	<img src="images/bolt-belt-clamp1-to-x-gantry-back-2.webp"/>

### Attach other side of belt

* Pull the right-side `GT2-belt` tightly towards `x-motor-mount` to tension it.

* Use `belt-clamp` with 2x `M5x10-bolt` to clamp the right-side `GT2-belt` to the `y-gantry` {color=orange}

* Tighten each `M5x10-bolt` to 0.5 N.M {color=orange}

	<img src="images/bolt-belt-clamp2-to-x-gantry-back.webp"/>

### Tension Belt

* Rotate the `M3x16-bolt` clockwise on `belt-tensioner-arm` installed on `x-idler-mount` to tension the `GT2-belt`

	<img src="images/tension-x-belt-1.webp"/>
	
* This will cause the `belt-tensioner-arm` to pull the `idler-pulley` away from `x-idler-mount` adding desired tension to the `GT2-belt`

	<img src="images/tension-x-belt-2.webp"/>

### Trim excess belt

* For the `x-motor-mount` side of the `x-gantry-back` print, trim loose `GT2-belt` until flush against `belt-clamp` {color=blue}


* For the `x-idler-mount` side of the `x-gantry-back` print, trim loose `GT2-belt` until approx. 15mm of `GT2-belt` remains past `belt-clamp` {color=blue}

	<img src="images/trim-x-belt.webp"/>

### Confirm progress

*	Check that finished `x-linear-axis` matches the image before proceeding
	
	<img src="images/finished-x-linear-axis.webp"/>

## Create `x-gantry-front` subassembly

### Prepare `NEMA-17-stepper-motor` for z-axis

*   Set `timing-pulley` height on `NEMA-17-stepper-motor` shaft with jig {color=green}

	<img src="images/image58.webp"/>

*   The 1st set-screw tightened must contact the flat region of the motor’s shaft {color=green}

	<img src="images/image57.webp"/>

	!!! note

		Tighten both set screws to 0.4 N/M

### Prepare `z-belt-subassembly`

*   Prepare `z-gantry-backplate-right`
	*   	Drill out the limit switch striker bolt hole on `z-gantry-backplate-right` with a 2.5mm drill bit

		<img src="images/image9.webp"/>

	*   Install 1x `M3x15-flathead-bolt` into `z-gantry-backplate-right` to a depth that roughly matches the image shown below
		*   This screw depth will be precisely adjusted in later steps

		<img src="images/image51.webp"/>

* Install both `z-gantry-backplate-left` and `z-gantry-backplate-right` onto `gt2-belt-loop`
	*   Place a `gt2-belt-loop` onto the `z-belt-alignment-jig`
	*   Place `z-gantry-backplate-left` and `z-gantry-backplate-right` onto the `z-belt-alignment-jig` to align them correctly on the `gt2-belt-loop`
	*   Twist `z-gantry-backplate-left` upwards to pull the completed `z-belt-subassembly` off of the `z-belt-alignment-jig`
	*   Use a dull knife or other tool to push the `gt2-belt-loop` all the way down into the cavity of each `z-gantry-backplate-####`

	!!!note "TO DO: Add info about LOCTITE 435 Usage"

### Install `M5-lock-nut` into `x-gantry-front`

*   Use an arbor press to install an `M5-lock-nut` into backside of `x-gantry-front`

	<img src="images/image38.webp"/>

### Install 2x `linear rail` onto `x-gantry-front`

*   Install 2x `linear-rail` by aligning them against the bumps found on `x-gantry-front`

	*   Uses 3x `M3x12-self-tapping-button-head` per `linear-rail`
	*   Tighten each bolt in place with the electic torque driver

	<img src="images/image44.webp"/>

	<img src="images/align-rail.webp"/>

	<img src="images/image67.webp"/>

### Install `z-axis-limit-switch`

*   Secure with 2x `M3x12-self-tapping-button-head`
	* Tighten each screw in place with the electic torque driver
*   Make sure each limit switch clicks and feels normal when actuated

	<img src="images/image22.webp"/>

	<img src="images/image63.webp"/>

### Mount `idler-pulley` and `z-belt-subassembly`

*   Secure `idler-pulley` onto `x-gantry-front`  with 1x `M5x25-bolt`, tightened enough that the pulley can rotate freely without resistance
*   Check that the pulley can only rotate - it should not be able to move up and down if the bolt is tightened correctly

	<img src="images/image20.webp"/>

*   Begin by placing `z-belt-subassembly` onto  `x-gantry-front`

	*   The `z-gantry-backplate-right` should fit over the right `linear-rail-carriage`, and the same goes for the left-side

	*	The `gt2-belt-loop` should wrap around the `idler-pulley`

	<img src="images/image66.webp"/>

### Install and tension the z-axis stepper motor

*   Install the `NEMA-17-stepper-motor` by angling it into the `z-belt-subassembly`

	*   The limit switch connector will be at a 45º from the motor’s connector when everything is in the proper position.

	<img src="images/image7.webp"/>

*   Bolt `NEMA-17-stepper-motor` onto `x-gantry-front` with 4x `M3x8-bolt`

	*   Leave the bolts loose for now

	<img src="images/image1.webp"/>

*   Tension `gt2-belt-loop` by pulling the motor upwards before tightening the mounting bolts to 0.5 N/M

	*   The belts should feel much firmer now - to test manually move the z-axis back and forth while inspecting the belts for sag when changing directions
	*   You should be able to pluck the belt like a bass string

		<img src="images/image8.webp"/>

		<img src="images/image13.webp"/>

*	The `x-gantry-front` should now match the image shown below:

	<img src="images/checkpoint.webp"/>

### Install 2x `z-gantry` 

*   Loosely attach a `z-gantry` onto the left-side `linear-rail-carriage` with 4x `M3x8-bolt` per side
	<img src="images/bolt-left-head.webp"/>

*   Align `z-gantry` parallel to `linear-rail` by lightly pressing it outward, while tightening the mounting bolts
	*   Tighten bolts to 0.5 N/M, moving in a star pattern

	<img src="images/image26.webp"/>

*	Repeat this process to attach the second `z-gantry` to the right-side `linear-rail-carriage`

	<img src="images/2x-z-gantry-installed.webp"/>

### Install `NEMA11-hollow-shaft-stepper`

*   Bolt `NEMA11-hollow-shaft-stepper` onto left-side `z-ganty`
	*   Attach with 4x M2.5x8 bolts
	*   Torque each bolt to **0.3 N/M**

	<img src="images/bolt-nema11-1.webp"/>

	<img src="images/bolt-nema11-2.webp"/>

### Install toolhead components
*	Slide `nozzle-mask` onto `nozzle-holder` as shown in the image below

	<img src="images/slide-nozzle-mask.webp"/>

*	Place `rotary-pneumatic-adapter` into `rotary-pneumatic-adapter-socket`
	*  Attach the custom socket to a torque driver if you have not already done so
	*  Set the torque driver to `0.5 N/M` for the following steps

	<img src="images/image10-render.webp"/>
	<img src="images/image10.webp"/>

*   Install `nozzle-holder` and `rotary-pneumatic-adapter` onto `NEMA11-hollow-shaft-stepper`
	*  Begin by loosely threading `nozzle-holder w/attached nozzle-mask` onto the `NEMA11-hollow-shaft-stepper` (on the side closest to the `idler-pulley`)
	*  Install `rotary-pneumatic-adapter` onto `NEMA11-hollow-shaft-stepper` (on the side closest to the motor's cable connector)
	*  Place a 16mm wrench onto the flats found on `nozzle-mask`
	*  Tighten the toolhead components onto the `NEMA11-hollow-shaft-stepper` by torquing the `rotary-pneumatic-adapter`

	<img src="images/tighten-toolhead.webp"/>

*   Repeat above process to attach a `rotary-pneumatic-toolhead-assembly` to the left-side `z-gantry`

	<img src="images/x-gantry-front-done1.webp"/>

## Install `x-gantry-front` onto `x-linear-axis`

*	Use 4x `M5x40-bolt` to attach `x-gantry-front` onto `x-linear-axis`
	*	Move each toolhead out of the way as needed
	*	Secure each bolt as tightly as possible without breaking `x-gantry-front`

	![alt text](images/bolt-x-gantry-front-1.webp)
	![alt text](images/bolt-x-gantry-front-2.webp)
	![alt text](images/bolt-x-gantry-front-3.webp)

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
		*   Adjust the M3x16 bolt either up or down as needed, until the z-gantry's are aligned vertically after homing
			*   This can be checked by sliding a brass shim across the top of the motor while checking to see if it sits higher/lower than the top surface of the adjacent motor
			*   Repeat this test and continue adjusting the M3x16 bolt until the alignment appears to be perfect
		
	*   Test Z-Movement Speed

!!! failure   "If issues arise, continue rerunning tests and reworking the x-gantry"

!!! success  "Once everything is passing, proceed with the following steps"

*   Remove `x-gantry` from Gundam
	*   Disconnect Gundam motherboard from 24vDC power
	*   Unplug the test jig’s `xy-limit`, `z-limit`, `x-motor`, and `z-motor` cables from `x-gantry`
	*   Unscrew `drag-chain mounting hardware` from `x-gantry`
	*   Remove the 2x `M5x25-bolt` used to keep `x-gantry` on `x-gantry-spacer-jig`

## QC Checklist
Inspect the completed `x-gantry` for the following criteria:

* `GT2-belt` has been trimmed to appropriate length (flush on 1 side, 15mm on the other)
* `Top-light-mount` is attached with two screws
* `top-ring-light` is present with the wire connector visible
* Camera lens cap is present
* The wire connectors on both `NEMA-11-stepper-motor` units face away from each other, sitting adjacent to their respective cable strain relief points
* Each `nozzle-holder` has been lubricated and fit-tested with a nozzle
* `Z-belt-loop` feels appropriately tensioned when plucked
* Each `z-gantry` moves smoothly when actuated back-and-forth by hand
* 1x `M5-hex-nut` is installed in `x-gantry-back` for use in `cable-splay` attachment
* `NEMA-17-stepper-motor` wire connector faces towards `z-limit-switch`
* `Linear-rail` is centered atop `alu-extrusion`
* `x-idler-mount` and `x-motor-mount` are secured to `alu-extrusion` with 2x `M5x10-bolt` per side
* `Tensioner-arm` is installed on `x-idler-mount` in the correct orientation (IE acorn-nut facing touches print)
* `Timing-pulley` is tightened down and at proper height
* `GT2-belt` lays flat and is roughly centered in the `alu-extrusion` channels
* `GT2-belt` has been correctly tensioned
* `X-gantry-toolhead` moves smoothly when actuated back and forth by hand


!!!success "If all checks pass, place completed `x-gantry` on shelf for peer-review and pack-out."
