## Intro
The purpose of this work instruction is to explain the assembly process for the LumenPnP v4 Left-Side Y-Gantry (`y-gantry-left`). This document also serves as the work instruction for the `y-gantry-right` subassemby, as this is simply a mirror of the left-side.

## Create Y-Gantry Subassembly
- Remove any stringing from the print with a heat gun
- Insert 6x `m5-hex-nut` into the following region
	![](img/y-gantry-hex-nut.webp)
- Install 2x `m5-square-nut` into the location shown below
	![](img/y-gantry-square-nut.webp)

## Create Front-Left-Leg Subassembly

### Prepare front-left-leg
- Remove any stringing from the print with a heat gun
- Insert 2x `M5-hex-nut` into bottom of leg. You can use a thick screwdriver to push part of the `M5-hex-nut`in and finish with the `M5-hex-nut-jig`, also known as the `thingy`. 
	
	![](img/with_1.webp)
	![](img/sauce.webp)
	![](img/the_1.webp)

- Insert 1x `m5-square-nut` near extrusion pocket
 	![](img/front-drag-chain-mount-nut.webp)
 	
- Insert 1x `m5-nylock-hex-nut` into in the underside of `belt-tensioner-arm` mounting post
	![](img/belt-tension-arm-nut.webp)

### Prepare belt-tensioner-arm
- Press an `M3-hex-nut` into the `belt-tension-arm` with a `arbor-press-jig`
![](img/tensioner-arm-m3-hex-nut-insertion.webp)
- Thread a `M3x16-bolt` through the `belt-tension-arm`
![](img/m3x16-tensioner-bolt-install.webp)
- Thread a `M3-acorn-nut` onto the end of the bolt
	-  The `M3-acorn-nut` and `M3-hex-nut` should be on the same side of the `belt-tensioner-arm`
	-  Tighten the `M3-acorn-nut` onto the `M3x16-bolt` with a 5.5mm socket and an allen wrench
	
	![](img/M3-acorn-nut-install.webp)
	![](img/tighten-acorn-nut1.webp)
	![](img/tighten-acorn-nut2.webp)


- Rotate the `M3x16-bolt` until the `M3-acorn-nut` is fully secure and the `M3x16-bolt` has been threaded through the hex nut. 

	!!!info "This ensures the `belt-tensioner-arm` is installed with it's adjustment range fully available for when it's time to tension `GT2-belt`"

	![](img/newagebelts.webp)

- Insert a `M5-nylock-hex-nut` into `belt-tension-arm`'s hex-nut pocket
	![](img/gt2-pivot-hex-nut-insert.webp)

- Slide a `GT2-idler-pulley` into the `belt-tensioner-arm`
	![](img/gt2-idler-install.webp)

	!!!note "Note that the `GT2-idler-pulley` is symmetrical, so it's orientation does not matter"

- Install a `M5x25-bolt` into the `belt-tensioner-arm` to secure the `GT2-idler-pulley` in place
	- Avoid over tightening this bolt as the `GT2-idler-pulley` should be able to spin freely without resistance
	- The bolt should, however, be tightened enough to eliminate lateral pulley movement within the `belt-tensioner-arm`

	![](img/gt2-idler-pivot-bolt.webp)

### Install belt-tensioner-arm onto front-left-leg

- Add a drop of `ptfe-silicone-lubricant` to both sides of `belt-tensioner-arm`'s pivot point

- Install `belt-tensioner-arm` onto `front-left-leg`
	![](img/belt-tensioner-arm-asm-install.webp)

- Secure the `belt-tensioner-arm` onto `front-left-leg` with a `M5x40-bolt`
	- Avoid over tightening this bolt as the `belt-tensioner-arm` should be able to pivot freely without *much* resistance

	![](img/belt-tensioner-pivot-bolt.webp)

- The completed `front-left-leg` should match the image shown below
	![](img/complete-front-left-leg.webp)

## Create Back-Left-Leg Subassembly

### Prepare back-leg
- Remove any stringing from the 3D print with a heat gun
- Insert an `m5-hex-nut` into the bottom of the `back-leg` 3D print
	- Finger strength *should* be sufficient to install this fastener into position
	!!!glue "Glue if needed"
		Add a drop of loctite to the region if the fastener fit is looser than normal and seems at risk of falling out in transit
	![](img/back-leg-hex-nut1.webp)
	![](img/back-leg-hex-nut2.webp)

