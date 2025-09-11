## Create Draft Purchase Order
0. Go to the [Purchase Manager](https://opulo.aligni.com/purchases) tab of Aligni

1. Click the ➕ icon to create a new purchase order
	<img style="height:500px width:auto;" src="img/add-part-0.webp">
	
5. Click `Assign PO #` to assign a Purchase Order Number
	<img style="height:500px width:auto;" src="img/add-part-5.webp">

### Add a Line Item
2. Within the purchase order page, click the ➕ icon to add a new line item
	<img style="height:500px width:auto;" src="img/add-part-1.webp">
4. Search Aligni for the part you wish to purchase with either the `Opulo MFG P/N` or `MFG P/N`
4. Select the desired part from the drop-down list
5. Click `Add Part`
	
	<img style="height:500px width:auto;" src="img/add-part-2.webp">
	<img style="height:500px width:auto;" src="img/add-part-3.webp">
	<img style="height:500px width:auto;" src="img/add-part-4.webp">

### Set the part's `Vendor P/N`
6. Click `Set Vendor P/N` to open a selection window 
7. Select a `Vendor P/N` that matches the packaging of on-hand inventory, requesting help from a teammate if needed
8. Copy the  `Vendor P/N`'s URL to your computer's clipboard if available, other copy just the `Vendor P/N`
9. Click `Save`

	<img style="height:500px width:auto;" src="img/add-part-5.5.webp">
	<img style="height:500px width:auto;" src="img/add-part-6.webp">

8. Confirm your screen matches the image below

	<img style="height:500px width:auto;" src="img/add-part-7.webp">

### Find Part in LCSC
9. In a new browser tab, go to the [LCSC website](https://www.lcsc.com/) 
10. Login to LCSC
	<img style="height:500px width:auto;" src="img/add-part-8.webp">
	<img style="height:500px width:auto;" src="img/add-part-9.webp">
	<img style="height:500px width:auto;" src="img/add-part-10.webp">
12. Navigate to the part's product page with any of the following techniques:
	13. Paste the `Vendor P/N`'s URL into your browser's address bar
	14. Paste the `Vendor P/N` into the LCSC search bar found at the top of the website

	<img style="height:500px width:auto;" src="img/add-part-11.webp">
	
### Determine Order QTY
14. In another tab, navigate to the given part's `Inventory` tab in Aligni
15. Examine the `Historical Consumption Rates` and compare it to the volume pricing shown in LCSC while considering the following:
	16. What is our current inventory levels compared to the `Safety Stock` values? 
	17. Is purchasing 6-months or 12-months of inventory reasonable? If a year's worth of a part is only $100, just buy it.
	17. Is this part becoming obsolete soon?
	17. Consider what the price breaks are - is it worth buying 2-years worth of a part we're guaranteed to still be using because of a 40% discount? Maybe.  
	18. Does LCSC have enough in stock?
	19. Does buying more than #pcs increase the lead-time an intolerable amount? 
	20. What QTY does the item come in from the MFG? 

	!!!info "There is a lot to consider here, so asking for help is always welcome"
		However, please feel empowered to spend <$200 if the order covers our needs for 1+ month.	
	
	<img style="height:500px width:auto;" src="img/add-part-11.5.webp">

14. Add the amount you have decided to order to your cart

###Prepare for checkout
16. Select DHL for the shipping service
17. For every line item in your order, input the relevant `Opulo MFG P/N` into the `Customer #` text-field 
18. Click `Checkout`
	
<img style="height:500px width:auto;" src="img/add-part-12.webp">
	
!!!warning "Do not continue with the checkout process on LCSC until the purchase order has been approved"

###Update the purchase order for component QTY and unit cost
15. Copy/paste the chosen `order QTY` from LCSC to the part's `purchase QTY` field in Aligni
16. Copy/paste the chosen `unit price` from LCSC to the part's `unit price` field in Aligni
17. Confirm the given part's `EXT. Price` matches between LCSC and Aligni
	
	<img style="height:500px width:auto;" src="img/add-part-16.webp">

###Add Shipping to PO
	
20. Add line item for shipping to purchase order
	
	<img style="height:500px width:auto;" src="img/add-part-17.webp">
	<img style="height:500px width:auto;" src="img/add-part-18.webp">

21. Set LCSC as the part's vendor
	<img style="height:500px width:auto;" src="img/add-part-19.webp">
22. Words
	<img style="height:500px width:auto;" src="img/add-part-20.webp">

### Edit PO Info

23. Click `Edit PO`
	<img style="height:500px width:auto;" src="img/add-part-21.webp">
24. Update the following fields:
	25. Payment Terms: CIA
	26. INCOTERM: DDU
	27. DELIVERY TERMS: Ship via DHL
	
	<img style="height:500px width:auto;" src="img/add-part-22.webp">

24. Click `Save` to close the `Edit Purchase Order` window

###PO Approval Process

25. If the expense is <$200, click `Approve`

	!!!info "Technicians are able to approve purchases <$200 without manager approval"

	<img style="height:500px width:auto;" src="img/add-part-23.webp">

	!!!warning "If the order is `$200<`, you must submit the purchase for manager approval"

26. A confirmation pop-up will be shown when the purchase order has been approved
<img style="height:500px width:auto;" src="img/add-part-24.webp">
	
### Placing the Order
15. Return to LCSC's order checkout page and perform the following tasks:
	17. Input the purchase order number
	18. Confirm the choose of shipping provider is still DHL
	19. Confirm the billing and shipping address
	20. Click `Submit Order`
	
	<img style="height:500px width:auto;" src="img/add-part-13.webp">

16. Select `Checkout (Credit/Debit Card)` from the list of Payment Methods
	<img style="height:500px width:auto;" src="img/add-part-14.webp">
17. Enter the provided card details before clicking `Pay`
	<img style="height:500px width:auto;" src="img/add-part-15.webp">
