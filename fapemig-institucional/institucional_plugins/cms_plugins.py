from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from institucional_plugins.models import PessoaModel
from django.utils.translation import ugettext as _
from .forms import PessoaForm

@plugin_pool.register_plugin  # register the plugin
class PessoaPluginPublisher(CMSPluginBase):
    model = PessoaModel  # model where plugin data are saved
    module = _("Quem Somos")
    name = _("Pessoa Plugin")  # name of the plugin in the interface
    render_template = "quem_somos/pessoa_plugin.html"
    form =  PessoaForm

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context