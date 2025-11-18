# Purchase Forecasting & Planning SOP  

**Revision:** Draft  
**Cadence:** Weekly (with Monthly & Quarterly supplements)

---

## 1. Purpose
This SOP defines the standardized workflow for forecasting and purchasing materials using a single “Proxy SKU” with a Monster BOM representing Opulo’s last quarter of sales, plus a 10% factor of safety. This ensures accurate purchasing decisions based on real consumption data and a 3-month forward forecast horizon.

---

## 2. Preconditions (Must Be Completed *Before* Running Forecast)
Accurate inventory is mandatory before any forecasting run. The following must be completed weekly **before** building the Proxy SKU or running a Material Shortage Report:

### 2.1 Non-Serialized Inventory Removal  
Reference the SOP:  
[https://ohai.opulo.io/operations/managing-weekly-non-serialized-aligni-builds/
](https://ohai.opulo.io/operations/managing-weekly-non-serialized-aligni-builds/)
### 2.2 Serialized Inventory Removal  
Remove shipped serialized units (LumenPnP and Control Boxes) by finalizing their respective builds.  

### 2.3 Scrap Removal  
Remove all defective or unusable material using:  
**Inventory → Adjustments → Scrap Material**

Production must immediately report any unusual spike in scrap rates.

### 2.4 Inventory Day (Quarterly, Q1 & Q3 Only)  
Perform full inventory audit if it is the last week of an odd-numbered quarter.  
Reference the SOP:  
[https://ohai.opulo.io/operations/inventory-audit/
](https://ohai.opulo.io/operations/inventory-audit/)

After Inventory Day:  
- Update attrition multipliers per part  
- Apply adjustments to forecasting coefficients as needed  

---

## 3. Monster BOM Structure
Opulo uses **one** Proxy SKU representing all products sold in the last 3 months × 1.10.

**Source of truth calculation:**  
- Pull all sales from the last 3 months using the Coefficient Forecast Tab  
- Apply a 10% factor of safety  
- Update BOM quantities for each child item accordingly  

This Proxy SKU is the only BOM used for forecasting.

---

## 4. Weekly Forecasting Workflow

### 4.1 Update Monster BOM (Quantity Inputs)
1. Open the **Coefficient → Forecasting Tab**.  
2. Refresh last-quarter sales data.  
3. Apply **× 1.10** safety factor.  
4. Update the Monster BOM import sheet with new calculated quantities.

### 4.2 Update BOM in Aligni
1. Navigate to:  
   **[Proxy SKU] → Bill of Materials → New Revision → Import BOM**
      * Name the new revision based off the forecast week range it corresponds to
2. Import the updated BOM sheet.  
3. Confirm all part quantities match “last 3 months × 1.10”.
4. Release the new revision

---

## 5. Create a Production Build (Required Before MSR)
The Material Shortage Report must run against a **real** build entry for the Proxy SKU.

### 5.1 Create the Build
1. Navigate to:  
   **Production → Create Build**
2. Select the Proxy SKU.  
3. Set:
      - **Build Quantity:** `1`
      - **Attrition:** Enabled
      - **Drill Down:** Enabled
      - **Start Date:** Today
      - **Completion Date:** Today + 3 months

4. Click **Create Build**.

### 5.2 Allocate Material  
Inside the Build screen:

1. Click **Allocate Material**.  
2. Ensure all available stock is allocated to the build.

---

## 6. Run a Material Shortage Report

### 6.1 Run the MSR Against the 1-pcs Build
Navigate to:  

**Reports → Material Shortage Report**

Set filters to:

- **Build:** Select the active Proxy SKU build (1 pcs)

Run the report.

### 6.2 Interpret the MSR
For each child item listed:

- Identify items with **negative availability**  
- Identify items predicted to run out before the build completion date  
- Note manufacturer lead time, MOQ, historical slip, and vendor reliability  

Any item predicted to stock-out within 3 months triggers a purchase.

---

## 7. Purchasing Actions

### 7.1 Create Purchase Orders for Shortfall Items
For every part predicted to stock-out:

1. Navigate to:  
   **Purchasing → Create PO**
2. Select vendor  
3. Enter:
      - **Delivery Date** (required, must be realistic)  
      - **Quantity** (minimum = 1 quarter’s consumption, adjusted for MOQ or long lead time)  
4. Submit PO

### 7.2 Receiving Requirements
Items must be recived into inventory upon delivery

* No backdating or retroactive receipts.

---

## 8. Monthly Scrap & Corrections
Performed the first week of every month:

1. Production exports defective/scrap logs.  
2. Ops removes the materials using:  
   **Inventory → Adjustments → Scrap Material**  
3. Update scrap factors in forecasting if trending upward.  
4. Notify Engineering if scrap > 2× baseline.

---

## 9. Quarterly Inventory Day (Q1 & Q3)
Reference SOP:  
[https://ohai.opulo.io/operations/inventory-audit/
](https://ohai.opulo.io/operations/inventory-audit/)
Outputs:
- Updated attrition multipliers
- Adjusted safety factors  
- Corrections to BOM quantities  

These updates feed back into next week’s Monster BOM.

---

## 10. Exception Handling

### Vendor Lead Time Slips  
If vendor slips by >7 days:

- Update lead time in Aligni  
- Increase order buffer for next cycle  

### Scrap Spike
If scrap increases unexpectedly:

- Ops halts purchasing for that item  
- Engineering investigates failure mode  

### Repeated Over-forecasting
If MSR shows overstock:

- Re-examine sales data  
- Reduce Monster BOM quantity for that SKU