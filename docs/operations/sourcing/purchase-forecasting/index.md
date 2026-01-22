# Purchase Forecasting

This SOP defines the standardized workflow for forecasting and purchasing materials. Mainly, it's used to ensure we don't run out of stock.

We have an Aligni SKU called `BATCH-0002` which is used to run Material Shortage Report in Aligni. Every week on Monday, after the previous week's build is completed, we *uprev* `BATCH-0002` to have a BOM of *everything we sold in the last 90 days*. Then, when we ask Aligni what happens when we do a build for QTY 1, due in 90 days, we'll see what we're likely to run out of, and what we should purchase.

This is similar to how we do weekly removal of inventory with a QTY 1 build of `BATCH-0001`. However, we never *actually* build `BATCH-0002`, it's only ever used to check Material Shortage report, then the Build draft is deleted.

**This should only happen with an accurate inventory count.** This means:
 - All inventory received
 - All completed builds finalized


## Getting our last 90 days of sales

1. In Shopify, click on Analytics -> Reports -> SKU QTYs Sold in the last 90 Days

2. Click the three dot menu in the upper right corner, click Export.

3. Select CSV and All results from the data query. Click Export.

## Update BATCH-0002 in Aligni

1. Navigate to:  
   **[Proxy SKU] → Bill of Materials → New Revision → Import BOM**
      * Name the new revision based off the forecast year/week range it corresponds to
2. Import the updated BOM sheet.  
3. Select the "Clear existing partlist before importing" import option
4. Release the new revision

## Create a QTY 1 Build

1. Navigate to:  
   **Production → Create Build**
2. Select BATCH-0002.  
3. Set:
      - **Build Quantity:** `1`
      - **Attrition:** Enabled
      - **Drill Down:** Enabled
      - **Start Date:** Today
      - **Completion Date:** Today + 90 days

4. Click **Create Build**.

1. Click **Allocate Material**.  

2. Ensure all available stock is allocated to the build.

## Run a Material Shortage Report

Now that we have an allocated build of everything we'll likely build in the next quarter, we can run Material Shortage Report to see what we'll run out of!


1. Navigate to:  **Reports → Material Shortage Report**

2. Set filters to: **Build:** Select the active Proxy SKU build (1 pcs)

3. Run the report.

4. For each item listed:
      - Identify items with **negative availability**  
      - Identify items predicted to run out before the build completion date  
      - Note manufacturer lead time, MOQ, historical slip, and vendor reliability  

Any item predicted to stock-out within 3 months triggers a purchase.
