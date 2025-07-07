# Inventory Day SOP

## Glossary

- **Ghidra** – LumenPnP production room  
- **Thunderbird** – Inventory room  
- **Mendel** – SMT assembly line  
- **Tequila Sunrise** – Feeder Assembly Line #1  
- **Docker** – Feeder Assembly Line #2
- **Aligni** - Opulo's MRP (Material Resource Planner) used for purchasing of stock, production lot planning, and inventory management

## Preflight checklist

Before inventory day begins, complete the following preparatory steps to ensure an accurate and efficient audit:

- **Receive all shipments**  
  Ensure all incoming shipments delivered to HQ have been received into Aligni. This includes both parts and consumables.

- **Enter retroactive purchases**  
  Manually enter any parts or materials acquired via Amazon, McMaster-Carr, or similar vendors that were not tracked through a formal purchase order.

- **Review zero-quantity parts**  
  Open the `Aligni All Inventory` report (Reports → Inventory → All Inventory) and filter for items showing a **quantity of zero**.  
  Cross-reference against physical stock at HQ.  
  - If a part is physically present but shows zero in Aligni, create a placeholder entry:
    - Quantity: `1`
    - Cost: `$0.00`
    - Lot code: `"placeholder"`
  - This ensures the item is flagged for audit without affecting financial reporting or triggering restock alerts.

## Inventory management tasks

During the inventory count, complete the following cleanup and organization work:

- **Consolidate small hardware**  
  Transfer all loose bolts, nuts, washers, etc., from small bins in **Ghidra** (LumenPnP room), **Tequila Sunrise**, and **Docker** (Feeder assembly stations) into the appropriate categorized bins in **Thunderbird** (Inventory room).

- **Standardize part locations**  
  Group like parts together and consolidate duplicate storage locations.
  Limit each part to as few open bins as possible to improve traceability.

- **Label bins and update lot codes**  
  Confirm that all bins and storage locations are clearly labeled with part numbers.  
  Replace faded, handwritten, or missing labels to ensure accuracy during audit.

## Dealing with in-progress builds

To maintain inventory accuracy, handle active builds before the audit begins:

- **Finalize completed builds**  
  If a build is physically complete, mark it as **finalized** in Aligni and move it to the pack-out shelf.  
  Ensure all used components have been deducted from inventory.

- **Close open builds before inventory**  
  All work-in-progress builds must be finalized prior to starting inventory day.

---

## Day-of inventory audit procedure

On inventory day, each team member will be assigned one or more part categories, each corresponding to a pre-created adjustment batch in Aligni. The goal is to confirm physical inventory against Aligni records and correct any discrepancies.

### 1. Open your assigned inventory batch

- Go to Aligni → **Inventory Adjustment Batches**
- Locate the batch for your assigned category (e.g., “Switches – June 2025 Inventory Sync”)
- Click into the batch to begin

### 2. Import the part collection

- Click **“Add Parts”**
- Select the correct **Part Collection** (should match the batch title)
- Leave the "Inventory Sublocation" blank
- Click **Add Parts**

> ⚠️ You can only import up to 250 items per batch. If a batch doesn’t show all `Asset IDs` for a given part, this may be the cause.

### 3. Perform the physical count

For each part and lot:

- Compare Aligni’s listed quantity to what is physically present
- In the `Final Qty` column:
  - Enter the **corrected quantity** if there’s a mismatch
  - Leave the value unchanged if the inventory is correct
  - Enter `0` for lots that do not physically exist

> 💡 If you find unlabeled, duplicate, or mixed bins, consolidate them and notify the inventory lead.  
> ℹ️ Some bins may contain multiple lots combined for space efficiency. If this makes it impractical to split counts by `Asset ID`, estimate each lot's quantity as best you can—what matters most is that the **total count across lots reflects our real stock**.

### 4. Submit the adjustment

- Once all quantities in your batch are reviewed:
  - Double-check for any obvious mistakes
  - Click **Submit Adjustments** (Do *not* finalize)
  - The batch will be sent to Lucy for final review and commit

> ✅ Do not delete lines or create new entries—adjust only what’s already listed.

---

### Audit support & troubleshooting

Notify the inventory lead if:

- A part exists physically but isn’t listed in Aligni
- You encounter bins with no labels, wrong labels, or ambiguous part numbers
- A bin contains mixed parts
- You aren’t sure what a part is or can’t determine its `Part Number`

---

## Post-audit procedure

After all counts are submitted, inventory is finalized before normal operations resume.

### 1. Review submitted batches

- Lucy will review each submitted batch:
  - Look for inconsistencies or unusual quantities
  - Follow up on any questionable entries
  - Ensure no batches were prematurely finalized

- If corrections are needed:
  - Reopen the batch
  - Coordinate with the original counter
  - Resubmit after resolving issues

### 2. Finalize adjustments

- Once reviewed, batches will be **finalized and committed** in Aligni
- Finalized records become the new official inventory baseline

### 3. Resume production

- Once **all batches are finalized**, material consumption and production may resume
- Lucy will notify the production team that **inventory lockdown is lifted**

> ⚠️ No material should be consumed between the start of inventory and the finalization of all adjustments.  