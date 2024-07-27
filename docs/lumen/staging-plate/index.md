# Staging Plate

## Subassembly Prep

### Install hardware into 3D printed components

* Use an arbor press to insert the given quantities of `M3-hex-nut` into the following parts:
  * 4x for `bottom-camera mount`
  * 3x for 3x `peek-cable-clamp`

    !!! note
        Be sure to change the arbor press tip for the different prints as needed.

	<img src="img/image42.png" width="60%"/>
* * *


### Removing punch-out from `PCB-0003`

* Remove the punch-out from center of `PCB-0003` with flush cutters

 <img src="img/image27.png" width="60%"/>
 
 <img src="img/image19.png" width="60%"/>

* Clean up hole with a razor blade after punch-out has been removed

 <img src="img/image29.png" width="60%"/>

* Clean both sides of `PCB-0003` with an IPA-soaked shop rag

***

### Focus the bottom-camera

Use `bottom-camera-focus-jig` to pre-focus `bottom-camera`

* Loosen the set screw on the side of the lens, this will let the lens focal-point be adjusted
  * Be careful not to loosen it too much or the screw may fall out and get lost!

   <img src="img/image50.JPG" width="60%"/>

* Remove the lens cap from bottom-camera
* Rotate the camera lens back and forth to loosen any glue
  * Hold the PCB in one hand while twisting the lens body with your other hand
  * Don't be afraid to use a few pounds of force if needed

   <img src="img/image56.jpeg" width="60%"/>
 
* Install the `bottom-camera` fully into the `bottom-camera-focus-jig`
  * Put the JST-side of `bottom-camera` into the jig first
  * Connect the JST-side of the USB cable into the bottom-camera PCB

   <img src="img/image52.JPG" width="60%"/>

* Connect the USB cable on `bottom-camera-focus-jig` to a computer and open its native camera viewing application
  * Use Photobooth if on Mac OSX or Cheese if on Linux
  * Confirm that the camera feed is running in 720p, sometimes it can launch in 360p or 480p
  * Within the camera viewing application, change the selected camera to `PnP Bottom` to view the camera feed of the bottom-camera

  !!! warning "If the listed camera is something other than `PnP Bottom`, the device may either be incorrectly programmed or mixed up with a top-camera module" 
  	
    **Please take this as an opportunity to double-check the device name even if the computer switched to the correct camera feed automatically.**
 
* Rotate the camera lens until the live viewport shows the datum board as focused as possible
  * Before and after lens focusing:
  
   <img src="img/image49.jpg" width="60%"/>
  
* Once the camera is focused, tighten the set screw to lock in the focus adjustment
* Put a blue dot on the camera PCB with a sharpie to denote that the camera has passed testing

  <img src="img/image53.JPG" width="60%"/>

* Remove the `bottom-camera` from the `bottom-camera-focus-jig` and immediately replace the lens cap
* Return the `bottom-camera` to the red esd-safe bag

  <img src="img/image54.JPG" width="60%"/>

***

### Creating bottom-camera-assembly

* Attach `bottom-camera` and `bottom-camera-cover` to `bottom-camera-mount` with 4x `M2.5x8-bolt`

 <img src="img/image2.jpg" width="60%"/>
 <img src="img/image17.jpg" width="60%"/>

* Confirm `bottom-camera`'s JST connector is next to the zip-tie cable strain relief feature, as indicated below:

 <img src="img/image28.jpg" width="60%"/>

* Clean `bottom-light-mount` print by removing any loose stringy plastic with a heat gun and/or razer blade (as needed)
* Install `bottom-ring-light` into `bottom-light-mount`

 <img src="img/image39.jpg" width="60%"/>
 <img src="img/image25.jpg" width="60%"/>
 
***

## Final Assembly

#### Installing bottom-camera-assembly

* Attach `bottom-camera-assembly` onto `staging-plate` with 4x `M3x16-bolt`

 <img src="img/image22.jpg" width="60%"/>

* The JST cable connector found on `bottom-ring-light` should match the orientation shown below when installed - *as close to the Opulo logo as possible and in line with `staging-plate` column 18*

 <img src="img/image5.jpg" width="60%"/>

* The JST cable connector found on `bottom-camera` should match the orientation shown below when installed - *as close to the Opulo logo as possible*

 <img src="img/image6.jpg" width="60%"/>

* * *


***

#### Install datum-board and datum-board-mount

* Use four `M3x16mm-bolt` and 4x `M3-hex-nut` to secure the `datum-board` and `datum-board-mount` to `staging-plate` on the rear of the `bottom-camera`, through holes: B18, A19, A21, B22.
  * Use a 2.5mm hex wrench and a 5.5mm (6mm if 5.5mm is unavailable) socket wrench to tighten these bolts
  * The fisheye calibration pattern should be facing down, and the gold grid lines and fiducial in the center of the Opulo logo facing upwards

   <img src="img/image11.png" width="60%"/>
 
***

#### Attach Machine Serial # Label

* Install a unique Machine Serial # sticker onto the bottom of the `staging-plate`

 <img src="img/image8.png" width="60%"/>
 
 !!!note
  - The `up-light-harness` shown above is installed backwards
  - The `up-light-harness` label should be on the `motherboard` side
  - The side plugged into `bottom-ring-light` should be unlabled

***

#### Performing cable management

* Clamp cables in the locations shown below with 6x `peek-cable-clamps`, 6x `m3-hex-nut`, and 6x `m3x14` bolts

 <img src="img/image20.png" width="60%"/>
 <img src="img/image30.png" width="60%"/>
 <img src="img/image3.png" width="60%"/>

***

### QC Checklist

Run the staging plate assembly through the QC inspection form found here:

[https://docs.google.com/forms/d/e/1FAIpQLSf1HXndxFzhRyJsBtHUMHoJEiU\_ig9z8cUJpGCH4vcM8OR5mQ/viewform](https://www.google.com/url?q=https://docs.google.com/forms/d/e/1FAIpQLSf1HXndxFzhRyJsBtHUMHoJEiU_ig9z8cUJpGCH4vcM8OR5mQ/viewform&sa=D&source=editors&ust=1675029454657858&usg=AOvVaw12puD4NK5Y2xleOU-dRT_L)

<img src="img/image10.png" width="60%"/>

!!! note
    - The QC inspection form will ask you if the bottom-camera was correctly focused with the *orange version* of the `bottom-camera-focus-jig`
  - Use this jig in the same way the blue one is operated, while leaving the camera installed on the staging-plate

   <img src="img/image55.jpg" width="60%"/>   
   
   If the camera is out of focus, remove it from the assembly and repeat [bottom-camera focusing](#focus-the-bottom-camera).

***

### Next Steps

!!!success "After completing QC, perform the following steps"

* Add a `QC PASS` sticker to the `primary-staging-plate`'s `bottom-camera-cover`
 ![](img/staging-plate-qc-sticker.jpg)
* Binder clip the `box-sn-label` to the side of the `primary-staging-plate`
 ![](img/clipped-sn-label.JPG)
* Bring the completed `primary-staging-plate` to the shelf for peer-review and pack-out
