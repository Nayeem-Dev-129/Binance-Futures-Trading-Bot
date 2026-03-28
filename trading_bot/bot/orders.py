import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Request -> {symbol} {side} {order_type} qty={quantity} price={price}")

        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(f"Response -> {response}")

        return response

    except Exception as e:
        logging.error(f"Error -> {str(e)}")
        raise