# Opulo Order Fulfillment SOP

## Deciding What to Fulfill

- Review Coeffient V3 to see which orders should be shipped based off their `Batch WK#`
	- Orders are sorted into a given `Batch WK#` based off their `Planned Ship Date`, which may differ from the `Order Due Date`
  
	![](batching-orders.webp)

	!!!info "See [here](planned-ship-date-calc.md) for more information on our Planned Ship Date calculations"  

3. Go to ShipStation and create a batch for the orders that fall within the given `Batch WK#` you wish to fulfill.

	- Name the ShipStation batch to `Batch WK#`, where `#` is replaced with the batch's given week number
	- Be sure to select the correct box size for the items and ask for help if needed

## Prepare the Order-Packing-Checklist

- Prepare an `Order-Packing-Checklist` for the week's fulfillment using the [Google Slides template](https://docs.google.com/presentation/d/1bjngnZyvqVTuc3WafVRS6TTGYHAocfyJrHuGKA1xy9k/edit?usp=sharing)

	- Make a copy of the most recent slide and replace the image with the screenshot of the ShipStation batch you are working with
	- The checklist printout should look like the following image:

		![](Order-Packing-Checklist.webp)

3. Fill in the time and date for any scheduled pickup, per carrier

  	 - Write "Drop off" for any carrier that we will bring the packages to ourselves

2. Print out the week's checklist when ready

## Purchasing Shipping Labels

3. Review each ShipStation order in the batch for correctness - double check the package size, declared values, and shipping methods are all appropriate

	!!!note "Training is required for this step"
		Please ask Lucy for help if it's your first time doing this.

4. Purchase the labels

## Create a Pickup

5. Set the `Pickup Date` for the required shipping carriers

  - Customers can currently pick between UPS, USPS, and DHL at checkout so multiple pickups may be required

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
	- Alert customer service when these orders are ready for shipping , so that the team is given notice when an order with NET## terms has been shipped out
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

- Confirm the following:
	- Docker does not have any assembled goods beyond what's expected to be in `unfulfilled inventory`
	- There is exactly as many packages ready to ship as what's shown in the `order-packing-checklist`
	- Each line in the `order-packing-checklist` is checked-off and initialed
	- No unused shipping labels are left sitting out
	- The first page of any international shipment's custom form matches the receiver's name on the shipping label  
