# Staging Plate


### 4.2.0 Update

!!! note 
    This section highlights the changes in 4.2.0 — the remaining sections remain unchanged until further maintenance to OHAI. If information in later sections contradict what is in this section, please consider this section as accurate.

#### Fid Board Sub-assembly
1. Use press to install 2x `cal-fid`
    ![](img/press-cal-fid.webp)

2. Stack 2x `cal-fid-token` into the slot with copper side up
    ![](img/token-stack.webp)

3. Apply `polymer-tape` to ensure tokens do not fall out of the slot
    ![](img/tape-tokens.webp)

#### 4.2.0 Staging Plate Assembly Instructions

1. Secure `cal-fid-mount` to `staging-plate-offcenter` with 2x `m4x10mm-socket-head`
    ![](img/secure-fid.webp)

2. Secure `discard-bin-mount` with 2x `m4x10mm-socket-head`
    ![](img/secure-discard-bin.webp)

3. Add `discard-bin` into `discard-bin-mount`
    ![](img/insert-bin-1.webp)
    ![](img/insert-bin-2.webp)

4. Use `polymer-tape` to secure `discard-bin` to `staging-plate-offcenter`
    ![](img/tape-bin.webp)

5. Insert `bottom-camera` into `bottom-camera-mount`. Ensure the position matches the image below
    ![](img/insert-camera.webp)

6. Secure `bottom-camera` to `bottom-camera-mount` with 4x `m2.5x8mm-socket-head`
    ![](img/secure-camera.webp)

7. Insert `bottom-camera-cable` and loop through open cavity in `bottom-camera-mount`
    ![](img/cable-loop.webp)

8. Insert `zip-tie` through channel in `bottom-camera-mount`
    ![](img/thread-zip-tie.webp)

9. Tighten and ensure the head of `zip-tie` is centered in the cavity. Snip the excess
    ![](img/centered-zip-tie.webp)
    ![](img/snip-zip-tie.webp)

10. Add `ring-light` to `bottom-light-mount`
    ![](img/add-ring-light.webp)

11. Attach other end of `bottom-camera-cable` that is labeled `bottom-light-sp` to `ring-light`
    ![](img/plug-in-ring-light.webp)

12. Position `bottom-camera` assembly and `ring-light` assembly as shown in the image and bring the two assemblies together
    ![](img/sandwich-1.webp)
    ![](img/sandwich-2.webp)

13. Ensure `bottom-camera-cable` goes through the channel in `bottom-light-mount`
    ![](img/cable-channel.webp)

14. Place `bottom-vision-cover` over top of the assembly. Ensure the cables go into the cutouts
    ![](img/bottom-vision-cover-1.webp)
    ![](img/bottom-vision-cover-2.webp)

15. Flip `staging-plate` and secure `bottom-vision-cover` assembly with 4x `m4x18mm-socket-head`. Ensure the location matches the image below
    ![](img/secure-to-plate.webp)

16. Install `bottom-vision-cable-clamp` and ensure cables go into the channel properly 
    ![](img/cable-clamp-1.webp)
    ![](img/cable-clamp-2.webp)

17. Secure `bottom-vision-cable-clamp` with 2x `m4x10-socket-head`
    ![](img/cable-clamp-3.webp)

18. Install 2x `peek-cable-clamp`. Install one in the hole beside `bottom-vision-cover` skip 6 holes and install the second cable clamp in the 7th hole as shown in the image
    ![](img/peek-cable-clamp.webp)

!!! success "All done!"
    You have successfully assembled a 4.2 staging plate. The guide below has yet to be updated for 4.2 — if any information contridicts this section, consider the 4.2 section accurate.


### Install hardware into 3D printed components

* Use an arbor press to insert the given quantities of `M3-hex-nut` into the following parts:
  * 4x for `bottom-camera-mount`
  * 3x for 3x `peek-cable-clamp`

    !!! note
        Be sure to change the arbor press tip for the different prints as needed.

	<img src="img/insert-m3-hex.webp" width="60%"/>
    <img src="img/insert-m3-hex-2.webp" width="60%"/>

### Removing punch-out from `PCB-0003`

* Remove the punch-out from center of `PCB-0003` with flush cutters

    <img src="img/image27.webp" width="60%"/>

    <img src="img/image19.webp" width="60%"/>

