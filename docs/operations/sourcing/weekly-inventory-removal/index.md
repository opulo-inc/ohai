## Finalizing Last Week's Build

97. Navigate to the Finalize tab of the previous week's build, and disable "Add final assembly to inventory"

    ![](img/step_097.webp)

98. Pick "Computed Price ($####.##)" as selected "Record Cost As" option

99. Click "Finalize Build..."

    ![](img/step_099.webp)

100. Click "Finalize Build"

    ![](img/step_100.webp)

101. Click "Parts"

 	 ![](img/step_102.webp)

102. Confirm all parts have been removed
  ![](img/step_101.webp)

## Creating This Week's Build

### Export Item Removal List from ShipStation

1. Navigate to [https://ship13.shipstation.com/home](https://ship13.shipstation.com/home) and login

    ![](img/step_001.webp)

2. Click "Shipments"

    ![](img/step_003.webp)

3. Expand the "Batches" drop-down menu and select "Open"

    ![](img/step_002.webp)

4. Click "WK27" (or the given production week # you are working with)

    ![](img/step_004.webp)

5. Click "Export Orders"

    ![](img/step_005.webp)

6. Click "Export order line items"

    ![](img/step_006.webp)

7. Click the "Weekly Non-Serialized Item Removal" field.

    ![](img/step_007.webp)

8. Click "Export" and save the file somewhere you can easily it on your computer

    ![](img/step_008.webp)

### Removal items from inventory in Aligni

#### Up-Rev the Removal Batch Item

58. Navigate to [opulo.aligni.com](opulo.aligni.com)

59. Click on the search button in the top-right of the UI

    ![](img/step_059.webp)

60. Type "Batch-0001" in the search bar's text field

    ![](img/step_061.webp)

61. Click "BATCH-0001"

    ![](img/step_060.webp)

62. Click "New Revision"

    ![](img/step_062.webp)

63. Disable "Copy part list from source revision"

    ![](img/step_063.webp)

64. Click the "Revision Name" field.

    ![](img/step_064.webp)

65. Type "2025 WK#27" (the given week number and year of the production lot you are working with)

66. Click the Create button

    ![](img/step_066.webp)

67. Click the BOM tab's drop-down menu.
    ![](img/step_067.webp)

68. Click "Part List"

    ![](img/step_068.webp)

69. Click "Import CSV"

    ![](img/step_069.webp)

70. Click "Drag a file here to upload, or  choose a file from your computer"

    ![](img/step_070.webp)

71. From your computer's file explorer, navigate to and select the .CSV previously downloaded from Google Sheets

72. Map Part Number to "Column 1 (BASE SKU)"

    ![](img/step_073.webp)

73. Map QUANTITY to "Column 2 (SUM of Item - Qty)"

    ![](img/step_072.webp)

74. Click "Match Parts & Move to Step 3"

    ![](img/step_074.webp)

75. Perform the following two steps on this page:

	1. Select the "Clear existing partlist before importing" import option  
	2. Click "Import Parts"

76. You will be returned to the BOM (Part List) view

    ![](img/step_076.webp)

77. Add any parts that were added to production this week. This should only be any replacement parts that shipped. 

79. Click "Release this Revision"

    ![](img/step_080.webp)

80. Click "Release Revision"

    ![](img/step_079.webp)

#### Make a 1pcs Build for the Removal Batch Item

81. Click "New Build"

    ![](img/step_081.webp)

82. Click "Create a single build"

    ![](img/step_082.webp)

83. Click the "Title" field.
    ![](img/step_083.webp)

84. Type "Build for non-serialized goods made during WK #27" (27 for example)

85. Click the "Build Quantity" field.
    ![](img/step_085.webp)

86. Type "1"

87. Enable "DRILL-DOWN PARTLIST"

    ![](img/step_088.webp)

88. Click the "Expected Reservation Date" field and set it to the day the production lot began

    ![](img/step_087.webp)

89. Click the "Expected Completion Date" field and set it to the date the production lot is scheduled to be completed

    ![](img/step_089.webp)

90. Click "Create Build"

    ![](img/step_090.webp)

91. Click "Allocate..."

    ![](img/step_091.webp)

92. Click "Allocate" from the pop-up window

    ![](img/step_092.webp)

93. Click "Reserve Inventory..."

    ![](img/step_094.webp)

94. Click "Reserve"

    ![](img/step_093.webp)

95. Click "Parts"

    ![](img/step_096.webp)

96. Confirm all material has been properly reserved.

    ![](img/step_095.webp)

97. Get the build number to the Production Team for use in serializing any products that require a serial.
