from dataclasses import dataclass

from common.config import settings
from common.utils.shyft import ShyftAPI
from common.utils.utils import format_number


@dataclass
class HoldingToken:
    mint: str
    balance: float
    balance_str: str  # 带有单位的余额
    symbol: str
    # usd_value: float
    # price: float
    # total_profit: float = 0
    # total_profit_pnl: float = 0
    # last_active_timestamp: int | None = None


@dataclass
class TokenAccountBalance:
    balance: float
    decimals: int


# PERF: 暂时每次获取都调用 API，后续可以优化
class HoldingService:
    def __init__(self) -> None:
        self.shyft = ShyftAPI(settings.api.shyft_api_key)

    async def get_token_account_balance(
        self, mint: str, wallet: str
    ) -> TokenAccountBalance:
        """获取代币账户余额

        Args:
            token_mint (str): 代币地址
            owner (str): 持有者地址

        Returns:
            TokenAccountBalance: 代币账户余额
        """
        balance, decimals = await self.shyft.get_token_balance(mint, wallet)
        return TokenAccountBalance(balance=balance, decimals=decimals)

    async def get_tokens(
        self,
        wallet: str,
        hidden_small_amount: bool = False,
    ) -> list[HoldingToken]:
        """获取持有的 Token 列表

        Args:
            hidden_small_amount (bool, optional): 是否隐藏小额 Token. Defaults to False.

        """
        all_tokens = await self.shyft.get_all_tokens(wallet)
        if hidden_small_amount:
            all_tokens = [token for token in all_tokens if token["balance"] > 0]

        return [
            HoldingToken(
                mint=token["address"],
                balance=token["balance"],
                balance_str=format_number(token["balance"]),
                symbol=token["info"]["symbol"],
                # usd_value=token["info"]["current_supply"] * token["info"]["price"],
                # price=token["info"]["price"],
            )
            for token in all_tokens
        ]
