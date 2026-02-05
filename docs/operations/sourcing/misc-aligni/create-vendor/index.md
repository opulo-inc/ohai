# Creating and Associating Vendors, Manufacturers, and Contacts

#### Purpose

This purpose of this SOP is to document the process of creating Vendors, Manufacturers, and Contacts in Aligni. 

This SOP will also demonstrate how to properly associate these three types of entities to one another in order to properly conduct supply chain operations here at Opulo.

-----

#### Definitions

**What is a Manufacturer?**

* Manufacturers are business entities that produce goods found within our supply chain
* Sometimes we (Opulo) are the Manufacturer of a given part — for example assemblies or 3D-printed items made in-house

**What is a Vendor?**

* Vendors are business entities that sell goods found within our supply chain
* If a component is both manufactured and sold to us by a single business entity, the business would be listed as both a vendor and manufacturer

    * An association would then be created between the two listings, which will be explained in more detail later on

**What is a Contact?**

* Contacts are individuals or teams listed in Aligni that are associated with vendors and/or manufactuers
* Contact listings in Aligni contain the details required to contact the vendor/manufactuer for RFQ (request for quotes) and PO (purchase order) issuance
* These listings also contain enough contact info to manually message a given entity outside of Aligni

-----

#### Create a Manufacturer

2. Navigate to <https://opulo.aligni.com/relationships> to access the Relationship Manager section of Aligni

2. Click "+ Manufacturer"

    ![](img/01.webp)

1. Fill out the following information:

     - Name:
         - Enter the complete legal name of the manufacturer's business entity
     - SHORT NAME:
         - Enter a clear abbreviation for the manufacturer
     - WEBSITE:
         - Use the top-level URL of the manufacturer's website
     - Adresses:
         - If known, enter the primary address the manufacturer does business from
         - It's OK to list additional addresses – provided there's utility in doing so
     - Phone Number(s):
         - Add any phone number(s) for the manufacturer that you can easily find

    ![](img/02.webp)

    ![](img/03.webp)

2. Once all information has been entered, click "Create" in the bottom right section of the screen to create the manufacturer

    ![](img/04.webp)

-----

#### Create a Vendor

6. Navigate to <https://opulo.aligni.com/relationships> to access the Relationship Manager section of Aligni

6. Click "+ Vendor"

      ![](img/05.webp)

1. Fill out the following information:

     - SHORT NAME:
         - Enter a clear abbreviation for the Vendor
     - WEBSITE:
         - Use the top-level URL of the website used for purchasing parts from the vendor
     - ACCOUNT NUMBER:
         - Only enter one if known
     - CURRENCY:
         - Leave as USD (unless you know otherwise)
     - DEFAULT PAYMENT TERMS:
         - CIA
     - DEFAULT DELIVERY TERMS:
         - Ship via Shipping Service Provider
             - Replace Shipping Service Provider with the usual shipping service we use for the vendor
             - The Shipping Service can be set to something other than this default value when a PO is created
     - DEFAULT INCOTERMS:
           - DDU (unless you know otherwise)
     - DEFAULT SHIP-TO LOCATION:
           - Opulo HQ
     - VENDOR PORTAL:
           - Access Enabled
     - Add any phone numbers for the vendor that you can easily find

    ![](img/06.webp)

2. Once all information has been entered, click "Create" in the bottom right section of the screen to create the Vendor

    ![](img/07.webp)

1. Confirm the accuracy of the entered information

    ![](img/08.webp)

------

#### Associate Manufacturers with a Vendor

10. Return to the Manufacturer's listing in Aligni

    ![](img/09.webp)

1.  Click "Distribution"

    [](img/10.webp)

1.  Click "Edit Distribution"

    ![](img/11.webp)

1. Use the "Search..." field to select each vendor the manufacturer should be associated with
     - A manufacturer might have their products purchasable from multiple vendors
     - This is especially true if the manufacturer is one of our many "Generic Factory" sources

    ![](img/12.webp)

1.  Click "Save Distribution" when finished

    ![](img/13.webp)

1.  Confirm all required manufacturer distribution associations have been created

    ![](img/14.webp)

-----

#### Create a Contact

16. Navigate to <https://opulo.aligni.com/relationships> to access the Relationship Manager section of Aligni

    ![](img/15.webp)

1.  Click "+Contact"

    ![](img/16.webp)

1.  Fill out the "Basic Information" section

    ![](img/17.webp)

    ![](img/18.webp)

1.  Click "Create"

    ![](img/19.webp)

-----

#### Associate Contact with a Vendor

21. To associate a contact with a vendor, perform the following steps:

    - Return to the Relationship Manager
    - Search for the Vendor that the newly created Contact should associated to
    - Click on the Vendor's name to be taken to their page in Aligni

    ![](img/20.webp)

1.  Navigate to the Vendor page's "Contacts" tab

    ![](img/21.webp)

1.  Click "Edit Contacts"

    ![](img/22.webp)

1.  Select the appropriate Contact before clicking "Save Contacts"

    ![](img/23.webp)

    ![](img/24.webp)

------

#### Associate Contact to a Manufacturer [Optional]

!!!info "This is worth doing when a manufacturer and a vendor are actually the same entity"

26. Navigate to the "Manufacturer Associations" tab on the newly created Contact listing

    ![](img/25.webp)

1.  Click "Edit Manufacturers"

    ![](img/26.webp)

1.  Select the relevant Manufacturer before clicking "Save Manufacturers"

    ![](img/27.webp)

!!!success "Everything is finished once the Manufacturer Association is listed!"

    ![](img/28.webp)
