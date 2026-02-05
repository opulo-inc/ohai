# Feeder Connection Kit

This page will guide the reader on how to properly prepare a `feeder-connection-kit`, from initial assembly to final packaging.

![](img/blade-packaging3.webp)

## feeder-blade-panel (PCBA)
This section will guide the reader on how to properly create a `feeder-blade-panel (PCBA)`

#### SMT
* Paste blade panels three at a time.
* Load three pasted blade panels into the Blade Lumen
* Run the job in OpenPnP
* Remove the panels and reflow them in the oven *one at a time*
* Inspect for any shorts or shifted components and rework as needed
* Add the 120R termination resistor to the 50th slot position if needed
* Place the completed `feeder-blade-panel (PCBA)` units into the yellow bin found at the blade assembly work station
    ![](img/slots-in-bins3.webp)

#### Programming
* Grab the stylus from the blade programmer
  ![](img/pgrm-slot-set-pca-14.webp)
* Ensure that the address is set to `1`
    * You can adjust the address with the buttons to the right of the screen
* Place the spring pins of the stylus against the pads on `Slot #1`
    * Make sure the orientation matches as shown below:
          ![](img/pgrm-slot-set-pca-15.webp)
          ![](img/program-blade-4.webp)

* Press the switch on the stylus when all spring pins are compressed against the pads
    ![](img/program-blade-5.webp)
* Look at the screen:

    !!!failure "The programming step failed if you see *anything other than a `success` message*"
        * The jig is capable of detecting shorts, and will fail programming if one is detected
            * The screen will display which pin it sensed has shorted
        * If a failure is observed perform any necessary cleanup and try again
        * Note that the jig will remember the last place you left off

    !!!success "If the programmer reads `1 - SUCCESS` proceed to the next slot position"
        ![](img/program-blade-3.webp)

* After successfully programming address `1`, repeat this step for the next 49 addresses while moving in the following order:<br> <span style="color:#FF00FF"> Pink (4th row) </span> → <span style="color:Red"> Red (2nd row) </span> → <span style="color:Green"> Green (3rd row) </span> → <span style="color:#0096FF"> Blue (1st row) </span>
    ![](img/programming-blade-4.webp)

    !!!warning "Pay **extreme attention** to avoid programming any slot with the wrong value"

#### QC
Ensure your completed PCBA meets the following requirements:

- Switch the programmer to `QC Mode` and confirm that Slots #1, #13, #23, #26, #38, #48, and #50 each have a programmed value that matches the top-side silkscreen text

    !!!info "For example:"
        Confirm that Slot #26 is *actually* programmed as Slot #26

- Gold spring finger pads are free of damage

Place each quality checked `feeder-blade-panel (PCBA)` into the appropriate QC bin:

!!!success "Place all QC passing `feeder-blade-panel (PCBA)` units into the green QC bin"
    ![](img/slots-in-bins1.webp)

!!!failure "Place all QC failing `feeder-blade-panel (PCBA)` units into the red QC bin"
    Be sure to label each defective unit with any issues it has
    ![](img/slots-in-bins2.webp)

The next step is to proceed to `Feeder Blade Set Final Assembly`

## Feeder Blade Set Final Assembly

This section will guide the reader on how to properly assemble and package a `feeder-blade-set`

### Materials Prep

* Check 2x `blade-12` and 2x `blade-13` using the granite block to ensure the print printed without warping
    ![](img/IMG_2604.webp)

### Assembly Process
* Begin by separating a `feeder-blade-panel (PCBA)` into four separate rows
    ![](img/break-slots2.webp)
    ![](img/break-slots25.webp)
    ![](img/slot-set-3.webp)

* Install each `blade13-pcb` into a `blade13` 3D print to create `feeder-blade13-asm`
    ![](img/place-slots-in-blade2.webp)
    ![](img/place-slots-in-blade1.webp)

* Set `feeder-blade13-asm` into the `feeder-blade-cradle-jig`
    ![](img/place-blade-in-jig.webp)

* Proceed to install 5x `M3x8-self-threading-screw` into the WIP `feeder-blade13-asm`
    * Use an automatic torque driver set to `6`

    ![](img/install-m3-screws.webp)

* Remove the blades from the `feeder-blade-cradle-jig`
* Loosely install 5x `M5-t-slot-nut` and 5x `M5x10-bolt` into each feeder blade for subsequent use in mounting onto a feeder rail
    ![](img/install-t-nut1.webp)
    ![](img/install-t-nut2.webp)

* Repeat these above steps until you have created 2x `feeder-blade13-asm` and 2x `feeder-blade12-asm`
    * The steps to make the `feeder-blade12-asm` are the same as the 13-gang version, the only differences are that the 3D print and PCB are a 12-slot variant.

