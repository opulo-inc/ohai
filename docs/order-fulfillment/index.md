# Opulo Order Fulfillment SOP

## Deciding What to Fulfill:

1. Review the `Opulo Shopify Store - Coefficient Data Steam` for orders that are eligible for fulfillment. The following criteria must be met:
		
	- Every line item in the `order` must have an `Est Ship Date` value that's no later than Friday of the given production week
	- 	All of the line items within the order number must have one of the following fulfillment statuses: 
		- `UNFULFILLED - PAID`
		- `UNFULFILLED - PENDING`
		- `UNFULFILLED - PARTIALLY REFUNDED` 
			
			!!!warning "Please double-check items with this status before fulfilling them!"
				It is important to lookup orders with this status in Shopify to determine what exactly was refunded prior to fulfillment. It is possible for Coefficient to state that a refunded item still required fulfillment so we must be careful in these circumstances.
				
	-  Each line item within the order must have a `Build Number` entered
	-  Each line item within the order must have the `Built?` checkbox checked
		
		!!!info "This checkbox is to indicate that an item is on a shelf in salable form, ready for shipping"
		
2. Review `Opulo Shopify Store - Coefficient Data Steam` queue for `Replacement Parts` orders that **SHOULD** be shipped this week that didn't receive an `Est Ship Date` or `Build Number`
	- If feasible, create a build for these items in Aligni with a due-date that matches the `Est Ship Date` desired 
	- Enter a matching `Est Ship Date` for any replacement part that is being added to the fulfillment batch
	- Check-off the `Built?` checkbox when the replacement part's build has been completed

## Purchasing Shipping Labels:

3.  Go to Shopify and purchase shipping labels for `orders` that met the criteria listed in the previous step
	- Be sure to select the correct box size for the items and ask for help if needed

4. Screenshot the `Purchased Shipping Label` webpage in Shopify to create the `Order-Packing-Checklist` for the week
	- We will come back to this in the next section 

5. Set the `Pickup Date` for the required shipping carriers 
 - Customers can currently pick between UPS, USPS, and DHL at checkout so multiple pickups may be required

6. Print out all the shipping labels for the week on `4x6 Label Paper` with the Dymo 4XL Label Printer

7. Return to the `Opulo Shopify Store - Coefficient Data Steam` and input the date each fulfilled order is expected to be transferred to the shipping carrier in the `Actual Ship Date` text-field

## Prepare the Order-Packing-Checklist

1. Prepare an `Order-Packing-Checklist` for the week's fulfillment using the [Google Slides template](https://docs.google.com/presentation/d/1bjngnZyvqVTuc3WafVRS6TTGYHAocfyJrHuGKA1xy9k/edit?usp=sharing) 
	-  Make a copy of `Slide 1` and replace the image with the screenshot taken in the earlier section, adjusting the slide as needed
	- The checklist printout should look like the following image:
![](Order-Packing-Checklist.png)

2. Print out the week's checklist when ready
3. Write in the time and date for any scheduled pickup, per carrier
4. Write "Drop off" for any carrier that we will bring the packages to ourselves

## Handling the Shipping Labels
1. Separate the printed shipping labels while leaving all pages related to a given `order` connected
	- Domestic shipping labels will have 2 pages per order, these are: 
		- Shipping Label 
		- Packaging Slip
	- 	International shipping labels will have 2 or more pages per order, these are: 
		- Shipping Label 
		- Packaging Slip
		- Customs Declaration 
			
			!!!info "DHL does not require a Customs Declaration Sheet"
				This information is electronically transmitted to Customs agencies automatically

2. **For International Orders Only:**
	- Sign all copies of the `Customs Declaration Form`
	- Place all signed copies of the `Customs Declaration Form` into a resealable adhesive-backed plastic document holder
	- Paper clip the `Shipping Label` and `Packing Slip` to the front of the plastic document holder

4. Sort the shipping documents into containers that reflect the packaging used
	- The containers used for sorting should correspond to the packaging the week's orders require
	- Reference the `Order-Packing-Checklist` to determine what packaging is required for the week's fulfillment

## Packaging Orders
- Begin packaging orders by working through each container's sorted shipping documents
	- For example pack every order that had its shipping documents sorted into the `2-Tray OPF bin` before proceeding to the shipping documents sorted in the `4-Tray OPF bin` 
	- This will help prevent shipping customers more or less than of what they paid for
- Check-off and write in your initials on the printed `Order-Packing-Checklist` **each time an order is packaged and taped shut**

!!!warning "Serialization and OQC Form Requirements"
	Shipments that contain a uniquely serialized product (LumenPnP, PCB Kit, Replacement Motherboards) must be logged in the [LumenPnP - Serial Tracker and OQC Form](https://docs.google.com/forms/d/e/1FAIpQLSddZwlLa26bw81xRC3UofJ12yaRr4eiF1ZQTFnbHVbXxjBo6A/viewform?usp=sharing)
	
	- Shipments that contain a LumenPnP must have an orange fragile sticker adhered to the box after being taken through this form

	![](oqc-form.png)

## Outgoing Quality Control (OQC)
- Sort the taped boxes into the following stacks:
	- DHL
	- USPS Domestic
	- USPS International
	- UPS Domestic
	- UPS International

- Confirm the following: 
 	- Docker does not have any assembled goods beyond what's expected to be in unfulfilled inventory
 	- There is exactly as many packages ready to ship as what's shown in the `order-packing-checklist`
 	- Each line in the `order-packing-checklist` is checked-off and initialed
 	- No unused shipping labels are left sitting out
 	- The first page of any international shipment's custom form matches the receiver's name on the shipping label 	


