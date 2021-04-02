class TemplateMessages:
    def __init__(self):
        pass

    @staticmethod
    def get_increase_message(
        price_usd: float, price_eur: float, percentage: str
    ) -> str:
        return (
            f"APPC TO THE MOON!!! :rocket: :rocket: \n"
            f"({TemplateMessages.get_price_message(price_usd, price_eur, percentage)})\n"
            f"https://www.youtube.com/watch?v=V1CsOkcfVeo"
        )

    @staticmethod
    def get_decrease_message(
        price_usd: float, price_eur: float, percentage: str
    ) -> str:
        return (
            f"STONKS ONLY GO UP!!! "
            f"<:stonks:821467993141542932> "
            f"<:stonks:821467993141542932> \n"
            f"({TemplateMessages.get_price_message(price_usd, price_eur, percentage)})\n"
            f"https://www.youtube.com/watch?v=Kdmg1FZHPTA"
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

    @staticmethod
    def get_ping_message() -> str:
        return "Pong! :ping_pong:"
