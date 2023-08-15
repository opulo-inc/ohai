## Preparing back-leg

!!!info "Create 2x `back-leg` subassemblies per LumenPnP, one for each y-gantry-left/right, by following the steps below"


- Remove any stringing from the 3D print with a heat gun
- Insert an `m5-hex-nut` into the bottom of the `back-leg` 3D print
	- Finger strength *should* be sufficient to install this fastener into position
	!!!glue "Glue if needed"
		Add a drop of loctite to the region if the fastener fit is looser than normal and seems at risk of falling out in transit
	![](img/back-leg-hex-nut1.png)
	![](img/back-leg-hex-nut2.png)

## Preparing y-gantry

!!!info "Create 2x `y-gantry` subassemblies per LumenPnP, one for each y-gantry-left/right, by following the steps below"


- Remove any stringing from the 3D print with a heat gun
- Insert 6x `m5-hex-nut` into the following region
	![](img/y-gantry-hex-nut.png)
	
## Preparing y-gantry stepper motor

!!!info "Create 2x `y-gantry stepper motor` subassemblies per LumenPnP, one for each y-gantry-left/right, by following the steps below"

- Gather the following parts and tools
	- nema17-stepper-motor
	- GT2-timing-pulley
	- y-timing-pulley-spacer-jig
	- Torque driver w/2mm hex driver, set to `0.7 N/M` *(not shown)*

	![](img/y-gantry-motor-prep0.png)
- Use motor spacing jig to mount the timing pulley to the NEMA 17, ensuring the set screw is aligned to the flat side of the motor shaft 
	![](img/y-gantry-motor-prep1.png)
- Tighten the 2x timing pulley set screws to 0.7 N/M - first tightening the one facing the flat on the motor shaft 
	![](img/y-gantry-motor-prep2.png)
	![](img/y-gantry-motor-prep3.png)
	
## Preparing belt-tensioner-arm

!!!info "Create 2x `belt-tensioner-arm` subassemblies per LumenPnP, one for each y-gantry-left/right, by following the steps below"

- Press an `M3-hex-nut` into the `belt-tension-arm` with the `arbor-press-jig`
![](img/tensioner-arm-m3-hex-nut-insertion.png)
- Thread an `M3x16-bolt` all the way through the `belt-tension-arm`
![](img/m3x16-tensioner-bolt-install.png)
- Thread an `M3-acorn-nut` onto the end of the bolt
	-  The `M3-acorn-nut` and `M3-hex-nut` should be on the same side of the `belt-tensioner-arm`
	-  Tighten the `M3-acorn-nut` onto the `M3x16-bolt` with pliers and an allen wrench
	
	![](img/M3-acorn-nut-install.png)

- Rotate the `M3x16-bolt` until the `M3-acorn-nut` is loosely resting against the `M3-hex-nut`

	!!!info "This ensures the `belt-tensioner-arm` is installed with it's adjustment range fully available for when it's time to tension `GT2-belt`"

- Insert a `M5-nylock-hex-nut` into `belt-tension-arm`'s hex-nut pocket
	![](img/gt2-pivot-hex-nut-insert.png)

- Slide a `GT2-idler-pulley` into the `belt-tensioner-arm` 
	![](img/gt2-idler-install.png)

	!!!note "Note that the `GT2-idler-pulley` is symmetrical, so it's orientation does not matter"
	
- Install a `M5x25-bolt` into the `belt-tensioner-arm` to secure the `GT2-idler-pulley` in place
	- Avoid over tightening this bolt as the `GT2-idler-pulley` should be able to spin freely without resistance
	- The bolt should, however, be tightened enough to eliminate lateral pulley movement within the `belt-tensioner-arm`

	![](img/gt2-idler-pivot-bolt.png)
	
## Create front-left-leg
- Remove any stringing from the 3D print with a heat gun
- Insert 3x `m5-hex-nut` into the following regions
	- 2x in bottom of the leg for customer-side `front-leg-extension` mounting 
	![](img/front-leg-extension-mounting-nut1.png)
	![](img/front-leg-extension-mounting-nut2.png)
	- 1x near extrusion pocket for customer-side attachment of front-drag-chain-mount
 	![](img/front-drag-chain-mount-nut.png)
 	
- Insert 1x `m5-nylock-hex-nut` into in the underside of `belt-tensioner-arm` mounting post
	![](img/belt-tension-arm-nut.png)
	
