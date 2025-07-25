# Packaging LumenPnP v4

## Reviewing packaging layout

1. The following components are packaged into the `lower-foam-tray`:
	* `y-gantry-left`
	* `y-gantry-right`
	* `x-gantry`
	* `nozzle-rack-asm`
	* `getting-started-kit`
	* `tool-kit-bag`
	* `feeder-blade-harness-set`
	* `x-cable-chain-support`
	* 2x `front-leg-extension`
	* 2x `back-leg-extension`

2. The following components are packaged into the `upper-foam-tray`:
	* `primary-staging-plate`
	* `aux-staging-plate`
	* `static-camera-foot`
	* `aux-staging-plate-foot`
	* `bagged-10x-extrusion-cable-clips`
	* `squaring-bracket`
	* `y-limit-striker`
	* `drag-chain-assembly`
	* `front-feeder-rail`
	* `rear-feeder-rail`
	* `24v6A-power-supply`
	* `power-cable`

## Package `lower-foam-tray`

!!!warning "The following steps must be conducted by someone other than the original assembler."

### `tool-kit-bag` and `back-leg-extension`

1. Confirm `lumenpnp-v4-hardware-kit` is present in `tool-kit-bag`

	!!!success "If OK continue onward"

2. Add `tool-kit-bag` into the middle region of `lower-foam-tray`
	* Orient the `tool-kit-bag` so its Opulo logo faces the `x-gantry-toolhead`

	![alt text](img/IMG_24.webp)

1. Insert 2x `back-leg-extension` - stacking them on the left of `tool-kit-bag`
	* Confirm both pieces have `rubber-feet` installed

	![alt text](img/IMG_25.webp)
	![alt text](img/IMG_26.webp)

### `getting-started-kit` and `feeder-blade-harness-set`
1. Insert `getting-started-kit` into the lower left region of tray
	* QC must be performed if collecting `getting-started-kit` pieces from anything other than a <span style="color:green"> green QC-Pass bin</span>
	* QC this item by weighing and confirming a mass of either 168g or 150g (varies based on the version of tape used)

	![alt text](img/IMG_28.webp)
	![alt text](img/IMG_29.webp)


2. Insert `feeder-blade-harness-set` to the right of `getting-started-kit`

	!!!warning "Please remember this is the new JST PH cables! We do not need to make IDC cables anymore."

	![alt text](img/IMG_30.webp)
	![alt text](img/IMG_31.webp)

### `x-gantry`
1. Perform `x-gantry` QC
	* `GT2-belt` has been trimmed to appropriate length:
		* Flush on `x-motor-mount` side
		* Approx. 15mm on `x-idler-mount` side
	* `lens-cap` is present on `top-camera`
	* The wire connectors on both `NEMA-11-stepper-motor` units face away from each other
	* Confirm each `nozzle-holder` fulfills the following requirements:
	    * Appears lubricated
		* Moves smoothly and in a straight path when actuated manually
		* Springs back to the extended position after being depressed by hand
	* `z-belt-loop` feels appropriately tensioned when plucked
	* Each `z-gantry` moves smoothly when actuated back-and-forth by hand
	* 1x `M5-hex-nut` is installed in `x-gantry-back` for mounting `cable-splay`
	* The wire connector on `NEMA-17-stepper-motor` that is attached to `x-gantry-front` faces `z-limit-switch`
	* The wire connector on `NEMA-17-stepper-motor` that is attached to `x-motor-mount` faces away from `xy-limit-switch`
	* `linear-rail` is centered atop `alu-extrusion`
	* `x-idler-mount` and `x-motor-mount` are secured to `alu-extrusion` with 2x `M5x10-bolt` per side
	* `belt-tensioner-arm` is installed on `x-idler-mount` in the correct orientation (IE acorn-nut facing touches print)
	* `timing-pulley` for both x & z  are tightened down and at proper height
	* `GT2-belt` lays flat and is roughly centered in `alu-extrusion` channel
	* `GT2-belt` has been correctly tensioned
	* `x-gantry-toolhead` moves smoothly when actuated back and forth by hand
	* `top-ring-light` is present with the wire connector visible
	!!!success "If all checks pass, continue onward"

* Package `x-gantry` into `lower-foam-tray`

	![alt text](img/IMG_32.webp)

### `x-cable-chain-support`
* Place `x-cable-chain-support` on the bottom of the `y-gantry` pocket

	![alt text](img/IMG_33.webp)

### `y-gantry-right`

![](img/y-gantry-right.webp)

