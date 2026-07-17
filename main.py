import math

def calculate_marketplace_earnings(gross_sales_usd, marketplace_config, exchange_rate_usd_to_local):
    """
    Calculates net earnings for a given marketplace and gross sales,
    including commission, tax, and currency conversion.
    """
    marketplace_name = marketplace_config['name']
    commission_rate = marketplace_config['commission_rate']
    tax_rate = marketplace_config['tax_rate']
    payout_threshold_usd = marketplace_config['payout_threshold_usd']

    # 1. Calculate commission: This is the fee the marketplace takes from gross sales.
    commission_amount_usd = gross_sales_usd * commission_rate
    earnings_after_commission_usd = gross_sales_usd - commission_amount_usd

    # 2. Calculate tax: Applied to the earnings after commission, as often seen in practice.
    tax_amount_usd = earnings_after_commission_usd * tax_rate
    net_earnings_usd = earnings_after_commission_usd - tax_amount_usd

    # 3. Check against payout threshold: Marketplaces often have a minimum amount
    # a vendor must earn before funds are disbursed. Funds might be held if below.
    payout_status = "Eligible for payout"
    if net_earnings_usd < payout_threshold_usd:
        payout_status = f"Below payout threshold (${payout_threshold_usd:.2f})"
        # For simplicity, we still show the calculated net, but flag it.
        # In a real system, funds might be rolled over to the next period or held.

    # 4. Convert to local currency: Addresses currency fluctuation complexity.
    # In a real application, this exchange rate would be fetched dynamically.
    net_earnings_local = net_earnings_usd * exchange_rate_usd_to_local

    return {
        "marketplace": marketplace_name,
        "gross_sales_usd": gross_sales_usd,
        "commission_rate": commission_rate,
        "tax_rate": tax_rate,
        "payout_threshold_usd": payout_threshold_usd,
        "commission_amount_usd": commission_amount_usd,
        "tax_amount_usd": tax_amount_usd,
        "net_earnings_usd": net_earnings_usd,
        "net_earnings_local": net_earnings_local,
        "payout_status": payout_status
    }

if __name__ == "__main__":
    # --- Configuration ---
    # Define different software marketplaces with their specific parameters
    marketplaces = [
        {
            "name": "App Store (iOS)",
            "commission_rate": 0.30,  # Example: 30% commission
            "tax_rate": 0.05,         # Example: 5% tax on net after commission
            "payout_threshold_usd": 150.00 # Example: Minimum payout threshold
        },
        {
            "name": "Google Play Store",
            "commission_rate": 0.15,  # Example: 15% commission (for subscriptions/small developers)
            "tax_rate": 0.08,         # Example: 8% tax
            "payout_threshold_usd": 100.00
        },
        {
            "name": "Envato Market",
            "commission_rate": 0.50,  # Example: High commission for exclusive authors
            "tax_rate": 0.10,         # Example: 10% tax
            "payout_threshold_usd": 50.00
        },
        {
            "name": "Gumroad",
            "commission_rate": 0.09,  # Example: 9% + $0.30 per transaction (simplified to just %)
            "tax_rate": 0.00,         # Example: No direct tax from Gumroad, vendor handles
            "payout_threshold_usd": 10.00
        }
    ]

    # Assume a fixed exchange rate for demonstration purposes (e.g., USD to Turkish Lira).
    # In a real application, this would be fetched from a reliable currency API.
    USD_TO_LOCAL_EXCHANGE_RATE = 32.50 # Example: 1 USD = 32.50 Turkish Lira (TRY)
    LOCAL_CURRENCY_NAME = "TRY"

    # --- Simulation ---
    # Gross sales amount in USD for which to calculate earnings
    gross_sales_amount_usd = 250.00

    print(f"--- Software Vendor Earnings Calculator ---")
    print(f"Gross Sales to Analyze: ${gross_sales_amount_usd:.2f}")
    print(f"USD to {LOCAL_CURRENCY_NAME} Exchange Rate: 1 USD = {USD_TO_LOCAL_EXCHANGE_RATE:.2f} {LOCAL_CURRENCY_NAME}\n")

    for mp_config in marketplaces:
        results = calculate_marketplace_earnings(
            gross_sales_amount_usd,
            mp_config,
            USD_TO_LOCAL_EXCHANGE_RATE
        )

        print(f"Marketplace: {results['marketplace']}")
        print(f"  - Commission ({results['commission_rate']:.0%}): ${results['commission_amount_usd']:.2f}")
        print(f"  - Tax ({results['tax_rate']:.0%}): ${results['tax_amount_usd']:.2f}")
        print(f"  - Net Earnings (USD): ${results['net_earnings_usd']:.2f} ({results['payout_status']})")
        print(f"  - Net Earnings ({LOCAL_CURRENCY_NAME}): {results['net_earnings_local']:.2f} {LOCAL_CURRENCY_NAME}\n")

    print("------------------------------------------")
    print("This simulation highlights how varying marketplace policies")
    print("impact a vendor's final earnings and the complexity of calculation.")
