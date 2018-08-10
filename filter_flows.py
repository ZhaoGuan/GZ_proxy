# -*- coding: utf-8 -*-
# __author__ = 'Gz'
from mitmproxy import flowfilter
from mitmproxy import ctx, http


class Filter:
    # def __init__(self):
    #     self.filter: flowfilter.TFilter = '~http'

    # def configure(self, updated):
    #     self.filter = flowfilter.parse(ctx.options.flowfilter)
    #
    # def load(self, l):
    #     l.add_option(
    #         "flowfilter", str, "", "Check that flow matches filter."
    #     )

    def response(self, flow: http.HTTPFlow) -> None:
        print(flow.request.url)
        # match = flowfilter.match('!(~u kika)', flow)
        match = flowfilter.match(None, flow)
        print(match)
        if match:
            print('!!!!!!!!!!!!!!!!!')
            # ctx.log.info("Flow matches filter:")
            # ctx.log.info(flow)
            print(flow.request.url)
            print('!!!!!!!!!!!!!!!!!')
        elif match == None:
            pass


addons = [Filter()]
