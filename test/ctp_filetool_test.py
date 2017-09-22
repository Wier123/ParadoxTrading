import logging

from ParadoxTrading.Utils.CTP.CTPFIleTradeTool import CTPFileTradeTool

logging.basicConfig(level=logging.INFO)

tool = CTPFileTradeTool(
    'config.ini', 'order.csv', 'fill.csv',
    _retry_time=1
)
tool.tradeFunc()