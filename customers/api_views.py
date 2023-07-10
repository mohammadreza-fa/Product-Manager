class SerialDetail(DestroyModelMixin, RetrieveAPIView):
    """
        Detail of User for Managers
    """
    serializer_class = SerialSerializer
    queryset = Serial.objects.all()
    lookup_field = 'serial'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.usage += 1

        if instance.usage == 5:
            return self.destroy(request, *args, **kwargs)

        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

