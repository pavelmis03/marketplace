"""Просто модуль для генерации кода"""

CLASS_NAME = "Partner"

SERIALIZER_TEMPLATE = """
class {0}Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = {0}
        fields = []  # TODO: insert fields!"""

VIEW_TEMPLATE = """
class {0}ViewSet(viewsets.ModelViewSet):
    queryset = {0}.objects.all()
    serializer_class = {0}Serializer
    permission_classes = [permissions.IsAuthenticated]"""


URL_ROUTER_TEMPLATE = """
router.register(r'{lower}', views.{0}ViewSet)"""


print(SERIALIZER_TEMPLATE.format(CLASS_NAME))
print(VIEW_TEMPLATE.format(CLASS_NAME))
print(URL_ROUTER_TEMPLATE.format(CLASS_NAME, lower=CLASS_NAME.lower()))
