# Manufacturing Operations

Manufacturing at Opulo is broken into three main parts:

- **Sourcing**: Ordering inventory, tracking inventory, communicating with vendors, removing inventory as builds complete.
- **Production**: Deciding what should get built this week, building product, performing QC checks
- **Fulfillment**: Packing individual orders, printing labels, handling customs

[**CLICK TO VIEW MANUFACTURING STRUCTURE DIAGRAM**](https://app.diagrams.net/#G1W1miMUE59fZ-qFedDb_wN7-9yU5UW_Mv)

The weekly flow is structured as follows:

``` mermaid
---
config:
  logLevel: 'debug'
  theme: 'neutral'
  timeline:
    disableMulticolor: true
  themeVariables:
    cScale0: '#000000'
    cScale1: '#000000'
    cScale2: '#000000'
    cScale3: '#000000'
    cScale4: '#000000'
---

timeline
    title One Week in Opulo Manufacturing
    section Monday
      Sourcing : Weekly Inventory Removal for last weeks build, plus any extra/ replacement parts that were not part of the Build List
               : Sourcing Manager makes `BATCH-0001` build in Aligni based on Build List from Production Manager last week, scheduled completion this Friday
               : Sourcing Manager provides Build number for Production to use for serial numbers
               : Purchase Forecasting is run with `BATCH-0002` based on Shopify export of last 90 days of sales.
               : Purchasing for any short items begins.
      Production : Build begins
    section Tuesday
      Production    : Build continues
    section Wednesday
      Production    : Build continues
    section Thursday
      Production    : Build continues
    section Friday
      Production    : This week build completes, packout begins
                    : Production Manager generates next week's Build List (either from ShipStation or their brain, depending on if we're ahead or behind)

```

While we have a lead time, we treat production and fulfillment as one branch, because they happen together and need to inform each other. Whatever gets built in a week also gets shipped that week.

Without a lead time and with inventory on the shelf, production just provides finished stock to a shelf awaiting packout. Fulfillment is then just reacting to orders as they come in.

This section of OHAI has SOPs for each of these sections of Manufacturing.