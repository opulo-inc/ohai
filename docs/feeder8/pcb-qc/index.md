## QC

### Programming

1. Confirm that the jig is properly pluged into the power supply and the laptop at Docker. 

<img src="img/IMG_4492 2.webp" width="60%" height=auto>

* Plug both motors into the `feeder-mobo` being programmed.
  
    <img src="img/img2.webp" width="60%" height=auto>

<!-- 1. While pushing down, secure the board into the jig by twisting the green retention arm, and the swiveling slot.
  
    ![](img/green-arm.webp)
    ![](img/swivel-slot.webp) old instructions i'll keep here.  -->

* Carefully line the board up with the edge of the jig. 

    <img src="img/img8.webp" width="60%" height=auto>

!!! Note "Hold it Partner"
    * We don't want to be sliding it around on the pins in the jig. Line it up and gently place it down. 

    <img src="img/img5.webp" width="60%" height=auto>

<!-- 1. Lock the slot in place with the key.

    ![](img/key.webp) -->

* You are going to have to hold the swivel to the pins on the side of the board. This keeps the jig & `feeder-mobo` powered so the program can be recieved. 
    
    <img src="img/img6.webp" width="60%" height=auto>

### The terminal (dun dun dun)

1. Flash firmware by typing `flashphoton` into a terminal on the QC computer at Docker, then hit the enter key. Remember to hold on to your swivel! 

    <img src="img/img7.webp" width="60%" height=auto>

* The terminal will let you know if the program installed correctly or not. 

<!-- 1. If you see the terminal say `Target voltage: 3.3v` at the beginning, and `[Inferior 1 (Remote target) killed]` at the end, the feeder was successfully programmed. -->

### Testing

With the `feeder-mobo` still loaded in the jig, check the following:

 <img src="img/img1.webp" width="60%" height=auto>

1. Tap the forward button. You should see:
   
    1. Peel motor spins.
    1. Drive motor spins forward a small amount.
    1. The LED turns pure white.
   
2. Tap the backwards button. You should see:
   
    1. Peel motor spins in the opposite direction.
    1. Drive motor spins one direction, then the other.
    1. LED turns pure white.

!!!failure "If any of this fails to happen, move the board to `NEEDS WORK`"

!!!success "If both motors move both directions, the led turns pure white, and both buttons work, move the board to `PASSED`"
  
## SMT Troubleshooting

### `Is the feeder inserted?` Error

* Find the feeder that has the `Enabled?` checkbox *unchecked*.
* In the settings menu for that feeder, click the `Find` button. Check to see that the slot address now has a number.
* Recheck the `Enabled?` checkbox for the feeder.
* Hit the play button on the job to resume.

### Mispick

* Set pick position. If it wasn't set well to begin with, try tuning it to be more accurate.
    * Select the feeder from the list under the `Feeders` tab in OpenPnP.
      ![](img/opnp-feeder-tab.webp)
    * Click the `Move Nozzle To Position` button.
    * using the jog controls in OpenPnP, adjust the nozzle tip to be in the exact center of the part, and gently pressing into the part.
    * Capture the new, better pick position with the `Capture Nozzle Position` button.
    * Jog the nozzle up to prevent a collision.
    * Click the `Pick Part` button in OpenPnP to test the newly captured pick position.
* Check the nozzle tip for clogs.
    * If the nozzle tip has some solder paste stuck in the tip, it won't pick nearly as well.
    * Remove the nozzle tip from the nozzle, and hold it up to a light. Check to see if you can see light shining through the tip.
    * If there's a blockage, clear it with some magnet wire. If it's difficult to clear, try soaking in IPA. Ask your manager about doing this if you think it's necessary.
* Increase dwell time.
    * If the pick movement is too quick, it's possible that the pump doesn't pull enough vacuum to grab the part before moving away from the tape.
    * This can be adjusted in the OpenPnP `Machine Config` tab under the relevant nozzle tip in the `Nozzle Tips` section. Increase the value under `Pick Dwell Time`.