!!!success "Once all 4 assemblies have been prepared, you have finished building a `feeder-blade-set`"
    ![](img/feeder-blade-set.webp)

### Next Steps
The next step is to proceed to either:

* [Feeder Connection Kit Accessories](#feeder-connection-kit-accessories) - provided you are making a Feeder Connection Kit
* [Front-feeder-rail / Rear-feeder-rail Assembly](https://ohai.opulo.io/lumen/feeder-rail/) - provided you are making a LumenPnP

## Feeder Connection Kit Accessories

This section will guide the reader on how to properly prepare the accessories that go into a `feeder-connection-kit`.

#### bagged-extrusion-cable-clips

* Place 10x `extrusion-cable-clip` pieces into a `3x4-bag` before sealing it shut

    ![](img/IMG_3667.webp)
    ![](img/IMG_3666.webp)

* Place each `bagged-extrusion-cable-clips` set into a <span style="background-color:yellow"> yellow NEEDS QC bin</span> while it awaits inspection

    ![](img/IMG_6181.webp)

* Weigh each `bagged-extrusion-cable-clips`, confirming it weighs `19.9g`

    ![](img/IMG_6182.webp)

* Place the `bagged-extrusion-cable-clips` pieces that pass weight check into a <span style="color:green"> green QC-Pass bin</span>

    ![](img/IMG_6185.webp)

#### Hex Key for Drive Wheel Adjustment

* Adhere a "hex key bag label" onto a `2x3-bag`

    ![](img/IMG_3668.webp)

* Place a hex key into the plastic bag before resealing it

    ![](img/IMG_3669.webp)

#### Collect feeder-blade-harness-set

* Collect a `feeder-blade-harness-set` [ASM-0079-02] from inventory

    ![](img/feeder-blade-harness-set-rev02.webp)

#### Feeder-cable-adapter

###### Assemble `feeder-cable-adapter`

- Create a `50mm-idc-ribbon-cable` that matches the image below
    ![alt text](img/connection-kit-ph3.webp)
    ![alt text](img/connection-kit-ph5.webp)
- Assemble `feeder-blade-idc-adapter-pcba`
    ![alt text](img/connection-kit-ph1.webp)
    ![alt text](img/connection-kit-ph6.webp)
- Glue `blade-adapter-pin-cover` onto the PCBA
    ![alt text](img/connection-kit-ph7.webp)
    ![alt text](img/connection-kit-ph13.webp)
    ![alt text](img/connection-kit-ph4.webp)

- Connect `50mm-idc-ribbon-cable` to `feeder-blade-idc-adapter-pcba`
    ![alt text](img/connection-kit-ph2.webp)
    ![alt text](img/connection-kit-ph8.webp)

###### Packing `feeder-cable-adapter`
* Add 1x `feeder-blade-idc-adapter` and 2x `blade-jumper-v4` into `2x3-bag`
    ![alt text](img/connection-kit-ph9.webp)
* Seal bag shut
    ![alt text](img/connection-kit-ph11.webp)

!!!note "If the `feeder-cable-adapter` is being prepared for individual sale, adhere a `build-number-sticker` to the outside of the packaging"
    ![alt text](img/IMG_2182.webp)

!!!success "These assemblies can now be set aside for further use in packout"

## Packaging Feeder Connection Kit

This section will guide the reader on how to properly package a `feeder-connection-kit`

### Prep the cardboard tray

* Apply hot melt glue to inside faces of `feeder-accessory-tray`

    ![](img/hot-glue.webp)

* Immediately after gluing, folding `feeder-accessory-tray`

    ![](img/feeder-connection-kit-1.webp)

### Package `feeder-connection-kit`
* Install the following items into the `feeder-accessory-tray`:
    * `feeder-blade-set`
    * **`feeder-blade-harness-set`**

        !!!warning "DO NOT MIX THIS UP WITH THE `feeder-slot-cable-harness` WE USED TO USE HERE"
            ALSO BE SURE IT IS REWORKED TO INCLUDE JUMPERS

    * `feeder-connection-kit-add-ins`
    * `feeder-programmer`
    * `bagged-extrusion-cable-clips`
    * `drive-wheel-adj-key`

    ![alt text](img/connection-kit-ph10.webp)

    !!!warning "The above photo forgets to show the bagged `drive-wheel-adj-key`"

* Add some foam to the `feeder-connection-kit` tray to protect the items in transit

    !!!info "The foam shown in use here is 3 pieces of foam covering from 2020 aluminum extrusion"
