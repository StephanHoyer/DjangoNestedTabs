from django.views.generic import TemplateView

tabs = {}

class _TabTracker(type):
    """Metaclass that tracks all subclasses that have set the _is_tab
    attribute. The classes are stored inside self._registry."""
    def __init__(cls, name, bases, attrs):
        parent_classname = cls.__bases__[0].__name__
        if parent_classname not in tabs:
            tabs[parent_classname] = [];
        tabs[parent_classname].append(cls);

class BaseView(TemplateView):

    _registry = []
    template_name = 'base.html'
    __metaclass__ = _TabTracker

    def get_context_data(self, **kwargs):
        """Add tab information to context. To retrieve list of all group tab
        instances, use ``{{ tabs }}`` in your template."""

        # Get base context
        context = super(BaseView, self).get_context_data()

        # Update the context with kwargs, as TemplateView doesn't do this
        context.update(kwargs)

        context['tabs'] = tabs
        context['active_tabs'] = [self.__class__] + \
                                 list(self.__class__.__bases__)

        return context

    def type(self):
        return self.__class__

class AView(BaseView):
    template_name = 'a.html'
    label = 'a'
    url_name = 'a'

class AAView(AView):
    template_name = 'aa.html'
    label = 'aa'
    url_name = 'aa'

class ABView(AView):
    template_name = 'ab.html'
    label = 'ab'
    url_name = 'ab'


class BView(BaseView):
    template_name = 'b.html'
    label = 'b'
    url_name = 'b'