### Prepare y-gantry stepper motor
- Gather the following parts and tools
	- nema17-stepper-motor
	- GT2-timing-pulley
	- y-timing-pulley-spacer-jig
	- Torque driver w/2mm hex driver, set to `0.7 N/M` *(not shown)*

	![](img/y-gantry-motor-prep0.webp)
- Use motor spacing jig to mount the timing pulley to the NEMA 17, ensuring the set screw is aligned to the flat side of the motor shaft
	![](img/y-gantry-motor-prep1.webp)
- Tighten the 2x timing pulley set screws to 0.7 N/M - first tightening the one facing the flat on the motor shaft
	![](img/y-gantry-motor-prep2.webp)
	![](img/y-gantry-motor-prep3.webp)
	
### Install y-gantry stepper motor onto back-leg
- Connect `Y1-stepper-motor-cable` to the `y-gantry-stepper-motor`

	![](img/y1-cable-connected.webp)

- Install the  `y-gantry-stepper-motor` onto `back-leg`
	- The `Y1-stepper-motor-cable` should be routed through `back-leg` to exit towards the center of the machine
	- Ensure no wires are being crushed or strained

	![](img/install-y1-stepper.webp)

- Put 4x `M3x8-bolt` through the motor mounting holes found on `back-leg`

	![](img/bolt-y1-stepper-motor.webp)

- Install a `zip-tie` for cable strain relief
	- Use a `zip-tie` to attached the `Y1-stepper-motor-cable` to the `back-leg` to add strain relief

		![](img/zip-tie-y1-cable1.webp)

	- Cut the `zip-tie` with `flush-cutters`

		![](img/zip-tie-y1-cable2.webp)

	- Ensure that `Y1-stepper-motor-cable` and `zip-tie` are resting against the logo-face side of `back-leg`

		![](img/zip-tie-y1-cable3.webp)

## Assemble y-gantry-left

### Install front-left-leg and back-leg onto alu-extrusion

- Begin by inserting a `525mm-m3-t-nut-bar` into a piece of `alu-extrusion`
	- There should be about 51.5mm between the end of the `525mm-m3-t-nut-bar` and the right-side end of the `alu-extrusion` after installation
	- The `525mm-m3-t-nut-bar` needs to be slide aside in later steps, so do not bother to make this perfect right now

	![](img/install-tnut-bar.webp)

- Insert `front-left-leg` and `back-leg` onto 2x pieces of `alu-extrusion`
	- The `525mm-m3-t-nut-bar` is oriented in the top-side groove of the uppermost `alu-extrusion`
	- The extrusion pieces should be *fully* inserted into each leg

	![](img/install-legs-onto-ext.webp)

- Bolt `back-leg` to `alu-extrusion`
	- Insert 3x `m3-t-nut` into the `alu-extrusion` pieces before sliding each of them into alignment with the matching bolt holes on `back-leg`

		![](img/back-leg-t-nut-insertion.webp)

	- Insert 3x `M5x10-bolt` into `back-leg` and thread the bolts into each corresponding `M5-t-nut`

		![](img/bolt-back-leg-to-ext.webp)

- Bolt `front-left-leg` to `alu-extrusion`
	- Slide the `M3-t-nut-bar` out of the way *if needed*
	- Insert an `M5-t-nut` into the upper channel of `alu-extrusion`
	- Align the `M5-t-nut` with the top-side bolt hole on `front-left-leg`  

		![](img/insert-front-leg-top-t-nut.webp)

	- Insert a `M5x10-bolt` into the top-side bolt hole on `front-left-leg` and tighten it into the `M5-t-nut`

		![](img/insert-front-leg-top-m5x10-bolt.webp)

	- Slide 2x `M5-t-nut` into the the side channel of lower `alu-extrusion` and align them with the two bolt holes on `front-left-leg`

		![](img/insert-front-leg-bottom-t-nut.webp)

	- Insert 2x `M5x10-bolt` into the side bolt holes on `front-left-leg` and tighten each into the corresponding `M5-t-nut`

		![](img/insert-front-leg-side-t-nut.webp)

- Compare the WIP `y-gantry-left` assembly to the image below after completing all previous steps, address any discrepancies as needed before proceeding onward

	![](img/y-gantry-left-process-check1.webp)

### Install linear-rail-550mm

- Roughtly position `linear-rail-550mm` onto top-side of uppermost `alu-extrusion`

	![](img/position-y-linear-rail.webp)