1. Perform `y-gantry-right` QC
	* Confirm M5 bolts are installed in every recessed region
	* `M5-hex/square-nut` installed where required:
		* 2x `M5-hex-nut` pressed into bottom of `front-right-leg`
  		* 1x `M5-hex-nut` pressed into bottom of `back-leg`
  		* 2x `M5-hex-nut` pressed into `y-gantry` on textured face
  		* 2x `M5-square-nut` pressed into `y-gantry` for attaching `x-cable-chain-support`
	* `GT2-belt` has been trimmed to appropriate length:
		* Flush on `front-right-leg` side
		* Approx. 15mm on `back-leg` side
	* `GT2-belt` has been correctly tensioned
	* `belt-tensioner-arm` is installed on `front-right-leg` in the correct orientation (IE acorn-nut facing touches leg)
	* `linear-rail` is centered atop `aluminum-extrusion`
	* `y-gantry` sits flat on `linear-rail-carriage`
	* `y-gantry` feels smooth and free of friction across the y-min to y-max travel range when actuated by hand
	* `GT2-belt` lays flat in the `alu-extrusion` channels
	* 3x `extrusion-cable-clip` have been installed onto the lower `alu-extrusion`
	* `timing-pulley` is tightened down and at proper height
	*  `Y2` cable is secured with a zip-tie and exits the port labeled `Y2`

	!!!success "If all checks pass, continue onward"

*  Package `y-gantry-right` into `lower-foam-tray`
  
	![alt text](img/IMG_34.webp)

### `y-gantry-left`

![](img/y-gantry-left.webp)

1. Perform `y-gantry-left` QC
	* Confirm M5 bolts are installed in every recessed region
	* `M5-hex/square-nut` installed where required:
		* 2x `M5-hex-nut` pressed into bottom of `front-left-leg`
		* 1x `M5-square-nut` pressed into side of `front-left-leg` for use with `y-limit-striker`
  		* 1x `M5-hex-nut` pressed into bottom of `back-leg`
  		* 2x `M5-hex-nut` pressed into `y-gantry` on textured face
  		* 2x `M5-square-nut` pressed into `y-gantry` for `x-cable-chain-support` mounting
	* `GT2-belt` has been trimmed to appropriate length:
		* Flush on `front-left-leg` side
		* Approx. 15mm on `back-leg` side
	* `GT2-belt` has been correctly tensioned
	* `belt-Tensioner-arm` is installed on `front-right-leg` in the correct orientation (IE acorn-nut facing touches leg)
	* `linear-rail` is centered atop `aluminum-extrusion`
	* `y-gantry` sits flat on `linear-rail-carriage`
	* `y-gantry` feels smooth and free of friction across the y-min to y-max travel range when actuated by hand
	* `GT2-belt` lays flat in the `alu-extrusion` channels
	* 3x `extrusion-cable-clip` have been installed onto the lower `alu-extrusion`
	* `timing-pulley` is tightened down and at proper height
	* `Y1` cable is secured with a zip-tie and exits the port labeled `Y1`

	!!!success "If all checks pass, continue onward"

*  Package `y-gantry-left` into `lower-foam-tray`

	![alt text](img/IMG_35.webp)

### `front-leg-extension` and `nozzle-rack-asm`
1. Insert `nozzle-rack-asm` into the bottom right pocket
	* Confirm `nozzle-rack` has all its mounting hardware installed by peering through the bag

	![alt text](img/IMG_36.webp)
	![alt text](img/IMG_37.webp)

1. Insert 2x `front-leg-extension`, stacking them in the same region
	* Confirm both pieces have `rubber-feet` installed

	![alt text](img/IMG_38.webp)
	![alt text](img/IMG_39.webp)

### Confirm the contents of `lower-foam-tray`
Confirm the `lower-foam-tray` matches the image shown below before continuing:

![alt text](img/IMG_40.webp)

## Package `upper-foam-tray`

!!!warning "The following steps must be conducted by someone other than the original assembler."

### misc. parts
1. Insert the following items into the **right-side** pocket of `upper-foam-tray`

	!!!note "Package each of the following items while inspecting them for their given QC inspection criteria"
	* `squaring-bracket` - confirm print is latest revision (gold PLA & hex wrench feature)
	* `y-limit-striker` - confirm `M5-thumb-screw` is installed and appears to stick-out `1.5mm`
	* `aux-staging-plate-foot` - confirm top-side M3 bolt and bottom-side `rubber-foot`
	* `static-camera-foot` - confirm bottom-side `rubber-foot`
	* `bagged-10x-extrusion-cable-clips`
		* Only pull these items from a <span style="color:green"> green QC-Pass bin</span>.

	![alt text](img/IMG_41.webp)
	![alt text](img/IMG_43.webp)

