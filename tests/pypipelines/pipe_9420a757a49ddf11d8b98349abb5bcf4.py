# Pipe pipe_9420a757a49ddf11d8b98349abb5bcf4 generated by pipe2py

from pipe2py import Context
from pipe2py.modules.pipeforever import pipe_forever
from pipe2py.modules.pipefetchpage import pipe_fetchpage
from pipe2py.modules.pipetruncate import pipe_truncate
from pipe2py.modules.pipeoutput import pipe_output


def pipe_9420a757a49ddf11d8b98349abb5bcf4(context=None, _INPUT=None, conf=None, **kwargs):
    # todo: insert pipeline description here
    conf = conf or {}

    if context and context.describe_input:
        return []

    if context and context.describe_dependencies:
        return [u'pipefetchpage', u'pipeoutput', u'pipetruncate']

    forever = pipe_forever()

    sw_266 = pipe_fetchpage(
        context, forever, conf={'URL': {'type': 'url', 'value': 'file://data/www.caltrain.com_Fares_farechart.html'}, 'to': {'type': 'text', 'value': '</tr>'}, 'token': {'type': 'text', 'value': '<td style="TEXT-ALIGN: center">'}, 'from': {'type': 'text', 'value': 'One Way</span>'}})
    
    sw_287 = pipe_truncate(
        context, sw_266, conf={'count': {'type': 'number', 'value': '100'}})
    
    _OUTPUT = pipe_output(
        context, sw_287, conf=None)
    
    return _OUTPUT


if __name__ == "__main__":
    pipeline = pipe_9420a757a49ddf11d8b98349abb5bcf4(Context())

    for i in pipeline:
        print i