- Place a `linear-rail-2020-alignment-jig` on both ends of `linear-rail-550mm`
	- Do not cover any bolt holes with the jig  

	![](img/insert-y-rail-alignment-jig.webp)

- Visually center the `linear-rail-550mm` between the `back-leg` and `front-left-leg`
- Slide the `M3-t-nut-bar` to line up with the linear rail's bolt hole pattern
- Starting from the `front-left-leg` side, lightly snug a `M3x8-bolt` into **every other** bolt hole on `linear-rail-550mm`
	- Move the `linear-rail-carriage` out of the way as needed

	![](img/install-11x-linear-rail-bolts.webp)

- Torque the rail mounting bolts to specification in sequence beginning with the bolts at the center of the rail and working towards each end
	- A torque wrench should be used to set the specified bolt torque
	- The torque specification for these `M3x8-bolts` is `0.5N/M`

	![](img/y-linear-rail-bolt-sequence.webp)

- Remove the `linear-rail-2020-alignment-jig` from both ends of `linear-rail-550mm`
- Slide the linear-rail-carriage back and forth a few times, checking to see that it travels smoothly and consistently

### Halfway Checkpoint

- Verify that `y-gantry-left` matches the following photo

	![](img/y-gantry-checkpoint.webp)

!!!success "If `y-gantry-left` matches the photo, proceed to the next section"
!!!failure "If `y-gantry-left` does not match the photo, correct discrepancies before proceeding to the next section"

___________________________________________________________________________________________________________________________________

### Install GT2-belt

- First slip `GT2-belt` through `y-gantry` itself. 
- Work it through the end that is closer to the `belt-tension-arm`. (The side that DOES NOT have the long end with the two holes on top) 

	<img src="img/1.webp" width="60%" height=auto>

- Grab a `belt-clamp`, have the `GT2-belt` & `belt-clamp` be flushed to the edge of gantry as much as possible. Screw it down with 2x `M5x10-bolt`. 

	<img src="img/2.webp" width="60%" height=auto>

!!! info "With the other end of the `GT2-belt`" 

	- Snake it through the `extrusion-rail` on the `belt-tension-arm` side first. Front to back.
	- Wrap it around the `idler-pulley` in the `belt-tension-arm`, then snake it through the back of the `extrusion-rail`. 
	- Pull it all the way to the other side of the rail, into the open channel, around the `timing-pulley` on the `NEMA-17`.
	- Then bring the working end of the `GT2-belt` to the gantry and snake the belt from back to front in the open section for the belt. 

<img src="img/4.webp" width="60%" height=auto>
<img src="img/5.webp" width="60%" height=auto>
<img src="img/6.webp" width="60%" height=auto>
<img src="img/8.webp" width="60%" height=auto>

!!! note "While tightening in the next step, make sure that the belt does not twist in the `extrusion-rail` and stays flushed on the angles on the back of the gantry."
	
	<img src="img/13circs.webp" width="60%" height=auto>

- Bolt `y-gantry` to the `linear-rail-carriage` with 4x `M3x8-bolt`
    - Tighten each bolt to 0.7 N/M

<img src="img/bolt-y-gantry-to-carriage.webp" width="60%" height=auto>

!!! failure "Ensure that `y-gantry` sits flush against `linear-rail-carriage` without any visible gaps" 

- Place the partially assembled leg on its side so the gantry face and the `GT2-belt` are facing up. This will make it so much easier for tightening without the gantry moving so much. 

<img src="img/10.webp" width="60%" height=auto>


- Either with your fingers or the soft jaw pliers, you will pull that working end of the `GT2-belt` to tighten it to the `extrusion-rail`. Once you have tensioned it, screw it into place with a `belt-clamp` and 2x `M5x10` bolts. 

<img src="img/11.webp" width="60%" height=auto>
<img src="img/12.webp" width="60%" height=auto>





<!-- ### Install GT2-belt
- Route a 1.3m-long piece of `GT2-belt` through `y-gantry-left`

	!!!info "Belt routing step-by-step"
		- Start by running the belt through the `y-gantry`'s left-side slot and leave 75mm of extra belt poking out
		- Run it through the extrusion towards the `back-leg`
		- Wrap it around the `timing-pulley`
		- Run it back through the extrusion towards the `front-left-leg`
		- Wrap it around the `idler-pulley`
		- Run it back through the extrusion towards the `back-leg` again
		- Have the belt exit through the `y-gantry`'s right-side slot

	![](img/route-belt-through-step1.webp)

