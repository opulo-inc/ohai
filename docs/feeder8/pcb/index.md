# PCB Assembly

This section will guide the reader on how to properly assemble and test a `feeder-mobo` for further use in all width `feeder` variants.

## Solder Paste

1. Inspect the stencil. Make sure all the voids are clear of debris and solder paste.
   
    ![](img/stencil-ng.webp){: style="height:350px"}
    ![](img/stencil-ok.webp){: style="height:350px"}

1. If the stencil is not clean, squirt IPA onto the stencil.

    ![](img/stencil-ipa.webp)

1. Use a paper towel to **very lightly** wipe down the stencil. Do **not** apply hard pressure, as it'll cause the stencil to cut the paper towel and cause debris to form.

    ![](img/stencil-cleaning-top.webp)
    ![](img/stencil-cleaning-bottom.webp)

2. Grab a new feeder panel.

    ![](img/panel.webp)

3. Insert the panel into the jig.

    ![](img/panel-in-jig.webp)

4. Check to make sure that the stencil is aligned with the pads on the panel.

    ![](img/stencil-aligned.webp)

5. Grab the jar of **FRESH** Loctite GC10 solder paste.

    ![](img/loctite-gc10.webp)

6. Remove the plug from the jar.

    ![](img/paste-plug.webp)
    ![](img/paste-plug-removed.webp)

7. Remove some paste from the jar with the paddle, and spread it along the top of the stencil.

    ![](img/applying-paste.webp)

8. IMMEDIATELY replace the plug.

    ![](img/plug-reinserted.webp)

9. Grab the squeegee tool.

    ![](img/squeegee.webp)

10. Align the squeegee on the stencil so that the **boltheads are facing up**.

    ![](img/boltheads-up.webp)
    ![](img/about-to-squeegee.webp)

11. Squeegee paste across the panel. **Apply plenty of force**. Make sure you use the correct angle. An angle too high will result in not enough paste, and an angle too low will result in too much.

    ![](img/correct-angle.webp)
    ![](img/angle-high.webp)
    ![](img/angle-low.webp)
    ![](img/angle-range-results.webp)

12. With a high angle, scrape up any remaining paste on the top of the stencil. Do this once in the Y axis, and twice in the X axis, covering the whole panel.

    ![](img/scrape-y.webp)
    ![](img/scrape-x.webp)

13. Lift the stencil away from the board in a smooth motion. **Do NOT bring the stencil back onto the PCB after lifting**.

    ![](img/lift-stencil.webp)

14. Inspect the paste. Make sure that there is a sufficient gap between pads. If the paste is heavily bridging, wipe off the paste and redo the process.

    ![](img/paste-ok.webp)
    ![](img/paste-ng.webp)

15. Clean the stencil like before.

    ![](img/stencil-ipa.webp)
    ![](img/stencil-cleaning-top.webp)
    ![](img/stencil-cleaning-bottom.webp)

16. Repeat the process of adding a blank panel, squeegeeing, and cleaning until the necessary amount of panels are pasted. Only paste what you are **SURE** you can populate and reflow in the same day. If you complete that number early, you can paste more boards and run more jobs, but leaving a panel pasted and not reflowed overnight is **not acceptable**.

17. If you are done pasting, scrape any remaining paste off of squeegee with the paddle, and scrape it into the **OLD Paste container**.

    ![](img/scrape-paste-squeegee.webp)
    ![](img/paste-removed-squeegee.webp)
    ![](img/paste-recycle.webp)

18. When done pasting, immediately wash your hands, and wipe down the work area. We do not use leaded solder paste at Opulo, but even the unleaded stuff isn't great to have hanging around.

    ![](img/wash-hands.webp)


## SMT

1. Identify the Lumen configured for feeder PCB production.

    ![](img/feeder-lumen.webp)

1. Place a panel onto each of the panel platters.

    ![](img/panels-in-place.webp)

1. Use the M3x8mm screws to bolt the panel into the jig using the Populo screwdriver by the machine.

    ![](img/populo.webp)
    ![](img/bolt-placement.webp)
    ![](img/bolt-1.webp)
    ![](img/bolt-2.webp)

1. Log into the Thinkpad used to control the feeder Lumen.

    ![](img/ubuntu-desktop.webp)

1. If not already open, open OpenPnP by tapping the `Windows` key and typing "openpnp" and hitting enter.

    ![](img/opening-opnp.webp)

2. Home the Lumen with the home icon in the bottom left of the UI.

    ![](img/home-machine.webp)

3. As part of homing, the machine will find the homing fiducial. The screen should look similar to below.

    ![](img/finding-homing-fid.webp)

4. The machine will also perform a nozzle tip calibration. The screen should look similar to below.

    ![](img/nozzle-tip-cal.webp)

5. Click the `PLAY` icon along the top button bar.

    ![](img/run-job.webp)

6. Hit `Yes` to the reset placements popup.

    ![](img/reset-placements.webp)

7. The machine will perform a fiducial check. It will scan the fiducials on all 8 boards with the top camera, and use their location to get accurate placements. This will take a couple minutes. The screen should look similar to below.

    ![](img/finding-fids.webp)

8. The machine will begin feeding a part with a feeder, pick it with the first nozzle, then feed another part, and pick it with the second nozzle. It will then hold the parts over the bottom camera to calibrate their position, then place them both. It will repeat this process until the job is done.

9. When the job is complete, remove the panels from the machine with the Populo screwdriver.

    ![](img/remove-panels.webp)

## Reflow

1. Inspect the panel for accuracy. Adjust any components necessary to ensure a successful reflow, and correct any calibration that could be causing an alignment error. Ask Stephen for help if you get stuck.

2. Insert the panel into the reflow oven.

    ![](img/reflow-put-in-oven.webp)

3. Press the top button to return to the menu.

    ![](img/reflow-to-menu.webp)
  
4. Make sure the current setting is `Loctite GC10`, then press the top button to run the reflow cycle.

    ![](img/reflow-start.webp)
    ![](img/reflow-starting.webp)

6. Work on another task until the Reflow Master beeps **and** says "REFLOW DONE!".

    ![](img/reflow-to-menu.webp)

7. Using the pliers by the oven, grab the panel and place it in the `NEEDS TEST` tray in the rack.

    ![](img/reflow-to-tray.webp)

8. After cooling, gently break apart the panel.
