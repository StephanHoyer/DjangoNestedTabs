from django.views.generic import TemplateView

tabs = {}

class _TabTracker(type):
    """Metaclass that tracks all subclasses that have set the _is_tab
    attribute. The classes are stored inside self._registry."""
    def __init__(cls, name, bases, attrs):
        try:
            parent_type = cls.__bases__[0].tab_type
            if parent_type not in tabs:
                tabs[parent_type] = [];
            tabs[parent_type].append(cls);
        except AttributeError:
            pass

class BaseView(TemplateView):
    tab_type = label = url_name = 'base'

    _registry = []
    template_name = 'base.html'
    __metaclass__ = _TabTracker

    def get_context_data(self, **kwargs):
        # Get base context
        context = super(BaseView, self).get_context_data()

        # Update the context with kwargs, as TemplateView doesn't do this
        context.update(kwargs)

        context['tabs'] = tabs
        context['active_tabs'] = [self.tab_type]
        for cls in self.__class__.__bases__:
            if hasattr(cls, 'tab_type'):
                context['active_tabs'].append(cls.tab_type)

        return context

    def type(self):
        return self.tab_type

class AView(BaseView):
    tab_type = label = url_name = 'a'
    template_name = 'a.html'

class AAView(AView):
    tab_type = label = url_name = 'aa'
    template_name = 'aa.html'

class ABView(AView):
    tab_type = label = url_name = 'ab'
    template_name = 'ab.html'

class BView(BaseView):
    tab_type = label = url_name = 'b'
    template_name = 'b.html'

class BAView(BView):
    tab_type = label = url_name = 'ba'
    template_name = 'ba.html'

class BBView(BView):
    tab_type = label = url_name = 'bb'
    template_name = 'bb.html'

