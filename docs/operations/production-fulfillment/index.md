# WHEN BEHIND - Opulo Order Fulfillment/Production

## Deciding What to Fulfill

- Review Redash dashboard to see which orders need to be shipped that week based off the `last_acceptable_ship_week` column.

	![](redash.webp)

## Create ShipStation Batch

1. Go to ShipStation and create a batch for the orders that fall within the given `Batch WK#` you wish to fulfill.
2. **MAKE SURE** to check the `Awaiting Payment` tab for any orders with Net terms. Orders that show up in Redash but not in `Awaiting Shipment` are likely there.
2. Name the ShipStation batch to `2026-06`, where `06` is replaced with the batch's given week number for the year.

## Preparing Shipping Labels for Purchase

3. Review each ShipStation order in the batch for correctness:
   - Selct the correct package size/set, review declared values, and ensure shipping methods are sensible.
   - **Box Weight Check:**
       - After loading a box size preset **double check the weight field.**
       - If the weight has changed unexpectedly, **edit the weights back to the previously displayed total weight** to ensure accurate shipping costs.
   - **Avoid overpaying for shipping:** Do not select a service that costs vastly more than what the customer paid.
   - **Upgrade where possible:** If the customer’s paid shipping rate allows, consider upgrading their shipping service for faster delivery without exceeding their payment amount.
   - **FedEx consideration:** If shipping with another carrier would lose $100+ compared to FedEx, consider switching to FedEx to reduce the loss.
   - **Tax ID Handling:**
       - Check the order notes for the customer’s **Tax ID** and add it to the `Recipient Tax Identification` field in ShipStation.
       - If the Tax ID appears in **Line 3 (or elsewhere)** of the shipping address, **remove it from the address** and paste it into the `Recipient Tax Identification` field instead.
   - **For Canada-bound shipments enter the following info:**
       - Customs Declarations → “ECCN” field: `EAR99`
           - This should be there automatically
       - Customs Declarations → “ITN / AES Exemption” field: `NOEEI 30.36`
           - Source: [https://www.ecfr.gov/current/title-15/subtitle-B/chapter-I/part-30/subpart-D
](https://www.ecfr.gov/current/title-15/subtitle-B/chapter-I/part-30/subpart-D)

## Prepare the Order-Packing-Checklist

- Prepare an `Order-Packing-Checklist` for the week's fulfillment using the [Google Slides template](https://docs.google.com/presentation/d/1bjngnZyvqVTuc3WafVRS6TTGYHAocfyJrHuGKA1xy9k/edit?usp=sharing)

	- Make a copy of the most recent slide and replace the image with the screenshot of the ShipStation batch you are working with
	- The checklist printout should look like the following image:

		![](Order-Packing-Checklist.webp)

3. Fill in the time and date for any scheduled pickup, per carrier

  	 - Write "Drop off" for any carrier that we will bring the packages to ourselves

2. Print out the week's checklist when ready

## Purchase the labels
 - Some notes:
     - When you purchase the labels, select the correct "Ship On" date so that you can later schedule a pickup for this day

 - Cautions:

	!!!warning "**50 Character Line Limit:**"
		If an error occurs during label creation, it may be because a line in the shipping address exceeds 50 characters. If this happens:
		- Abbreviate words or
		- Split the content into an additional line to stay within the limit.



## Create a Pickup

5. Set the `Pickup Date` for the required shipping carriers

  - Customers can currently pick between UPS, USPS, and DHL at checkout so multiple pickups may be required
  - Note that DHL pickups are done in Shopify, UPS and USPS in ShipStation

6. Print out all the shipping labels for the week on `4x6 Label Paper` with the Dymo 4XL Label Printer

## Handling the Shipping Paperwork

- Separate the shipping labels by order number, leaving related shipping label(s) and packing slips connected

	- Domestic shipping labels will have 2 pages per order, these are:
		- Shipping Label
		- Packaging Slip

	- International shipping labels will have 2 or more pages per order, these are:
		- Shipping Label
		- Packaging Slip
		- Customs Declaration (3x copies, printed seperately on A4 paper)

			!!!info "DHL does not require a Customs Declaration Sheet"
				This information is electronically transmitted to Customs agencies automatically

2. **For International Orders Only:**

	- Sign all copies of the `Customs Declaration Form`
	- Place all signed copies of the `Customs Declaration Form` into a resealable adhesive-backed plastic document holder
	- Paper clip the `Shipping Label` and `Packing Slip` to the front of the plastic document holder

## Packaging Orders

- Begin packaging orders by working through the `Order Packing Checklist`
- Reference the `Order-Packing-Checklist` to determine what packaging is required for the week's fulfillment
- Check-off and write in your initials on the printed `Order-Packing-Checklist` **each time an order is packaged and taped shut**

### Additional Guidelines for Packaging

- Shipments with a pending payment status
    - Check the **Awaiting Payment** section in ShipStation for orders
    	- Always mark these orders as **Paid** so they appear in the `Awaiting Shipping` list
    		- We do not currently use the **Awaiting Payment** list at Opulo for anything, so we always mark things as paid reguardless of payment status.
	- If the `Ship By` field for an **Awaiting Payment** order is blank in ShipStation, manually append the date in `Custom Field 1` into the `Ship By` field
- Shipment comprised of two or more packages poly-strapped together:
	- Adhere the shipping label and other documents to the largest package in the shipment
	- Take care to avoid the shipping documents being obstructed by the poly-straps
	- Write the `order number` onto the smaller boxes within the bundle using a large marker
		- This is done to help the shipping carrier if the bundle breaks apart in transit

!!!note "The `Order-Packing-Checklist` lists what package type an order requires if you are unsure or found the shipping documents sorted into a vague pile"

!!!warning "Serialization and OQC Form Requirements"
	Shipments that contain a uniquely serialized product (LumenPnP, PCB Kit, Replacement Motherboards) must be logged in the [LumenPnP - Serial Tracker and OQC Form](https://docs.google.com/forms/d/e/1FAIpQLSddZwlLa26bw81xRC3UofJ12yaRr4eiF1ZQTFnbHVbXxjBo6A/viewform?usp=sharing)

	- Shipments that contain a LumenPnP must have an orange fragile sticker adhered to the box after being taken through this form

	![](oqc-form.webp)

## Outgoing Quality Control (OQC)

- Sort the taped boxes into the following stacks:
	- DHL
	- USPS Domestic
	- USPS International
	- UPS Domestic
	- UPS International
    - FedEx

- Confirm the following:
	- Docker does not have any assembled goods beyond what's expected to be in `unfulfilled inventory`
	- There is exactly as many packages ready to ship as what's shown in the `order-packing-checklist`
	- Each line in the `order-packing-checklist` is checked-off and initialed
	- No unused shipping labels are left sitting out
	- The first page of any international shipment's custom form matches the receiver's name on the shipping label  

## To do

- Add documentation for replacement part and return shipping label logistics