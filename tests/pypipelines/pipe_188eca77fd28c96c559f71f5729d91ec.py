# Pipe pipe_188eca77fd28c96c559f71f5729d91ec generated by pipe2py

from pipe2py import Context
from pipe2py.modules.pipeforever import pipe_forever
from pipe2py.modules.pipefetchpage import pipe_fetchpage
from pipe2py.modules.pipeitembuilder import pipe_itembuilder
from pipe2py.modules.pipeloop import pipe_loop
from pipe2py.modules.pipetruncate import pipe_truncate
from pipe2py.modules.pipeoutput import pipe_output


def pipe_188eca77fd28c96c559f71f5729d91ec(context=None, _INPUT=None, conf=None, **kwargs):
    # todo: insert pipeline description here
    conf = conf or {}

    if context and context.describe_input:
        return []

    if context and context.describe_dependencies:
        return [u'pipefetchpage', u'pipeitembuilder', u'pipeloop', u'pipeoutput', u'pipetruncate']

    forever = pipe_forever()

    # We need to wrap submodules (used by loops) so we can pass the
    # input at runtime (as we can to subpipelines)
    def pipe_sw_119(context=None, _INPUT=None, conf=None, **kwargs):
        # todo: insert submodule description here
        return pipe_fetchpage(
            context, _INPUT, conf={'URL': {'type': 'url', 'subkey': 'url'}, 'to': {'type': 'text', 'value': '</tr>'}, 'token': {'type': 'text', 'value': '<td style="TEXT-ALIGN: center">'}, 'from': {'type': 'text', 'value': 'One Way</span>'}})
    
    sw_163 = pipe_itembuilder(
        context, forever, conf={'attrs': {'value': {'type': 'text', 'value': 'file://data/www.caltrain.com_Fares_farechart.html'}, 'key': {'type': 'text', 'value': 'url'}}})
    
    sw_111 = pipe_loop(
        context, sw_163, embed=pipe_sw_119, conf={'assign_part': {'type': 'text', 'value': 'all'}, 'assign_to': {'type': 'text', 'value': 'loop:fetchpage'}, 'emit_part': {'type': 'text', 'value': 'all'}, 'mode': {'type': 'text', 'value': 'EMIT'}, 'embed': {'type': 'module', 'value': {'type': 'fetchpage', 'id': 'sw-119', 'conf': {'URL': {'type': 'url', 'subkey': 'url'}, 'to': {'type': 'text', 'value': '</tr>'}, 'token': {'type': 'text', 'value': '<td style="TEXT-ALIGN: center">'}, 'from': {'type': 'text', 'value': 'One Way</span>'}}}}, 'with': {'type': 'text', 'value': ''}})
    
    sw_287 = pipe_truncate(
        context, sw_111, conf={'count': {'type': 'number', 'value': '100'}})
    
    _OUTPUT = pipe_output(
        context, sw_287, conf=None)
    
    return _OUTPUT


if __name__ == "__main__":
    pipeline = pipe_188eca77fd28c96c559f71f5729d91ec(Context())

    for i in pipeline:
        print i