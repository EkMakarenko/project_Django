
class ImageService:

    @staticmethod
    def update_image(serializer, instance, request):
        if serializer.is_valid(raise_exception=True):
            instance.image.delete(save=True)
            instance.image = request.data['image']
