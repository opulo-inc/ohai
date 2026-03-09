# New Releases and Version Control

## Mattermost Playbooks
Project management for new releases will be handled with the Mattermost Playbooks tool. To get started, open Mattermost and click on the menu icon in the top left of the window.

![](img/mm-icon.webp)

Switch from the default `Channels` page to `Playbooks`

![](img/mm_menu.webp)

Here you will find all the available Playbooks to run. You can also create a new Playbook, but Playbooks for new releases of our major products already exist. 

![](img/playbooks.webp)

!!! warning "Please Note"
    Before you can run a specific Playbook, you may have to join it first if you haven't already done so.

Select the Playbook that matches the product that is being updated. For this example, we will proceed as if we are releasing a new version of the LumenPnP, so we will select the `LumenPnP Release` Playbook.

![](img/lumen-pb.webp)

After opening the Playbook, navigate to the `Outline` page. Ensure all tasks listed are still relevant and necessary for release. Once the information is verified, you can run the Playbook. Click `Run` at the top right of the page.

![](img/run-button.webp)

A new window will appear. We will need to replace the placeholder information with accurate information related to our release.

![](img/run-window.webp)

For this example, we will be creating a Playbook for the LumenPnP v4.1.0 release. Replace the placeholder text with the version number you are working with. In this example, we would change the title from `LumenPnP Release (vX.Y.Z)` to `LumenPnP Release (v4.1.0)`. Also make sure to change the version number from `TBD` to `v4.1.0` in `Run Summary`.

![](img/placeholder.webp)

Decide if you want to create a public or private channel that will be linked with the release. Once you've made your selection, click `Start run` at the bottom right of the window.

!!! success "Done!"
    You have successfully ran the Playbook to kick off the release of a new version. Use this Playbook to manage the steps needed for a successful release. You can assign certain actions to people in the organization and check them off as they are completed.

## Creating New Parts in Aligni

New releases usually come with parts that need to be added or updated in Aligni. For detailed instructions on adding and editing parts in Aligni, see [Aligni Misc](/operations/sourcing/misc-aligni/create-part/).

## Slicing New Prints for Print Farm

Any updated or new parts will need to be sliced for both P1P and P1S printers in our farm. 

### Updating Existing Prints 

Get new source files for the new release from the engineering team. Open a new Bambu Studio file and import the `.step` file by going to `File > Import > Import 3MF/STL/STEP/OBJ/AMF...` or use the `⌘ + I` keyboard shortcut.

![](img/import.webp)

For this example, we will import a new version of `front-left-leg` that was updated for v4.1.0 of the LumenPnP.

![](img/front-left-leg-import.webp)

The default import settings do not need to be adjusted. Click `Okay` to import. The object should appear on the print bed.

![](img/obj-imported.webp)

Now, we will open the sliced file of this item from the previous release to reference. This should be located in the shared `OpuloEngineering` folder in [Google Drive](https://drive.google.com/drive/folders/192uedSnuzkUN0lld6c-fzTRW7Omv1ipp?usp=drive_link). The path to the print files is `Shared drives > OpuloEngineering > manufacturing > production > 3D Printing > Print Farm Files`. Select the product that your part is for and find the `slice` folder to open the part's existing file. 

![]()

We will use the previous versions' file as a reference as to how the print should be laid out on the bed as well as where to add support (if necessary). Make sure the part is laying on the same face as the previous versions' file that we are using for reference.

!!! warning "Please Note"
    You should handle creating support before making copies of the object and laying it out on the bed. This way, the support is also copied over instead of having to add support to each copy manually.

After opening the file, check to see if this print needs support. Change the color scheme to `Line Type` in the `Slicing Result` window. This will allow you to easily see existing support.

![](img/line-type.webp)

Here we can see that there is support in the open cavity of the part (indicated in green) and there are brim ears around the print to help with bed adhesion (indicated in blue). We want to mirror the support shown here onto our new version file. Click the object and then click `Supports Painting` in the menu (or use the keyboard shortcut `L`).

![](img/support-1.webp)

Paint where support should be added. It will turn blue to indicate this area will be supported. You can also right click to paint areas red, which explicitly tells the program to not add support in that area.

![](img/support-2.webp)

Once support is added, make sure support is enabled in the settings. Check the `Enable support` box and set `Type` to `normal(manual)`.

![](img/enable-support.webp)

You can now make copies and lay out your new prints in the same position that the previous version was laid out.

![](img/layout.webp)

Once the bed is properly arranged and support is added, save the file and prep for slicing. Pick either the P1P printer or the P1S printer. We will need to slice twice for each printer. Set the filament to `PolyLite PLA` and use the `0.20mm Strength` preset. Then, select the proper bed for this print. Check the Kanban Cards to see which bed this should be printed on. Also double check that support is enabled, as it is off by default and may switch back to off if you change the preset. 

![](img/settings.webp)

We will slice the print for the P1P printer first. With the correct printer selected, click `Slice plate` at the top right of the screen. 

![](img/slice-plate.webp)

Change the slicing result to `Line Type` so it's easier to see support. Evaluate your print and ensure support is where it needs to be and there are no issues or collisions. 

![](img/eval.webp)

Once all looks good, we will export the sliced plate to upload onto the farm computer. `File > Export > Export plate sliced file` or `⌘ + G` to export. Save to `Shared drives > OpuloEngineering > manufacturing > production > 3D Printing > Print Farm Files`. Since we are exporting a P1P file here, we would save this example in `LumenPnP v4.1.0 > slice > P1P`.

![](img/export.webp)

Now we will repeat the process for the P1S export. Change the printer to `P1S` in the left panel. Make sure the settings remain the same and support is still enabled. 

![](img/p1s.webp)

Follow the same steps above to slice, evaluate, and export the print. Make sure this export goes into the `P1S` folder.

### Creating Files for New Prints

For new parts, we will have to create new slice files. Since there is no reference you can use, discuss with the engineering team what face the new part should be printed on, what bed it should be printed on, etc. Evaluate the profile of the new part add support for any overhangs. 

Then, follow the SOP for updating existing prints to slice, evaluate, and export the print. Make sure to export for both P1S and P1P. Alert the production team in Mattermost that new parts are being added and quality should be checked carefully for the first few prints.

## Upload New Files Onto Farm Computer

We will now take our new files and upload them to Bambu Farm Manager for printing. For a full guide on how to upload files onto Bambu Farm Manager, please see the "Using Bambu Farm Manager" section of the [Farm Management](/operations/print-farm/farm-management/) page.

It is important to delete old versions off of the farm computer to ensure the most recent version is being printed. Deleting files on Bambu Farm Manager does not delete the files anywhere else, so it is safe to delete these files. 

!!! success "Done!"
    You have successfully sliced new files, uploaded them to the farm computer, and deleted old files out of the Bambu Farm Management software. Notify the production team that there are new files and to keep an eye on how the first few prints turn out.

## Create New Kanban Bins

If you have any brand new parts, you must create new Kanban bins. This will ensure that the production team can track inventory for these prints. 