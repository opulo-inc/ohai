# Drag Chain Assembly #

This section will guide the reader on how to properly assemble the LumenPNP v4 Drag Chain Assembly.

## QC Harnesses ##

Before assembling the drag chain, QC the individual cable harnesses from the manufacturer.

- Head Harness
    - Labels are all correct
        ![bad label](img/wrong-label.webp)
    - Colors on head side are correct
		![](img/color-labels.webp)
    - `Z MOTOR`, `L MOTOR`, and `R MOTOR` cables have inner conductors swapped on the head side only.
		![](img/inner-swapped.webp)
	- `Z MOTOR`, `L MOTOR`, and `R MOTOR` connectors skips positions 2 and 5 on the head side only.
		![](img/skip-2-5.webp)
    - All crimps are fully loaded
    	![](img/not-seated.webp)
    - No loose conductors/Exposed wire
    	![](img/bad-crimp.webp)
- X Gantry
    - `X MOTOR` connector has inner conductors swapped gantry side only.
		![](img/inner-swapped.webp)
	- `X MOTOR` connector skips positions 2 and 5 on the gantry side only.
		![](img/skip-2-5.webp)
    - Labels are all correct
        ![bad label](img/wrong-label.webp)
    - All crimps are fully loaded
    	![](img/not-seated.webp)
    - No loose conductors/Exposed wire
    	![](img/bad-crimp.webp)

## Prepare `cable-splay` ##

- Insert 2x `M5-square-nut` into `cable-splay`
	- Glue is not required even if the fit is loose

	![alt text](img/insert-nuts.webp)

## Assemble Drag Chain ##

1. Insert `cable-splay` into `bij-jig` after 2x `M5-square-nut` are inserted

    ![](img/0.webp)

2. Place `34-link-chain` and `30-link-chain` in `drag-chain-jig` with the flat side resting on the red area of the jig

    ![](img/1.webp)

3. Screw the chains in place

    ![](img/2.webp)

4. Pop open the drag chain tabs with a screwdriver

    ![](img/4.webp)

5. Open all the tabs to make assembly easier

    ![](img/5.webp)

6. Insert `x-harness-cable` into `drag-chain-jig`

    ![](img/7.webp)

	- Ensure that the end photographed below is on the left side of the jig

	    ![](img/6.webp)

7. Insert `top-camera-cable` and feed through `drag-chain-jig`

    ![](img/9.webp)

8. Feed `top-camera-cable` around this piece of `drag-chain-jig` as shown below and pull taut

    ![](img/10.webp)

9. Take `pneumatic-tubing` (one of each color) and insert into the adapters on `drag-chain-jig`

    ![](img/8.webp)

10. Feed through `drag-chain-jig` and pull taut. Ensure the two `pneumatic-tubing` tubes don't cross over each other when feeding around `drag-chain-jig`

    ![](img/13.webp)

11. Insert `pneumatic-tubing` in opposite order on the bottom end of `drag-chain-jig`

    ![](img/15.webp)

12. Prepare `head-harness` and ensure that mobo side of `head-harness` has proper spacing. Inspect the cables for any loose crimps, reworking as needed, before continuing

    ![](img/17.webp)

13. Pull `head-harness` taut

    ![](img/18.webp)

14. With the thinner cable facing you, feed `head-harness` through `drag-chain-jig` until the first ring of tape on the toolhead side of `head-harness` is at the beginning of `34-link-chain`

    ![](img/19.webp)
    ![](img/20.webp)

15. Pull `head-harness` all the way through and ensure the cable is taut

    ![](img/21.webp)

16. Close all of the tabs on `34-link-chain` and `30-link-chain`

    ![](img/22.webp)

17. Use `presser-tool` to secure the tabs

    ![](img/23.webp)

18. Disconnect `pneumatic-tubing` and the usb side of `top-head-cam`. 

    ![](img/25.webp)

19. Unscrew `34-link-chain` and `30-link-chain` from `drag-chain-jig`

    ![](img/26.webp)

20. Remove `34-link-chain` from `drag-chain-jig` first. Bring it to the bottom side of `30-link-chain` while keeping it face up

    ![](img/27.webp)

21. Remove `30-link-chain` from `drag-chain-jig`. Flip both chains upside down in preperation for placement into the `bij-jig`

    ![](img/28.webp)

22. Insert both chains into `bij-jig`

    ![](img/29.webp)

23. Secure chains into `bij-jig` with `m5x16-flat-head`. Use high torque

    ![](img/30.webp)

24. Raise the rail attached to `bij-jig` and insert `pneumatic-tubing` into color-coded slots

    ![](img/32.webp)

25. Zip tie the tubing and cables into the grooves of `cable-splay`

    ![](img/34.webp)

26. Feed `head-harness` cables underneath the cables zip tied to `cable-splay`

    ![](img/35.webp)

27. Seperate `top-light-cable` from `z-limit-cables`

    ![](img/36.webp)

28. Pull `top-light-cable` through to line marked on the back side of `bij-jig`

    ![](img/37.webp)
	![](img/38.webp)


29. Do the same for `top-camera-cable`

    ![](img/39.webp)

30. Zip tie `top-light-cable` and `top-camera-cable` in place

    ![](img/40.webp)

31. Pull `head-harness` cables taut. The cables should reach to or beyond the sticker on `bij-jig`

    ![](img/41.webp)
	![](img/42.webp)
	![](img/43.webp)

32. Bundle all cables and tubing together and place a rubber band to keep them together

    ![](img/44.webp)

33. Do the same for the cables at the top, making sure not to bend `pneumatic-tubing`

    ![](img/45.webp)

## OQC Checks ##

* Inspect the *cable-splay* side of `drag-chain` and confirm the following cables are present and installed in the correct direction

	*  `LM` cable: 6-pin connector with a <span style="background-color:red">**red**</span>`LM` label
	*  `RM` cable: 6-pin connector with a <span style="background-color:blue">**blue**</span> `RM` label

* Confirm the following vacuum tubes are present at both ends:
	*  	<span style="background-color:red">**Red**</span> `4mm-pneumatic-tubing`
	*  	<span style="background-color:blue">**Blue**</span> `4mm-pneumatic-tubing`

* Confirm no vacuum tubes are pinched closed by the rubber banding
* Confirm 3x `zip-tie` used in `cable-splay` are trimmed flush and present
* Confirm presence of `top-camera-cable`
* Confirm presence of `x-harness` and double check that `x-harness` has the correct orientation

	![alt text](img/x-harness-qc.webp)

!!!success "If all checks pass, place the completed `drag-chain` into a yellow `NEEDS QC` bin found on the pack-out shelf while it awaits review"
