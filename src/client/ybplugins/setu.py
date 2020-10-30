from typing import Any, Dict, Union

from aiocqhttp.api import Api
from .web_util import rand_string


class Setu:
    def __init__(self,
                 glo_setting: Dict[str, Any],
                 bot_api: Api,
                 *args, **kwargs):
        self.setting = glo_setting
        self.api = bot_api
        self.verification = {}

    async def execute_async(self, ctx: Dict[str, Any]):
        cmd = ctx['raw_message']
        if cmd.startswith('色图'):
            if ctx['message_type'] != 'group':
                return '此功能仅可用于群聊'
            await self.api.send_group_msg(
                group_id=ctx['group_id'],
                message='色图发送测试',
            )
