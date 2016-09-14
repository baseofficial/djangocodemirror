"""
Tests against template tags for Codemirror config
"""
import json
import pytest

from djangocodemirror.widgets import CodeMirrorWidget
from djangocodemirror.templatetags.djangocodemirror_tags import codemirror_field_js_assets

from project.forms import SampleForm, ManyFieldsSampleForm


def test_codemirror_single_field_js_assets():
    """Test codemirror_field_js_assets tag for a single field"""
    f = SampleForm({'foo': 'bar'})

    f.as_p()

    assets = codemirror_field_js_assets(f.fields['foo'])

    assert assets == ("""<script type="text/javascript" src="/static/CodeMirror/lib/codemirror.js"></script>\n"""
                      """<script type="text/javascript" src="/static/CodeMirror/mode/restructuredtext/restructuredtext.js"></script>""")


def test_codemirror_multiple_field_js_assets():
    """Test codemirror_field_js_assets tag for many fields"""
    f = ManyFieldsSampleForm({'foo': 'bar'})

    f.as_p()

    assets = codemirror_field_js_assets(
        f.fields['foo'],
        f.fields['pika'],
        f.fields['ping']
    )

    assert assets == ("""<script type="text/javascript" src="/static/CodeMirror/lib/codemirror.js"></script>\n"""
                      """<script type="text/javascript" src="/static/CodeMirror/lib/util/dialog.js"></script>\n"""
                      """<script type="text/javascript" src="/static/CodeMirror/lib/util/search.js"></script>\n"""
                      """<script type="text/javascript" src="/static/CodeMirror/lib/util/searchcursor.js"></script>\n"""
                      """<script type="text/javascript" src="/static/CodeMirror/mode/restructuredtext/restructuredtext.js"></script>\n"""
                      """<script type="text/javascript" src="/static/CodeMirror/mode/python/python.js"></script>\n"""
                      """<script type="text/javascript" src="/static/CodeMirror/mode/css/css.js"></script>""")
