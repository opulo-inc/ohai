# Create a Purchase Order in Aligni

## Draft the Purchase Order

1. Navigate to [https://opulo.aligni.com/purchases](https://opulo.aligni.com/purchases)

	![][image1]

2. Click "+" to create a new Purchase Order

	![][image2]

3. Review the Purchase Details before clicking "Update"

	![][image3]

## Edit Terms

* To be added

## Add the 1st part

4. Click the "+" to add a part to the purchase order

	![][image4]

5. Type the beginning of the part name you are buying and select it from the drop-down list when available

	![][image5]

6. Click "Add Part"

	![][image6]

7. Double-click the unit price text field and input a price – making sure it matches what you were quoted

	![][image7]

8. Change the purchase unit from "each" to something else – if needed

9. Double-click the purchase quantity text field to input a value

	![][image9]

10. Click "Set Vendor P/N"

	![][image10]

11. Select the part's Vendor Part Number

	![][image11]

12. Click "Save"

	![][image12]

13. The vendor part number will now be applied to the line item

	![][image13]

## Add a 2nd part

For this 2nd part, we will input a price directly from a previously entered quote in Aligni

14. Click the "+" to add a part to the purchase order

	![][image14]

15. Type the beginning of the part name you are buying and select it from the drop-down list when available

	![][image15]

16. Click "Add Part"

	![][image16]

17. Double-click the unit price text field to input a value.

	![][image17]

18. Click on the correct price listed in the Helper sidebar ($0.80 in this example)

	![][image18]

19. Double-click the purchase quantity text field to input a value

	![][image19]

20. Type the amount of an item you wish to receive

	![][image20]

21. Change the purchase unit from "each" to something else – if needed

22. Click "Set Vendor P/N"

	![][image21]

23. Choose the correct Vendor P/N (HFC-128-6mm in this example)

	![][image22]

24. Click "Save"

	![][image23]

## Edit Purchase Order details

### Assign a PO number

25. Click "- Assign" to assign a PO number to the order – these are auto generated

	![][image24]

### Set the desired Global Delivery Date

26. Click "Edit Details"

	![][image25]

27. Click "No delivery date" to expand the delivery date menu

	![][image26]

28. Choose "Deliver on or before"

	![][image27]

29. Click within the delivery date-field

	![][image28]

30. Pick the desired delivery date from the calendar pop-up menu

	![][image29]

31. Click outside the calendar pop-up menu once a date has been chosen

	![][image30]

32. Click "Update"

	![][image31]

!!! info "Delivery Dates can also be set on per line item basis"

## Add Shipping and/or other Unmanaged Items

33. Click "ADD UNMANAGED ITEM"

	![][image32]

34. Type the intended Shipping Service into the Manufacture P/N text-field
	* For this example we will enter "UPS Ground"

	![][image33]

35. Set "QUANTITY" to 1

	![][image34]

36. Click "PRICE" and enter the shipping charge for the given PO in the price field.

	![][image35]

	![][image36]

37. Click "UNIT OF MEASURE" and enter "per order"

	![][image37]

	![][image38]

38. Once you have finished filling out the required text-fields, click "Add Item" to add the Unmanaged Item to the Purchase Order.

	![][image39]

39. Assign all unmanaged items (such as shipping charges, bank fees, sales tax) to match the vendor of the other items in the PO.

	a. Click "Select Vendor"

	![][image40]

	b. Select the vendor responsible for the other line items in the PO

	![][image41]

	![][image42]

	 c. Confirm all line items list the same vendor before continuing onward

	![][image43]

## Verify Purchase Order Accuracy

Next we need to verify that draft/unapproved PO PDF renders correctly and that all required information is present when viewed outside of Aligni.

44. Click "Download PO"

	![][image44]

45. Open the downloaded PO PDF and review it for accuracy

	![][image45]

46. It's best practice to do one of the following before continuing:

	* Delete this PDF off your computer
	* Add " - Draft" to the end of the downloaded PO's filename

!!! note
	If you are sharing a draft PO PDF with a vendor or teammate for review, please add a red "DRAFT" (font size 200) watermark somewhere that cannot be cropped or easily edited away.

![][image46]

## Finalize PO

47. Click "APPROVE" (if this option is not available click "Submit for Approval" instead)

	![][image47]

48. Click "X" to close the confirmation pop-up

	![][image48]

## Verify Vendor Purchase Order Web Portal Page

49. Click "Vendor PO page"

	![][image49]

50. Confirm everything looks correct

	![][image50]

## Sharing the PO

Usually our purchase orders need to be shared to someone at a vendor's facility for them to acted upon, however you may not need to share the PO if purchasing these items does NOT require communication with the vendor.

This is more common when purchasing basic off-the-shelf (OTS) commodity items through regular retail web stores.

* Examples include:

	* Aggregation platforms like AliExpress or Amazon
	* Big vendors that have made purchasing from them very streamlined – such as Mouser or Analog Devices

If this is the case for the PO you are making, you can skip ahead to [Mark PO as Submitted](#mark-po-as-submitted).

Follow the steps below if you are ordering material from a vendor that Opulo must communnicate with for material to be delivered to our produciton line.

### Email PO to Vendor via Aligni

Aligni is capable of emailing the PO direct to our vendor when contact information for them is on file.

51. Double-click "Email PO"

	![][image51]

52. If a "Send" button is available, you may now click it to share the PO!  

	* The PO will automatically change status to "Submitted" when successfully shared this way

	![][image52]

!!! note
	In this example, there's actually no contact information listed for this vendor in Aligni so we must manually share via the steps shown below.

!!! info "If you are able to transmit the PO through Aligni..."
	the only thing left to do is confirm the vendor received it via regular communication channels. Once you have done this, you are all set until the order arrives onsite!

	The following steps in this SOP can be ignored in this case ✅

### Manually Send PO to Vendor

Manually download the PO to your computer and share it via email, Alibaba, or however else you may need to share it.

## Mark PO as Submitted

!!! note "The steps below still matter – even if the PO does not need to be shared with a vendor"

54. Click "Mark as Submitted"

	![][image53]

55. Click "Mark as Submitted" again, this time in the pop-up dialog window

	![][image54]

56. Click "OK" to close the pop-up dialog window

	![][image55]

!!! success "The Purchase Order is now fully live and capable of being referenced by our Material Planning tools!"

[image1]: img/img_001.webp

[image2]: img/img_002.webp

[image3]: img/img_003.webp

[image4]: img/img_004.webp

[image5]: img/img_005.webp

[image6]: img/img_006.webp

[image7]: img/img_007.webp

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

[image28]: img/img_028.webp

[image29]: img/img_029.webp

[image30]: img/img_030.webp

[image31]: img/img_031.webp

[image32]: img/img_032.webp

[image33]: img/img_033.webp

[image34]: img/img_034.webp

[image35]: img/img_035.webp

[image36]: img/img_036.webp

[image37]: img/img_037.webp

[image38]: img/img_038.webp

[image39]: img/img_039.webp

[image40]: img/img_040.webp

[image41]: img/img_041.webp

[image42]: img/img_042.webp

[image43]: img/img_043.webp

[image44]: img/img_044.webp

[image45]: img/img_045.webp

[image46]: img/img_046.webp

[image47]: img/img_047.webp

[image48]: img/img_048.webp

[image49]: img/img_049.webp

[image50]: img/img_050.webp

[image51]: img/img_051.webp

[image52]: img/img_052.webp

[image53]: img/img_053.webp

[image54]: img/img_054.webp

[image55]: img/img_055.webp