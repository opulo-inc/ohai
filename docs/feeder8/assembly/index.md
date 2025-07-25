# Final Assembly

## Motherboard Assembly

1. Plug the `peel-motor-asm` into the 2-pin connector on the PCB
   
   	![](img/PXL_20230125_205520692.webp)

2. Slide the `peel-motor-asm` into its corresponding cavity in `feeder-frame-8mm`
	* Tuck the excess cable into the empty region behind the `peel-motor-asm`

   	![](img/PXL_20230125_205545511.webp)

1. Tilt the PCB slightly to insert the `drive-motor` cable into the six-pin connector on `feeder-motherboard`
		![](img/drivemotor.webp)


3. Press the PCB flat into `feeder-frame-8mm`
	* Make sure the cable is not caught between them - it should lay flush

   	![](img/PXL_20230125_205601695.webp)

1. Press `drive-motor` into its cavity while ensuring it is flush with the back of `feeder-frame-8mm` and the cables are well routed, as shown
		![](img/drivemotor3.webp)
		![](img/drivemotor2.webp)

4. Insert 4x `M3x12mm` flathead screws into the holes in the PCB as shown below
	* Use automatic screwdriver with power set to 4

	![](img/IMG_2233.webp)
	![](img/IMG_2235.webp)

!!! inspect "QC Check - Test if the buttons on `feeder-frame-8mm` can easily actuate the switches on the PCB before proceeding"

1. Install a `drive-motor-bracket`
   
   	![](img/bracket1.webp)

10. Insert 2x `M3x12mm` flathead screws
 	* Turn the screws in equal amounts before tightening them both to the final torque spec
 	* Tighten the 2x `M3x12mm` flathead screws to `55 cN.m (5.5 N.m)` with a `2mm` hex head driver

  	 ![](img/bracket2.webp)
 	 ![](img/bracket3.webp)

	!!! failure "*DO NOT OVER-TIGHTEN*"
		Over-tightening can lead to bracket damage and motor skewing in the `feeder-frame-8mm`
			![](img/install-bracket-4.webp)


11. Check that the `drive-motor` is still flush and hasn't skewed because of tightening
	* If it appears crooked or not flush, loosen the screws and readjust the `drive-motor`

   	![](img/bracket4.webp)

1. Use a blade to clean up any loose plastic that was pushed through the `drive-motor-bracket` mounting screw holes during installation 

!!!warning "Failure to perform this step may cause issues with cosmetic sticker installation later on"


![](img/cleanscrews1.webp)
![](img/cleanscrews2.webp)


## Install the `release-lever`

!!!warning "Wearing safety glasses is required while installing springs"

5. Install the spring
	* Grab a spring and a `release-lever`, and hold the spring in the `release-lever` as shown
	* Match the other end of the spring up with the circular cutout in the `feeder-frame-8mm` print
	* Finally, drop the `release-lever` into the `feeder-frame-8mm`
   
   	![](img/release1.webp)
   	![](img/release2.webp)

6. Insert an `M3x15mm` flathead screw from the backside and drive it in using the automatic screwdriver on the 4 setting (0.25 N*m).
	* Make sure the arm can still swivel easily
	* Make sure that the arm does not have any lateral movement

   	![](img/release3.webp)

## Install the `peel-gear-box`

1. Obtain `peel-gear-box`
	![](img/peel1.webp)

1.  Place `peel-gear-box` in place, engaging with the `worm-gear` in `peel-motor-asm`
	![](img/peel2.webp)
	![](img/peel3.webp)

1. Insert 2x `M3x12mm` flathead screws into the locations shown using automatic screwdriver set to 6
	![](img/peel4.webp)

## Install the `drive-wheel-asm`

!!!info "Note on `drive-motor` shaft angle"
	Drive-motor units may come from factory with a shaft rotated at an angle that's not ideal for set-screw tightening. If this applies to the feeder you are handling, follow the steps below:
	
	* Power up to the affected units by plugging it into Gundam
	* Press the feeder's jog-forward button until the shaft is at an optimal angle for subsequent assembly work

	![](img/install-gear-2.webp)
	
	![](img/install-gear-1.webp)

12. Place the `Drive Wheel Shims` in the `drive-wheel-asm` cavity as shown, with the `drive-motor` shaft sticking through it

	![](img/shim1.webp)

13. Drop the `drive-wheel-asm` onto the `drive-motor` shaft
   
	![](img/wheel1.webp)

14. With one hand, **press down firmly on** `drive-wheel-asm` while using your free hand to tighten the `shaft-collar-asm` set-screw
	* Tighten the `M2.5x3mm-set-screw` to `30 cN.m (0.3 N.m)` with a `1.27mm` or `1.3mm` hex head driver
  
	 ![](img/wheel2.webp)

15. Remove the `Drive Wheel Shims`
     
## Install `drive-motor-cover`

18. Place a `drive-motor-cover` over the `drive-wheel-asm`
	* The `drive-motor-cover` should lay flat with none of the cables preventing it from being flush against `feeder-frame-8mm`

    ![](img/cover1.webp)

19. Insert 3x `M3x12mm` flathead screws in the locations shown below
	* Use automatic screwdriver set to 6

    ![](img/cover2.webp)
	![](img/IMG_2234.webp)

!!!success "You may now proceed to OQC"
