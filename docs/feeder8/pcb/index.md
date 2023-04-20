# PCB Assembly
This section will guide the reader on how to properly assemble and test a `feeder-mobo` for further use in `feeder-8mm`

## Solder Paste
* Drop the feeder panel into the stencil jig
* 


## SMT PnP
* run smt lmao

## Reflow
* Run the Reflow Master at the regular setting, `Chipquik 138`

## QC
### Programming
* Install the `feeder-mobo` into the test jig as shown.
  PIC
* While pushing down, secure it in place by twisting the green retention arm, and the swiveling slot.
* Lock the slot in place with the key
* Flash firmware by typing `flash` into a terminal on the QC computer.
* If you see the terminal say ``, the feeder was successfully programmed.
  
!!! note
    The indicator light blinking gold, then turn red is a quick way to check that the firmware has been successfully programmed.

* If you do not see lights blink, and the terminal does *not* say `text`, the board was not programmed.

### Testing

* With the `feeder-mobo` still loaded in the jig, check the following:
  * Tap the backwards button. You should see:
    * Drive motor spins one direction, then the other.
    * Peel motor spins one direction, then the other.
    * LED turns pure white.
  * Press and hold the forward button. You should see:
    * The drive motor spins as long as you hold the button.

!!!failure "If any of this fails to happen, move the board to `TODO`"

!!!success "If both motors move both directions, the led turns pure white, and both buttons work, move the board to `TODO`"
  