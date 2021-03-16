class TemplateMessages:
    def __init__(self):
        pass

    @staticmethod
    def get_increase_message(percentage: str) -> str:
        return (
            f"APPC TO THE MOON!!! :rocket: :rocket: "
            f"\n\n(price change: {percentage})"
        )

    @staticmethod
    def get_decrease_message(percentage: str) -> str:
        return (
            f"STONKS ONLY GO UP!!! "
            f":stonks:821467993141542932 "
            f":stonks:821467993141542932"
            f"\n\n(price change: {percentage})"
        )

    @staticmethod
    def get_price_message(price_usd: float, price_eur: float, percentage: str) -> str:
        return (
            f"Current price is: {price_usd:.8f}$ / {price_eur:.8f}€ \n"
            f"Changed {percentage} in the last 24h"
        )

    @staticmethod
    def get_failure_message() -> str:
        return "Failed to get current APPC stats. Try again later. :poop:"
