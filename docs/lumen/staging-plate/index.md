# Staging Plate

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

* Plug `bottom-light-harness` into `bottom-ring-light`
* Plug `bottom-camera-harness` into `bottom-camera` before securing cable to `bottom-camera-mount` with a `zip-tie`

    ![alt text](img/IMG_2018.webp)

#### Install datum-board and datum-board-mount

* Use four `M3x16mm-bolt` and 4x `M3-hex-nut` to secure the `datum-board` and `datum-board-mount` to `staging-plate` on the rear of the `bottom-camera`, through holes: B18, A19, A21, B22.

<img src="img/vertical-4.webp" width="60%"/>


  * Use a 2.5mm hex wrench and a 5.5mm (6mm if 5.5mm is unavailable) socket wrench to tighten these bolts
  * The fisheye calibration pattern should be facing down, and the gold grid lines and fiducial in the center of the Opulo logo facing upwards

    ![alt text](img/IMG_2021.webp)

#### Install secondary fiducial

* Use two `M3x10-hex-head` to attach `secondary-fiducial-bracket` to `staging-plate`. Make sure the closed portion of the. bracket is facing the `ring-light`.

    <img src="img/secondary-fid.webp" width="60%"/>    

* Fasten `secondary-fiducial-bracket` to `staging-plate` with two `m3-hex-nut`. 

    <img src="img/secondary-fid-2.webp" width="60%"/>

#### Performing cable management

* Clamp cables in the locations shown below with 3x `peek-cable-clamp`, 3x `m3-hex-nut`, and 3x `m3x14` bolts

    ![alt text](img/IMG_2020.webp)
    ![alt text](img/IMG_2019.webp)

* After securing the cables, tie them up with a `rubber-band`

    ![alt text](img/IMG_2017.webp)