from asosiy.models import *
from asosiy.serializers import *
from django.test import  TestCase


class TestQoshiqSerializer(TestCase):
    def setUp(self) -> None:
        self.qoshiqchi = Qoshiqchi.objects.create(ism="Bobo", tugilgan_yil="1995-06-23", davlat="Belgiya")
        self.albom1 = Albom.objects.create(nom="Top xit 2022", sana = "2023-02-04", rasm = "https://www.google.com/url?sa=i&url=https%3A%2F%2Ftiktok-wiki.ru%2Ftrendy%2Fpopulyarnye-pesni-iz-tik-toka-2022%2F&psig=AOvVaw3lJsgM4aYX6_Oa5NCc0wi4&ust=1689734372579000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCKClu5qdl4ADFQAAAAAdAAAAABAE", qoshiqchi=self.qoshiqchi)
        self.albom1.save()

    def test_valid_fayl(self):
        d = {"id":1, "nom": "Al by yourself", "janr": "Clasic", "albom": self.albom1.id, "fayl": "xotlar.mp3" , "davomiylik":"00:05:35"}
        serializer = QoshiqSaveSerializer(data=d)
        assert serializer.is_valid() == True
        assert True == True

    def test_invalid_fayl(self):
        d2 = {"id":1, "nom": "Al by yourself", "janr": "Clasic", "albom": self.albom1.id, "fayl": "xotlar.mp4" , "davomiylik":"00:05:35"}
        serializer = QoshiqSaveSerializer(data=d2)
        assert serializer.is_valid() == False
        assert serializer.errors.get("fayl")[0] == ".mp3 bolishi shart!"

    def test_valid_davomilik(self):
        d = {"id":1, "nom": "Al by yourself", "janr": "Clasic", "albom": self.albom1.id, "fayl": "xotlar.mp3" , "davomiylik":"00:05:35"}
        serializer = QoshiqSaveSerializer(data=d)
        assert serializer.is_valid() == True
        assert True == True

    def test_invalid_davomiylik(self):
        d2 = {"id":1, "nom": "Al by yourself", "janr": "Clasic", "albom": self.albom1.id, "fayl": "xotlar.mp3" , "davomiylik":"00:15:35"}
        serializer = QoshiqSaveSerializer(data=d2)
        assert serializer.is_valid() == False
        assert serializer.errors.get("davomiylik")[0] == "The duration should not exceed 00:07:00."