from django.http import Http404, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.utils.http import urlquote
from django.views.generic import DetailView

# from oscar.apps.catalogue.signals import product_viewed
from apps.catalogue.models import Market


# class MarketDetailView(DetailView):
#     context_object_name = 'магазин'
#     model = Market
#     # view_signal = product_viewed
#     template_folder = "catalogue"
#
#     # Whether to redirect to the URL with the right path
#     enforce_paths = True
#
#     # Whether to redirect child products to their parent's URL. If it's disabled,
#     # we display variant product details on the separate page. Otherwise, details
#     # displayed on parent product page.
#     enforce_parent = False
#
#     def get(self, request, **kwargs):
#         """
#         Ensures that the correct URL is used before rendering a response
#         """
#         self.object = market = self.get_object()
#
#         redirect = self.redirect_if_necessary(request.path, market)
#         if redirect is not None:
#             return redirect
#
#         # Do allow staff members so they can test layout etc.
#         if not self.is_viewable(market, request):
#             raise Http404()
#
#         response = super().get(request, **kwargs)
#         # self.send_signal(request, response, market)
#         return response
#
#     def is_viewable(self, market, request):
#         return market.is_public or request.user.is_staff
#
#     def get_object(self, queryset=None):
#         # Check if self.object is already set to prevent unnecessary DB calls
#         if hasattr(self, 'object'):
#             return self.object
#         else:
#             return super().get_object(queryset)
#
#     def redirect_if_necessary(self, current_path, market):
#         if self.enforce_parent and market.is_child:
#             return HttpResponsePermanentRedirect(
#                 market.parent.get_absolute_url())
#
#         if self.enforce_paths:
#             expected_path = market.get_absolute_url()
#             if expected_path != urlquote(current_path):
#                 return HttpResponsePermanentRedirect(expected_path)
#
#     def get_context_data(self, **kwargs):
#         ctx = super().get_context_data(**kwargs)
#         # ctx['alert_form'] = self.get_alert_form()
#         # ctx['has_active_alert'] = self.get_alert_status()
#         return ctx
#
#     # def get_alert_status(self):
#     #     # Check if this user already have an alert for this product
#     #     has_alert = False
#     #     if self.request.user.is_authenticated:
#     #         alerts = ProductAlert.objects.filter(
#     #             product=self.object, user=self.request.user,
#     #             status=ProductAlert.ACTIVE)
#     #         has_alert = alerts.exists()
#     #     return has_alert
#     #
#     # def get_alert_form(self):
#     #     return ProductAlertForm(
#     #         user=self.request.user, product=self.object)
#     #
#     # def send_signal(self, request, response, market):
#     #     self.view_signal.send(
#     #         sender=self, market=market, user=request.user, request=request,
#     #         response=response)
#
#     def get_template_names(self):
#         """
#         Return a list of possible templates.
#
#         If an overriding class sets a template name, we use that. Otherwise,
#         we try 2 options before defaulting to catalogue/detail.html:
#             1). detail-for-upc-<upc>.html
#             2). detail-for-class-<classname>.html
#
#         This allows alternative templates to be provided for a per-product
#         and a per-item-class basis.
#         """
#         if self.template_name:
#             return [self.template_name]
#
#         return [
#             'oscar/%s/detail-for-upc-%s.html' % (
#                 self.template_folder, self.object.upc),
#             'oscar/%s/detail-for-class-%s.html' % (
#                 self.template_folder, self.object.get_product_class().slug),
#             'oscar/%s/detail.html' % self.template_folder]

def market_view(request, slug):
    print(slug)
    return render(request, 'market.html')