- Slide the `y-gantry` subassembly onto the `linear-rail-carriage` while pulling slack out of the `GT2-belt`
	![](img/route-belt-through-step2.webp)
	![](img/belt-pulled-through-irl.webp)

- Bolt `y-gantry` to the `linear-rail-carriage` with 4x `M3x8-bolt`
	- Tighten each bolt to 0.5 N/M
	- Push `y-gantry` inward towards the `linear-rail-carriage while tightening the mounting bolts to align it  

	!!!warning "Ensure that `y-gantry` sits flush against `linear-rail-carriage` without any visible gaps"

	![](img/bolt-y-gantry-to-carriage.webp)

- Use `belt-clamp` with 2x `M5x10-bolt` to clamp the left-side of the `GT2-belt` to the `y-gantry`
	- Tighten each `M5x10-bolt` to 0.5 N.M

	![](img/route-belt-through-step3.webp)
	![](img/route-belt-through-step4.webp)

### Tension the Y-Gantry

- Pull the right-side `GT2-belt` tightly towards `front-left-leg`

	![](img/route-belt-through-step5.webp)

- Use `belt-clamp` with 2x `M5x10-bolt` to clamp the right-side `GT2-belt` to the `y-gantry`
	- Tighten each `M5x10-bolt` to 0.5 N.M

	![](img/route-belt-through-step6.webp)

- Rotate the `M3x16-bolt` clockwise on the `belt-tensioner-arm` to tension the `GT2-belt` installed on `y-gantry-left`
	- This will cause the `belt-tensioner-arm` to pull the `idler-pulley` away from the `front-left-leg` which adds desired tension to `GT2-belt`

	![](img/tension-belt-arm.webp)

- Trim the loose `GT2-belt` on either side of the `y-gantry`
	- For the `front-left-leg` side of the `y-gantry` print, trim the loose `GT2-belt` until it's flush against `belt-clamp`
	- For the `back-leg` side of the `y-gantry` print, trim the loose `GT2-belt` until there's approx. 15mm of `GT2-belt` past `belt-clamp`

	![](img/belt-cut-to-length.webp) -->



### Add cable management

- Use **3x** `extrusion-cable-clip` to secure the `Y1-stepper-motor-cable` to the inner side of the lower `alu-extrusion`

	![](img/y-gantry-extrusion-cable-clip.webp)

- Position the right-most `extrusion-cable-clamp` and the cable to match the following image:

	![alt text](img/y-gantry-final-wiring.webp)

## Quality Checks
A `y-gantry-left` that was built while following the above steps will match the following image.

![](img/complete-y-gantry-left.webp)

Confirm this by inspecting the completed `y-gantry-left` assembly with the following QC checklist:

* Confirm M5 bolts are installed in every counterbored region
* `M5-hex/square-nut` installed where required:
	* 2x `M5-hex-nut` pressed into bottom of `front-left-leg`
	* 1x `M5-square-nut` pressed into side of `front-left-leg` for use with `y-limit-striker`

		!!!info "This is only applicable when building y-gantry-left"
			Please ignore this QC check when building y-gantry-right.

	* 1x `M5-hex-nut` pressed into bottom of `back-leg`
	* 2x `M5-hex-nut` pressed into `y-gantry`

* `GT2-belt` has been trimmed to appropriate length:
	* Flush on `front-left-leg` side
	* Approx. 15mm on `back-leg` side
* `GT2-belt` has been correctly tensioned
* `GT2-belt` lays flat in the `alu-extrusion` channels
* `timing-pulley` is tightened down and at proper height
* `tensioner-arm` is installed on `front-left-leg` in the correct orientation (IE acorn-nut facing touches leg)
* `linear-rail` is centered atop `aluminum-extrusion`
* `y-gantry-left` sits flat on `linear-rail-carriage`
* `y-gantry` feels smooth and free of friction across the y-min to y-max travel range when actuated by hand
* 3x `extrusion-cable-clip` have been installed onto the lower `alu-extrusion`
* `Y1` cable is secured with a zip-tie and exits the port labeled `Y1`

!!!warning "Stay vigilant for new failure modes not listed above and report them to a production lead when found"

!!!success "If all checks pass"
	Set the finished `y-gantry-left` aside for Buddy QC testing
