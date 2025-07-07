
# Removing Non-Serialized Items from `Opulo Managed Inventory` per Production Batch #

1. Navigate to [https://ship13.shipstation.com/home](https://ship13.shipstation.com/home) and login

    ![](img/step_001.png)

2. Click "Shipments"

    ![](img/step_003.png)

3. Expand the "Batches" drop-down menu and select "Open"

    ![](img/step_002.png)

4. Click "WK27" (or the given production week # you are working with)

    ![](img/step_004.png)

5. Click "Export Orders"

    ![](img/step_005.png)

6. Click "Export order line items"

    ![](img/step_006.png)

7. Click the "Weekly Non-Serialized Item Removal" field.

    ![](img/step_007.png)

8. Click "Export"

    ![](img/step_008.png)

9. Navigate to tab "Weekly Aligni Item Removals - Google Drive"

    ![](img/step_009.png)

10. Make a copy of "WK ## NON-SERIALIZED ITEM REMOVAL"

    ![](img/step_010.png)

11. Right-click "WK ## NON-SERIALIZED ITEM REMOVAL"

    ![](img/step_011.png)

12. Click "Make a copy"

    ![](img/step_013.png)

13. Right-click "Copy of WK ## NON-SERIALIZED ITEM REMOVAL"

    ![](img/step_012.png)

14. Click "Rename"

    ![](img/step_015.png)

15. Click this text field.

    ![](img/step_014.png)

16. Click this text field.

    ![](img/step_016.png)

17. Type "[[Backspace]]" to delete "Copy of " from the front of the filename

18. Replace ## with the given production lot's week number

    ![](img/step_018.png)

19. Type "27" (for example)

20. Click "OK"

    ![](img/step_021.png)

21. Double-click "WK 27 NON-SERIALIZED ITEM REMOVAL" and Open the File

    ![](img/step_020.png)

22. Right-click "WK ## FROM SHIPSTATION"

    ![](img/step_023.png)

23. Click "Rename" on the first tab of the Workbook

    ![](img/step_022.png)

24. Click "WK ## FROM SHIPSTATION"

    ![](img/step_024.png)

25. Replace ## with the production lot's given week number – "27" in this case

26. Click "WK ## NON SERIALIZED ITEMS TO REMOVE"

    ![](img/step_027.png)

27. Right-click "WK ## NON SERIALIZED ITEMS TO REMOVE"

    ![](img/step_026.png)

28. Click "Rename"

    ![](img/step_029.png)

29. Click "WK ## NON SERIALIZED ITEMS TO REMOVE"

    ![](img/step_028.png)

30. Replace ## with the production lot's given week number – "27" in this case

31. Click "WK 27 FROM SHIPSTATION" to exit the renaming pop-up window

    ![](img/step_031.png)

32. Navigate to the "WK## FROM SHIPSTATION" tab

33. Select Cell "A1"

34. Click "File"

    ![](img/step_035.png)

35. Click "Import"

    ![](img/step_034.png)

36. Click "Upload"

    ![](img/step_036.png)

37. Click "Browse"

    ![](img/step_037.png)

38. In your computer's file explorer, navigate to and select the .CSV file you previously exported from ShipStation

39. Click "Create new spreadsheet" and expand the drop-down menu

    ![](img/step_039.png)

40. Select "Replace data at selected cell"

    ![](img/step_041.png)

41. Select "Import data"

    ![](img/step_040.png)

42. Confirm all data imported correctly from the top to bottom

    ![](img/step_043.png)

    ![](img/step_042.png)

44. Switch to the "WK ## NON SERIALIZED ITEMS TO REMOVE" tab

    ![](img/step_044.png)

45. Click on the Pivot Table

    ![](img/step_045.png)

46. Select the "Edit" pop-up button

    ![](img/step_046.png)

47. Edit the filtered "BASE SKU" list

    ![](img/step_047.png)

48. Click "Clear" to deselect all SKUs

    ![](img/step_048.png)

49. Click "Select all"

    ![](img/step_049.png)

50. Click "(Blanks)" to remove items without SKU numbers

    ![](img/step_050.png)

51. In the Filtered List search bar, type "sku-00"

52. Click "SKU-0002" to filter LumenPnP units from the list

    ![](img/step_052.png)

53. Repeat this step, as needed, to remove any of the following items:

	- Replacement Motherboards
	- Control Boxes

54. Click "OK"

    ![](img/step_055.png)

55. Click here to exit the Pivot table editor

    ![](img/step_054.png)

56. Click "File"

    ![](img/step_056.png)

57. Select "Download" from the File drop-down menu before selecting "Comma Separated Values (.csv)"

    ![](img/step_057.png)

58. Navigate to [opulo.aligni.com](opulo.aligni.com)

59. Click on the search button in the top-right of the UI

    ![](img/step_059.png)

60. Type "Batch-0001" in the search bar's text field

    ![](img/step_061.png)

61. Click "BATCH-0001"

    ![](img/step_060.png)

62. Click "New Revision"

    ![](img/step_062.png)

63. Disable "Copy part list from source revision"

    ![](img/step_063.png)

64. Click the "Revision Name" field.

    ![](img/step_064.png)

65. Type "WK#27" (the given week number of the production lot you are working with)

66. Click the Create button

    ![](img/step_066.png)

67. Click the BOM tab's drop-down menu.
    ![](img/step_067.png)

68. Click "Part List"

    ![](img/step_068.png)

69. Click "Import CSV"

    ![](img/step_069.png)

70. Click "Drag a file here to upload, or  choose a file from your computer"

    ![](img/step_070.png)

71. From your computer's file explorer, navigate to and select the .CSV previously downloaded from Google Sheets

72. Map Part Number to "Column 1 (BASE SKU)"

    ![](img/step_073.png)

73. Map QUANTITY to "Column 2 (SUM of Item - Qty)"

    ![](img/step_072.png)

74. Click "Match Parts & Move to Step 3"

    ![](img/step_074.png)

75. Perform the following two steps on this page:

	1. Select the "Add to working partlist" import option  
	2. Click "Import Parts"

	![](img/step_075.png)

76. You will be returned to the BOM (Part List) view

    ![](img/step_076.png)

77. Remove any errant items by clicking the "Red X" in the Actions column of the Part list  
	
	- It's important to remove any items from this list that may have already been previously removed from inventory – sometimes replacement parts shipped fast can be guilty of this

    ![](img/step_077.png)

78. Click "Yes" to remove anything that shouldn't be accounted for

    ![](img/step_078.png)

79. Click "Release this Revision"

    ![](img/step_080.png)

80. Click "Release Revision"

    ![](img/step_079.png)

81. Click "New Build"

    ![](img/step_081.png)

82. Click "Create a single build"

    ![](img/step_082.png)

83. Click the "Title" field.
    ![](img/step_083.png)

84. Type "Build for non-serialized goods made during WK #27" (27 for example)

85. Click the "Build Quantity" field.
    ![](img/step_085.png)

86. Type "1"

87. Enable "DRILL-DOWN PARTLIST"

    ![](img/step_088.png)

88. Click the "Expected Reservation Date" field and set it to the day the production lot began

    ![](img/step_087.png)

89. Click the "Expected Completion Date" field and set it to the date the production lot is scheduled to be completed

    ![](img/step_089.png)

90. Click "Create Build"

    ![](img/step_090.png)

91. Click "Allocate..."

    ![](img/step_091.png)

92. Click "Allocate" from the pop-up window

    ![](img/step_092.png)

93. Click "Reserve Inventory..."

    ![](img/step_094.png)

94. Click "Reserve"

    ![](img/step_093.png)

95. Click "Parts"

    ![](img/step_096.png)

96. Confirm all material has been properly reserved before navigating to the "Finalize" tab

    ![](img/step_095.png)

97. Disable "Add final assembly to inventory"

    ![](img/step_097.png)

98. Pick "Computed Price ($####.##)" as selected "Record Cost As" option

99. Click "Finalize Build..."

    ![](img/step_099.png)

100. Click "Finalize Build"

    ![](img/step_100.png)

101. Click "Parts"

 	 ![](img/step_102.png)

102. Confirm all parts have been removed

   ![](img/step_101.png)