* Clean up hole with a deburring tool after punch-out has been removed

    <img src="img/deburring-tool.webp" width="60%"/>

* Clean both sides of `PCB-0003` with an IPA-soaked shop rag

### Focus the bottom-camera

- Thread the `bottom-camera-cable` through `bottom-camera-cover` and connect it

    <img src="img/camera-cable.webp" width="60%"/>

* Remove the lens cap from `bottom-camera`

* Use `bottom-camera-focus-jig` to pre-focus `bottom-camera`

  * Turn on the light for the jig and attach `bottom-camera`

    <img src="img/focus-1.webp" width="60%"/>

* Connect the USB cable on `bottom-camera-focus-jig` to a computer and open its native camera viewing application
  * Use Photobooth if on Mac OSX or Cheese if on Linux
  * Confirm that the camera feed is running in 720p, sometimes it can launch in 360p or 480p
  * Within the camera viewing application, change the selected camera to `PnP Bottom` to view the camera feed of the bottom-camera

!!!warning "If the listed camera is something other than `PnP Bottom`, the device may either be incorrectly programmed or mixed up with a `top-camera`"
    Please take this as an opportunity to double-check the device name even if the computer switched to the correct camera feed automatically.

* Rotate the camera lens until the live viewport shows the datum board as focused as possible

    <img src="img/focus-2.webp" width="60%"/>

### Creating bottom-camera-assembly

* Attach `bottom-camera` and `bottom-camera-cover` to `bottom-camera-mount` with 4x `M2.5x8-bolt`

    <img src="img/jig-2.webp" width="60%"/>

* Confirm `bottom-camera`'s JST connector is in the correct orientation as indicated below:

    <img src="img/jig.webp" width="60%"/>

* Clean `bottom-light-mount` print by removing any loose stringy plastic with a heat gun and/or razer blade (as needed)
* Install `bottom-ring-light` into `bottom-light-mount`

    <img src="img/image39.webp" width="60%"/>
    <img src="img/image25.webp" width="60%"/>

### Final Assembly

#### Installing bottom-camera-assembly

It is recommended to wear gloves when handling the `staging-plate`.

* Attach `bottom-camera-assembly` onto `staging-plate` with 4x `M3x16-bolt`

    <img src="img/image22.webp" width="60%"/>

* The JST cable connector found on `bottom-ring-light` should match the orientation shown below when installed - *as close to the Opulo logo as possible and in line with `staging-plate` column 18*

    <img src="img/vertical-2.webp" width="60%"/>

* The JST cable connector found on `bottom-camera` should match the orientation shown below when installed - *as close to the Opulo logo as possible*

    <img src="img/vertical-3.webp" width="60%"/>

#### Install datum-board and datum-board-mount

* Use four `M3x16mm-bolt` and 4x `M3-hex-nut` to secure the `datum-board` and `datum-board-mount` to `staging-plate` on the rear of the `bottom-camera`, through holes: B18, A19, A21, B22.

<img src="img/vertical-4.webp" width="60%"/>


  * Use a 2.5mm hex wrench and a 5.5mm (6mm if 5.5mm is unavailable) socket wrench to tighten these bolts
  * The fisheye calibration pattern should be facing down, and the gold grid lines and fiducial in the center of the Opulo logo facing upwards

    ![alt text](img/IMG_2021.webp)

* Plug `bottom-light-harness` into `bottom-ring-light`
* Plug `bottom-camera-harness` into `bottom-camera` before securing cable to `bottom-camera-mount` with a `zip-tie`

    ![alt text](img/IMG_2018.webp)

#### Install secondary fiducial

* Use two `M3x10-hex-head` to attach `secondary-fiducial-bracket` to `staging-plate`. Make sure the closed portion of the. bracket is facing the `ring-light`.

    <img src="img/secondary-fid.webp" width="60%"/>    

* Fasten `secondary-fiducial-bracket` to `staging-plate` with two `m3-hex-nut`. 

    <img src="img/secondary-fid-2.webp" width="60%"/>

#### Performing cable management

* Clamp cables in the locations shown below with 3x `peek-cable-clamp`, 3x `m3-hex-nut`, and 3x `m3x14` bolts

    ![alt text](img/IMG_2020.webp)
    ![alt text](img/IMG_2019.webp)

* After securing the cables, tie them up with the twist tie from `bottom-camera-cable`

    ![alt text](img/IMG_2017.webp)