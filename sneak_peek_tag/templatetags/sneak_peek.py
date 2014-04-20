from django.template import Library, Node

register = Library()

@register.tag(name="sneak_peek")
def sneak_peek(parser, token):
    tag = None
    style = 'default'
    try:
        tag, style = token.split_contents()
    except ValueError:
        pass
    nodelist = parser.parse(('endsneak_peek',))
    parser.delete_first_token()
    return SneakPeekWrapper(nodelist, style)


class SneakPeekWrapper(Node):
    def __init__(self, nodelist, style):
        self.nodelist = nodelist
        self.style = style

    def render(self, context):
        user = context['user']
        user_is_blessed = user.has_perm('sneak_peek_tag.can_view_sneak_peek')

        if user_is_blessed:
            content = self.nodelist.render(context)
            wrapped_hidden_feature = """<div class="sneak-peek %s">
                	%s
                </div>""" % (self.style, content)
            return wrapped_hidden_feature
        else:
            return ''
