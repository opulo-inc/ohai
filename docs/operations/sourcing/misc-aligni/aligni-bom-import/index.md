## Purpose

The goal of this document is to outline a workflow for importing an entire BOM into Aligni Assembly with the minimum amount of manual data entry.

## Definitions

* Assembly

    * Assembly-level parts are typically classified as an Assembly or PCA part type
    * An assembly can also be any part that has child items added to the BOM

---
## Manage Manufactuers and Vendors

* The first step is to make sure the vendors and manufacturers relevant to the BOM have been created and associated together. Follow the steps below to achieve this:

    ??? note "Refresher: Create Suppliers"
        1. Go to the `Suppliers` tab of Aligni by clicking on the icon highlighted in the image below

            ![][image1]

            !!! info "Once Aligni has forwarded you to the Suppliers page, you can view an alphabetically sorted list of all our previously entered suppliers."

        2. Within the Suppliers page, proceed with creating a new supplier entry

            ![][image8]

            * Click on the `(+) Manufacturer` icon to create new manufacturers  
            * Click on the `(+) Vendor` icon to create new vendors  
            * Aligni will forward you to the Details page for the given supplier  
            * Enter all required information (as much known as possible)  
            * Click `Create` when you are finished

    ??? note "Refresher: Associate Vendors and Manufacturers"
        Associate vendors and manufacturers together so that Aligni knows that a given vendor is approved by us to distribute components made by any given manufacturer.

        Steps:

        1. Go to the Suppliers tab of Aligni and select the Manufacturer you wish to create a vendor association with

        2. Navigate to the `Distribution` section of the Manufacturer page

            ![][image3]
            ![][image22]

        3. Click on the `Edit Distribution` icon and wait for the `Select Vendors` pop-up window to appear
              1. Within the `Select Vendors` pop-up window, check all vendors capable of distributing for the relevant manufacturer
              2. Click `Save Distribution` when you are finished

            ![][image4]

        4. Confirm that the selected vendors are now listed in the Distribution details pane of the Manufacturer entry

            ![][image17]

* Repeat these steps until you have completed listings and defined distribution channels for all the components of the BOM you wish to import.

---

## Create Parts

1. Manually create any top-level Assembly part in Aligni that you intend to upload a BOM for.

2. Import data about the BOM into a copy of [ASM-####-##-Part-List-Template](https://docs.google.com/spreadsheets/u/0/?ftv=1&tgif=d)

    Notes about the template:

    * Columns colored **yellow** are relevant to the assembly BOM details
    * Columns colored **white** are relevant to information about the particular part
    * Columns colored **red** should be left blank for Aligni to auto-fill
    * Columns colored **light blue** are optional, but best filled in if possible
    * Column A denotes “Level,” which defines the parent-child relationship of a BOM:

      * Level-0 → top-level assembly and PCA type items

        * Only 1 component at this level per BOM
      * Level-1 → unique components that go into a Level-0 assembly
      * Level-2+ → child items of Level-1 components if further depth is required

    !!!note "A sample CSV is available [here](https://docs.google.com/spreadsheets/u/0/d/1II3TcQo-Ti0NBAoFJ9SHTzenCsp3R-xUhtaHW8CJ1XY/edit) for reference"

          ![][image12]

3. Fill out as much information as possible:

    * Use ROW2 to enter information about the parent (level-0) component of the BOM
        * If you leave the MFG PN field blank, Aligni will attempt to auto-generate one
        * Best practice is to assign even a placeholder PN
        * MFG PN values must be unique!
    * **Leave the `Part Number` field blank if you want Aligni to auto-generate it**

4. Download the spreadsheet as a CSV file, using the convention:

      * `ASM-####-##-Part-List` where `#`s are replaced with the relevant numbers

      * If an Opulo MFG PN is not defined yet, use the informal colloquial name

5. Upload the CSV file to Aligni:

      * Navigate to the `Parts` pane → `[Import New Parts From CSV]`

        ![][image21]
        ![][image6]
        ![][image24]

    !!!info "Release parts after import” is optional"
         * Disabled = Lucy's suggestion (but may require manual release of many parts)
         * Enable `Ignore Pre-existing Parts` for best practice

   * Choose file → Select CSV → Click `Open`

     ![][image7]

6. Identify CSV columns and add custom parameters:

      * Enable “Ignore first row from CSV”

        ![][image16]

      * Map CSV fields to Aligni parameters

        ![][image27]

          * It’s OK to leave unmapped fields blank

      * Click `Continue to Next Step` when done

7. Review processed CSV Data and create parts:

      * The utility will create any required Part Types, Manufacturers, or Use-As-Units not already created
      * Items created appear in **green** in preview table
      * If everything looks correct, click `Create Parts`

     ![][image15]

---

## Import BOM to Assembly

!!!warning "Before proceeding, note:"
      * Part lists can only be edited in Draft mode
      * All parts in the BOM must already exist in the database

1. Choose a CSV file to import for the Assembly BOM:

      * Navigate to `BOM (Parts List)` tab of Assembly

         ![][image5]

      * Click `Import CSV`

        ![][image20]

      * Select CSV file → Click `Open`

2. Assign attributes to CSV columns:

      * Manufacturer’s P/N → Column 4

      * QUANTITY → Column 12

      * BUILD SEQUENCE → Column 16 (leave unmapped if null values)

      * DESIGNATOR → Column 25

      * COMMENT → Column 24

      * NO LOAD → Column 23

     ![][image25]

3. Review preview table → Uncheck Level-0 component

     ![][image19]

4. Uncheck any unintended parts

    ![][image13]

5. Click `Match Parts & Move to Step 3`

6. Confirm part matches:

      * Preview table will list results
      * Errors are shown line-by-line
        * If issues exist, you may need to revise the CSV and start again

      ![][image23]

      * If all rows match successfully, proceed

7. Choose whether to:

      * **Clear existing partlist before importing** (best practice)
      * **Add to working partlist** (useful for staged imports)

    ![][image2]

8. Click **Import Parts** to complete

    ![][image9]

9. Confirm imported BOM:

      * Level-0 Assembly BOM should now contain all components

    ![][image14]

---

🎉 You are now done! 🎉

[image1]: img/img_001.webp
[image2]: img/img_002.webp
[image3]: img/img_003.webp
[image4]: img/img_004.webp
[image5]: img/img_005.webp
[image6]: img/img_006.webp
[image7]: img/img_007.webp
[image8]: img/img_008.webp
[image9]: img/img_009.webp
[image10]: img/img_010.webp
[image11]: img/img_011.webp
[image12]: img/img_012.webp
[image13]: img/img_013.webp
[image14]: img/img_014.webp
[image15]: img/img_015.webp
[image16]: img/img_016.webp
[image17]: img/img_017.webp
[image18]: img/img_018.webp
[image19]: img/img_019.webp
[image20]: img/img_020.webp
[image21]: img/img_021.webp
[image22]: img/img_022.webp
[image23]: img/img_023.webp
[image24]: img/img_024.webp
[image25]: img/img_025.webp
[image26]: img/img_026.webp
[image27]: img/img_027.webp
