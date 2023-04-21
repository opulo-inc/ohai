# PCB Assembly
This section will guide the reader on how to properly assemble and test a `feeder-mobo` for further use in `feeder-8mm`

## Solder Paste
* Drop the feeder panel into the stencil jig.
* Squeegee the board with `Chipquik 138` solder paste.
* Immediately clean the stencil once complete.


## SMT PnP
* Mount the panel onto the Feeder Lumen and run the job in OpenPnP.

## Reflow
* Run the Reflow Master at the regular setting, `Chipquik 138`

## QC
### Programming
* Install the `feeder-mobo` into the test jig:
    * Plug both motors into the board being tested.
      ![](img/connect-motors.jpg)
    * While pushing down, secure it in place by twisting the green retention arm, and the swiveling slot.
      ![](img/green-arm.jpg)
      ![](img/swivel-slot.jpg)
    * Lock the slot in place with the key.
      ![](img/key.jpg)
    * Flash firmware by typing `flash` into a terminal on the QC computer.
    * If you see the terminal say `Target voltage: 3.3v` at the beginning, and `[Inferior 1 (Remote target) killed]` at the end, the feeder was successfully programmed.

!!! note
    The indicator light turning red is a quick way to check that the firmware has been successfully programmed.

* If you do not see the light turn red, or the terminal does *not* say `The program is not being run.`, the board was not programmed.

### Testing

* With the `feeder-mobo` still loaded in the jig, check the following:
  * Tap the backwards button. You should see:
    * Drive motor spins one direction, then the other.
    * Peel motor spins one direction, then the other.
    * LED turns pure white.
  * Tap the forward button. You should see:
    * Drive motor spins forward a small amount.
    * Peel motor spins one direction, then the other.

!!!failure "If any of this fails to happen, move the board to `NEEDS WORK`"

!!!success "If both motors move both directions, the led turns pure white, and both buttons work, move the board to `PASSED`"
  