1. Insert the following into the **left-side** pocket
    * `24v6A-power-supply` (unboxed)
    * `power-cable`

	![alt text](img/IMG_44.webp)
	![alt text](img/IMG_45.webp)
	![alt text](img/IMG_46.webp)

2. Confirm the left and right side pockets match the image below before continuing

	![alt text](img/IMG_47.webp)

### `primary-staging-plate`
1. Inspect `primary-staging-plate` before packaging it into the foam tray
	* Review the `primary-staging-plate` for the presence of all major components
		* `datum-board`
		* `bottom-camera-assembly` (with lens cap removed)
		* 3x `peek-cable-clamp`
		* `bottom-light-harness` and `bottom-camera-harness` w/propper cable managment
			* Ensure that the `bottom-camera-harness` was used and NOT the longer `top-cable-harness`
			* `peek-cable-clamp` usage and rubber-band for securing loose cables

	![alt text](img/IMG_49.webp)

1. Place the `primary-staging-plate` into `upper-foam-tray` in the region shown below

	!!!note "The Opulo logo should face away from the `feeder-rail` pocket"

	![alt text](img/IMG_50.webp)

1. Insert a foam block above each side of `primary-staging-plate`

	![alt text](img/IMG_51.webp)

### `control-box`

1. Insert `control-box` on right-side of `bottom-camera-assembly`

	![alt text](img/IMG_53.webp)

1. Unclip the `box-sn-label` from `control-box` and loosely add it to right side accessory pocket

	![alt text](img/IMG_54.webp)

### `aux-staging-plate`

1. Insert `aux-staging-plate` on top of `primary-staging-plate`

	!!!note "The Opulo logo should face away from the `feeder-rail` pocket"

	![alt text](img/IMG_55.webp)
	![alt text](img/IMG_56.webp)

### `front/rear-feeder-rail`

!!!note "It is much easier to check the entire batch at once for a given inspection, rather than checking each one rail at a time against this entire checklist"

1. Perform QC inspection on the front of `front-feeder-rail` and `rear-feeder-rail` pieces
	
	![alt text](img/IMG_61.webp)

	* Feeder blades are installed sequentially from left to right
	* Wiggle the installed blades to ensure no screws are loose, retightening any if needed
	* Ensure the print is free of defects and fits flush to `alu-extrusion`
	* The 2x (front)/4x (rear) installed `corner-bracket` pieces are flush to the `alu-extrusion`
	* Confirm a `blade-jumper-harness` is installed into each `feeder-rail`
	* Use the `feeder-programmer` to check that Slots `#1`, `#12`, `#13`, '#23', `#25`, `#26`, `#37` `#38`, `#48`, and `#50` are programmed correctly

		!!!success "If all checks pass continue onward"

 2. Add `front-feeder-rail` and `rear-feeder-rail` into  `upper-foam-tray`
	* Orient the rails back-side up, with `rear-feeder-rail` in the lower pocket and `slot #50` on the right  

	![alt text](img/IMG_62.webp)
	![alt text](img/IMG_63.webp)
	![alt text](img/IMG_64.webp)

### `drag-chain`

1. Perform `drag-chain` QC

	* Confirm the following vacuum tubes are present at both ends:
		*  	<span style="background-color:red">**Red**</span> `4mm-pneumatic-tubing`
		*  	<span style="background-color:blue">**Blue**</span> `4mm-pneumatic-tubing`
	* Confirm 3x `zip-tie` used in `cable-splay` are trimmed flush and present
	* Confirm presence of `top-camera-cable`
	* Confirm presence of `x-harness` and double check that `x-harness` has the correct orientation

		![alt text](img/x-harness-qc.webp)

	!!!success "If all checks pass, continue onward"

 2. Place `drag-chain` into `upper-foam-tray`

	![alt text](img/IMG_68.webp)
	![alt text](img/IMG_70.webp)

### Confirm the contents of `upper-foam-tray`

1. Confirm the `upper-foam-tray` matches the image shown below

	![alt text](img/IMG_93.webp)

## Package LumenPnP Box
!!!warning "Perform this process 1 machine at a time"
	It's OK for this work to be performed by the original machine assembler

