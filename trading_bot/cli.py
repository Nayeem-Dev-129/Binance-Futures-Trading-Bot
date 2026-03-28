import argparse
import logging

from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger


def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", required=False, help="Price for LIMIT order")

    args = parser.parse_args()

    try:
        # Validate input
        validate_order(args.symbol, args.side, args.type, args.quantity, args.price)

        # Create client
        client = get_client()

        print("\n📌 Order Request Summary")
        print("------------------------")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")
        if args.type == "LIMIT":
            print(f"Price    : {args.price}")

        # Place order
        response = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )
        print("\n✅ Order Successful!")
        print("------------------------")
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print(f"Avg Price     : {response.get('avgPrice')}")
        order_id = response.get("orderId")

        updated_order = client.futures_get_order(
            symbol=args.symbol,
            orderId=order_id
        )

        print("\n📊 Updated Order Status:")
        print(f"Status        : {updated_order.get('status')}")
        print(f"Executed Qty  : {updated_order.get('executedQty')}")
        print(f"Avg Price     : {updated_order.get('avgPrice')}")
    except Exception as e:
        print("\n❌ Order Failed!")
        print("Error:", str(e))


if __name__ == "__main__":
    main()