- Install the `belt-tensioner-arm` onto the `front-left-leg`
	![](img/belt-tensioner-arm-asm-install.png)

- Secure the `belt-tensioner-arm` onto the `front-left-leg` with a `M5x40-bolt`
	- Avoid over tightening this bolt as the `belt-tensioner-arm` should be able to pivot freely without *much *resistance
	
	![](img/belt-tensioner-pivot-bolt.png)

- The completed `front-left-leg` should match the image shown below
	![](img/complete-front-left-leg.png)

## Install y-gantry stepper motor onto back-leg (left-side)
- Install y1 cable onto y-gantry stepper motor 
	![]()
- Put 4x M3x8 bolts through the motor mounting holes on the back-leg print
	![]()
- Cable should be routed through the leg such that it exits towards the center of the machine
	- Ensure no wires are being crushed or strained 
	- Zip tie cable in place for strain relief
	- Add a photo to indicate which way to route the cables per side - We need to clarify since everything is symmetrical.
 	![]()
 	![]()
- Reference below picture for example of completed left back-leg
	![]()

## Install front-left-leg and back-leg onto aluminum extrusion 

- Begin by inserting a `525mm-m3-t-nut-bar` into a piece of `600mm-alu-extrusion`
	- There should be about 51.5mm between the end of the `525mm-m3-t-nut-bar` and the right-side end of the `600mm-alu-extrusion` after installation, but it needs to be slide aside in later steps so do not bother to make this perfect right now
	
	![](img/install-tnut-bar.png)
	
- Insert `front-left-leg` and `back-leg` onto 2x pieces of `600mm-alu-extrusion`
	- The `525mm-m3-t-nut-bar` is oriented in the top-side groove of the uppermost `600mm-alu-extrusion`
	- The extrusion pieces should be *fully* inserted into each leg

	![](img/install-legs-onto-ext.png)
	
- Bolt `back-leg` to `600mm-alu-extrusion`
	- Insert 3x `m3-t-nut` into the `600mm-alu-extrusion` pieces before sliding each of them into alignment with the matching bolt holes on `back-leg`

		![](img/back-leg-t-nut-insertion.png)

	- Insert 3x `M5x10-bolt` into `back-leg` and thread the bolts into each corresponding `M3-t-nut` 

		![](img/bolt-back-leg-to-ext.png)

- Bolt `front-left-leg` to `600mm-alu-extrusion`
	- Slide the `M3-t-nut-bar` out of the way *if needed*
	- Insert an `M3-t-nut` into the upper channel of `600mm-alu-extrusion` 
	- Align the `M3-t-nut` with the top-side bolt hole on `front-left-leg`  
		
		![](img/insert-front-leg-top-t-nut.png)
		
	- Insert a `M5x10-bolt` into the top-side bolt hole on `front-left-leg` and tighten it into the `M3-t-nut`
		
		![](img/insert-front-leg-top-m5x10-bolt.png)

	- Slide 2x `M3-t-nut` into the the side channel of lower `600mm-alu-extrusion` and align them with the two bolt holes on `front-left-leg`
		
		![](img/insert-front-leg-bottom-t-nut.png)

	- Insert 2x `M5x10-bolt` into the side bolt holes on `front-left-leg` and tighten each into the corresponding `M3-t-nut`
		
		![](img/insert-front-leg-side-t-nut.png)
		
- Compare the WIP `y-gantry-left` assembly to the image below after completing all previous steps, address any discrepancies as needed before proceeding onward

	![](img/y-gantry-left-process-check1.png)

## Install 550mm linear-rail onto y-gantry-left

![](img/position-y-linear-rail.png)
![](img/insert-y-rail-alignment-jig.png)
![](img/install-11x-linear-rail-bolts.png)

------------

## Install y-gantry stepper motor onto back-leg (right-side)
- Install Y2 cable onto y-gantry stepper motor
	![]()
- Put 4x M3x8 bolts through the motor mounting holes on the back-leg print
	![]()
- Cable should be routed through the leg such that it exits towards the center of the machine
	- Ensure no wires are being crushed or strained 
	- Zip tie cable in place for strain relief
	- Add a photo to indicate which way to route the cables per side - We need to clarify since everything is symmetrical
	![]()
	![]()
- Install 2x `extrusion-cable-clip` in position shown below to properly manage the stepper motor's cable
	![]()
- Reference below picture for example of completed right back-leg