1. Gather the following items:
	- Empty LumenPnP box
	- Packaged and QC'd upper-foam-tray
	- Packaged and QC'd lower-foam-tray
	- All relevant shipping paperwork, including packing slip, shipping label, and any international forms

	![alt text](img/IMG_77.webp)

2. Remove the `box-sn-label` from the `upper-foam-tray` and adhere it to the LumenPnP box in the region shown below

	!!!warning "It is **critical** that this label matches the serial number listed on the backside of `control-box`"

	![alt text](img/IMG_78.webp)

2. Adhere shipping documents to box
	- Adhere all relevant shipping documentation to the top left side of the LumenPnP box flap
	- Set the packing slip aside **if** it lists product pricing information, otherwise it can be adhered below the shipping label

	![alt text](img/IMG_94.webp)

3. Examine the packing slip and take note of what (if any) additional items must be packaged  

	![](img/packing_slip.webp)

4. Open the [OQC Checklist](https://docs.google.com/forms/d/e/1FAIpQLSddZwlLa26bw81xRC3UofJ12yaRr4eiF1ZQTFnbHVbXxjBo6A/viewform?usp=sharing)
	- Fill out this checklist as you package the LumenPnP

	![](img/oqc-form.webp)

5. Complete the first page of the `OQC Checklist` page

	![](img/QC-Form/2-qc-form.webp)

6. Examine the contents of the `lower-foam-tray` and complete the corresponding `OQC Checklist` page

	![](img/QC-Form/3-qc-form.webp)

7. Place the packaged `lower-foam-tray` into the LumenPnP packaging
	* Orient the tray so that the packaged `x-gantry` is closer to the Opulo logo side of the box

	![alt text](img/IMG_79.webp)

8. Examine the contents of the `upper-foam-tray` and complete the corresponding `OQC Checklist` page

    ![](img/QC-Form/3.5-qc-form.webp)

9. Place the packaged `upper-foam-tray` into the LumenPnP packaging
    * Orient the tray so that the staging plates are closer to the Opulo logo side of the box

	![alt text](img/IMG_82.webp)

11. Complete the corresponding `OQC Checklist` page

	![](img/QC-Form/4-qc-form.webp)

12. Reference the order's `packing list` to determine if the box must include *any additional items*
	- If the order **includes** additional items, select `Yes` to this page's last question before proceeding
	- If the order **does not include** additional items, select `No` to this page's last question before proceeding

12.  If you answered `Yes` to the previous question you will be directed to the `Extra Items Checklist` page
	- Package any additional items required into the open void regions of the LumenPnP's packaging
	
	!!!info "If the order includes `feeders` or items suitable for a `feeder-accessory-tray` package them above the `upper-foam-tray` like so:"
		![alt text](img/IMG_83.webp)
		![alt text](img/IMG_86.webp)

	- After adding any additional items to the order, check-off any additional items this order contains before proceeding

		![](img/QC-Form/5-qc-form.webp)

15. Fill out a `getting-started-card` with the machine's `version number`

    ![](img/getting-started-card.webp)

16. Peel the wax paper off the back of `getting-started-card` and adhere it to `top-foam sheet`
    * Orient the card so that it's bottom edge faces toward the Opulo logo side of the box

	!!!warning "If the order being packed included feeders skip this step"

	![alt text](img/IMG_90.webp)
	![alt text](img/IMG_91.webp)

14. Install a `top-foam-sheet` above the `upper-foam-tray`

	!!!warning "If the order being packed included feeders skip this step"

	![alt text](img/IMG_92.webp)

	!!!note "Is this LumenPnP being shipped with feeders? Follow this note below instead of the above step!"
		Use `feeder trays` and a `top-cardboard-pad` instead of a `top-foam-sheet` **if** the LumenPnP order includes either feeders and/or items that use a `feeder-accessory-tray`
		![alt text](img/IMG_87.webp)
		![alt text](img/IMG_88.webp)
		![alt text](img/IMG_89.webp)

13. Proceed to the `Finalize Shipment` page of the `OQC Checklist` and work your way through alongside following these last steps

	![](img/QC-Form/6-qc-form.webp)

17. Tape the LumenPnP box shut

	![alt text](img/IMG_95.webp)

18. Adhere an `orange sticker` to the top-right corner of the box.

	![alt text](img/IMG_96.webp)

19. Click `Submit` on the final page of `OQC Checklist` page

	![](img/QC-Form/8-qc-form.webp)

!!!success "The LumenPnP should now be ready for fulfillment!"
