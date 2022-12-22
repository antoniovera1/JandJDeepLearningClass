from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from tensorflow.keras.models import load_model

from .models import Car
from .serializers import CarSerializer, HorsePowerSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_serializer_class(self):
        if self.action == "predict_mpg":
            return HorsePowerSerializer

        return super().get_serializer_class()

    @action(detail=False, methods=['post'])
    def predict_mpg(self, request):
        # For images
        # request.files
        # classes = model.predict([image])
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        model = load_model("assets/machine_learning/mpg_model")
        mpg_pred = model.predict([[serializer.data['horse_power']]])[0][0]


        return Response({"mpg": mpg_pred})
