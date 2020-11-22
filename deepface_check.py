
from deepface import DeepFace

obj = DeepFace.analyze(r"static\uploads\sai_3.jpg")

print(type(obj))
#objs = DeepFace.analyze(["img1.jpg", "img2.jpg", "img3.jpg"]) #analyzing multiple faces same time
print( int(obj["age"])," years old ",obj["dominant_race"]," ",obj["dominant_emotion"]," ", obj["gender"])

