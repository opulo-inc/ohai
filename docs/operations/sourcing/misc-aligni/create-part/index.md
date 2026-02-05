# Create a New Part and Add Vendor Information

## Create new part

1. Navigate to [https://opulo.aligni.com/](https://opulo.aligni.com/)

	![][img1]

2. Click `New Part`

	![][img2]

3. You will now be brought to the `Create New Part` page

## Enter part attributes
1. Select a `Manufacturer` –
   * Select the Manufacturer who is responsible for the creation of this part
     * Select "Opulo" if we are the manufacturer
     * Select one of the relevant "Generic Factory" options if the part can be made by multiple equivalent sources – AND we aren't exactly sure where it's truly made

2. Enter a `Manufacturer Part Number` –
	* This would be the alphanumeric part number the manufacturer assigned to the given part you are adding to Aligni

	![][img3]

3. Set a `Part Type` –

	* There's many different types you can pick from that match up with different types of parts that we have in our supply chain.  
	* For this example, we'll pick `Fabricated, Other` - a catch-all for items whose type do not match other choices in the drop-down

	![][img4]

4. Select a `Unit of Measure` for the given part –

	* This option corresponds to how the item is consumed.  
	* It can be a measure of length, weight, volume, or something more specific.  
	* For this part, we'll pick `each`.

	![][img5]

5. Set `Manufactured Here?` –

	* This field is asking whether or not the item is built by Opulo or not.  
	* If an item is something we purchase as-is from a vendor, have `Manufactured Here?` be disabled.

	![][img6]

6. Set Revision fields

	* `Revision Name` –

		* When creating a new part, use 00 as the revision name unless the manufacturer already has a revision name for the part.

	* `Revision Reason` –

		* For a new part, input `Initial Release` here.  
		* This field is used to briefly explain differences in part revisions when up-rev'ing to subsequent versions.

	![][img7]

7.  RoHS Compliance  
  
	* Select the appropriate option for RoHS Compliance
		* Select the `Yes` option if you know the part to be RoHS compliant  
		* Select `Unknown` if you are unsure about the RoHS status of the part  
		* Select `No` if you know with certainty this part is not RoHS compliant  
 
	!!!info "What is RoHS (Restriction of Hazardous Substances)?"
		RoHS is a European Union rule (Directive 2002/95/EC) that limits the use of certain harmful materials in electrical and electronic products.

	![][img8]

8.  Click Create

	![][img9]

9.  Aligni will bring you to the `Details` tab of the newly created Part

	![][img10]
	
## Enter Vendor data

12. Navigate to the `Supply Chain` tab

	![][img11]

13. Add a `Vendor Part Number`

	![][img12]

14. Set the vendor to match where the part can be purchased from

	* For this example we will select `Fake Vendor`

	![][img13]

15. Select the `Buy Unit`  –

	* This can be different than the use-as unit

	* For example, the fasteners we buy from McMaster-Carr are often sold in 100-piece sets, so it'd be appropriate then to choose 100pcs set as the `Buy Unit`.

	* For the item being created in guide, we're just going to leave it as is.

	![][img14]

16. Set the `Vendor Part Number`

	![][img15]

17. Type the alphanumeric value the vendor uses for the part number field in their purchasing system. We'll use `HFC-128-5mm` for this example.

	![][img16]

18. When finished, click `Create new Vendor Part Number`

	![][img17]

19. Set a `Standard Cost and Lead Time` by clicking `Click here to set`

	![][img18]

20. Input the `Standard Cost` data
	* This is a single reference cost associated with the item.
	* Typically, this cost is determined manually based on recent quote and purchase.

	![][img19]

21. Click `Save` to apply changes and close the window

	![][img20]

22. Set `Preferred Vendor`

	![][img21]

	![][img22]

23. Click `Update` to apply the change and close the window

	![][img23]

## Enter Quote data

24. Click `Create` a new quote

	![][img24]

25. Input the `New Quote` data –

	* Vendor -  
	* Price -  
	* Buy Unit -  
	* Currency -  
	* Minimum -  
	* Multiple -  
	* Lead Time -  
	* Vendor Inventory -  
	* Valid For -  
	* Comment -

	![][img25]

26. Click `Create and Add Another` if you have multiple prices to input –

	* This may be the case if you have either:
		* a higher price that corresponds to a faster lead-time
		* a lower price that corresponds to a higher minimum purchase quantity
		* Literally any other reason

		![][img26]

	* If you just have one price/lead-time to input simply click `Create` to apply the change and close the window.

	!!!note "For the sake of this walk-through we'll add an additional quote to this item."

27. Let's say you have different prices at various order quantities, so this item is $0.80 when you purchase at least 10pcs.

	![][img27]

28. Click `Create` once the additional quote has been fully entered.

	![][img28]

29. Two different prices will now be shown in the `Cost and Lead Time` table.

	![][img29]

## Release the part

30. Once all the above data input is completed, click `Release the Revision`.

	![][img30]

31. Click `Release Revision` again

	![][img31]

32. Aligni will then navigate to the Revisions tab where you can confirm the part's initial revision was successfully released.

	![][img32]

!!!success "Return to the Part Details tab and confirm everything looks good. The item is now purchasable!"
	![][img33]

[img1]: img/img_1.webp

[img2]: img/img_2.webp

[img3]: img/img_3.webp

[img4]: img/img_4.webp

[img5]: img/img_5.webp

[img6]: img/img_6.webp

[img7]: img/img_7.webp

[img8]: img/img_8.webp

[img9]: img/img_9.webp

[img10]: img/img_10.webp

[img11]: img/img_11.webp

[img12]: img/img_12.webp

[img13]: img/img_13.webp

[img14]: img/img_14.webp

[img15]: img/img_15.webp

[img16]: img/img_16.webp

[img17]: img/img_17.webp

[img18]: img/img_18.webp

[img19]: img/img_19.webp

[img20]: img/img_20.webp

[img21]: img/img_21.webp

[img22]: img/img_22.webp

[img23]: img/img_23.webp

[img24]: img/img_24.webp

[img25]: img/img_25.webp

[img26]: img/img_26.webp

[img27]: img/img_27.webp

[img28]: img/img_28.webp

[img29]: img/img_29.webp

[img30]: img/img_30.webp

[img31]: img/img_31.webp

[img32]: img/img_32.webp

[img33]: img/img_33.webp