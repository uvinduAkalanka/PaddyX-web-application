import os
from uuid import uuid4
from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

classes = ['armyworm', 'brownSpot', 'Hispa', 'Healthy', 'grassHopper', 'leafBlast', 'sheath blight', 'tungro']


@app.route('/')
def index():  # put application's code here
    # return render_template('index.html')
    return render_template('welcome.html')


@app.route('/home')
def go_home():  # put application's code here
    return render_template('index.html')


@app.route("/upload", methods = ["POST"])
def upload():  # put application's code here'

    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)
        import tensorflow as tf
        import numpy as np
        from keras.preprocessing import image

        from keras.models import load_model
        new_model = load_model('sdgpModel.h5')
        new_model.summary()
        test_image = image.load_img('images\\' + filename, target_size = (64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = new_model.predict(test_image)
        result1 = result[0]
        text_position = 0
        for i in range(8):
            text_position = i
            if result1[i] == 1.:
                break;
        prediction = classes[i]
        topic = ""
        des1 = ""
        des2 = ""
        des3 = ""
        des4 = ""
        des5 = ""

        if text_position == 0:
            topic = ""
            des1 = "Armyworms are caterpillars that attack rice. There are at least three species of armyworm which " \
                   "attack rice in Asia. These are the rice swarming caterpillar, common cutworm, and the rice " \
                   "ear-cutting caterpillar "
            des2 = "Armyworm feeds on rice by cutting off leaves and young seedlings at the plant's base. They can " \
                   "also cut off rice panicles from the base. "
            des3 = "Adult armyworms survive better and produce more eggs when the temperature is at 15°C maximum, " \
                   "and when plants are naturally fertilized. Periods of drought followed by heavy rains, " \
                   "and the presence of alternate hosts also sustain the development of armyworms. "
            des4 = "The larvae usually feed in the upper portion of the rice canopy on cloudy days or at night; while " \
                   "the adult feeds, mates, and migrates at night and rests in daytime at the base of the plant. "
            des5 = "In dryland fields, armyworm pupa can be found in the soil or at the base of the rice plants. In " \
                   "wetlands, they pupate on the plants or on grassy areas along the field borders. "
        elif text_position == 1:
            topic = ""
            des1 = "Brown spot has been historically largely ignored as one of the most common and most damaging rice " \
                   "diseases. "
            des2 = "Brown spot is a fungal disease that infects the coleoptile, leaves, leaf sheath, " \
                   "panicle branches, glumes, and spikelets. "
            des3 = "Its most observable damage is the numerous big spots on the leaves which can kill the whole leaf. " \
                   "When infection occurs in the seed, unfilled grains or spotted or discolored seeds are formed. "
            des4 = "The disease can develop in areas with high relative humidity (86−100%) and temperatures between " \
                   "16 and 36°C. It is common in unflooded and nutrient-deficient soil, or in soils that accumulate " \
                   "toxic substances. "
            des5 = "For infection to occur, the leaves must be wet for 8−24 hours."
        elif text_position == 2:
            topic = ""
            des1 = "Rice hispa scrapes the upper surface of leaf blades leaving only the lower epidermis."
            des2 = "It also tunnels through the leaf tissues. When damage is severe, plants become less vigorous."
            des3 = "The presence of grassy weeds in and near rice fields as alternate hosts harbor and encourages the " \
                   "pest to develop. The heavily fertilized field also encourages damage. "
            des4 = "Heavy rains, especially in pre monsoon or earliest monsoon periods, followed by abnormally low " \
                   "precipitation, minimum day-night temperature differential for a number of days, and high RH are " \
                   "favorable for the insect’s abundance. "
            des5 = "The rice hispa is common in rainfed and irrigated wetland environments and is more abundant " \
                   "during the rainy season. "
        elif text_position == 3:
            topic = ""
            des1 = "This is healthy paddy leaf "
            des2 = ""
            des3 = ""
            des4 = ""
            des5 = ""
        elif text_position == 4:
            topic = " Desciption Grass Hopper"
            des1 = "Short-horned grasshopper and Oriental migratory locust both infest the rice plant and have similar "
            des2 = "Feeding damage caused by short-horned grasshoppers and oriental migratory locusts results to cut " \
                   "out areas on leaves and cut-off panicles. They both feed on leaf margins. "
            des3 = "Aquatic environments are suitable for the development of short-horned grasshoppers, while locusts " \
                   "may prefer dry environments. Both are favored by the presence of alternate hosts. "
            des4 = "The short-horned grasshoppers are common in moist and swampy areas. These nocturnal insect pests " \
                   "are abundant during September and October. "
            des5 = "Oriental migratory locusts are commonly found in all rice environments, but they are more " \
                   "concentrated in rainfed areas. They dominate the irrigated rice environment surrounded by "
        elif text_position == 5:
            topic = ""
            des1 = "Blast is caused by the fungus Magnaporthe oryzae. It can affect all above-ground parts of a rice " \
                   "plant: leaf, collar, node, neck, parts of panicle, and sometimes leaf sheath. "
            des2 = "It occurs in areas with low soil moisture, frequent and prolonged periods of rain showers, " \
                   "and cool temperature in the daytime. In upland rice, large day-night temperature differences that " \
                   "cause dew formation on leaves and overall cooler temperatures favor the development of the " \
                   "disease. "
            des3 = "Rice can have blast in all growth stages. However, leaf blast incidence tends to lessen as plants " \
                   "mature and develop adult plant resistance to the disease. "
            des4 = "Blast lesions can commonly be confused with Brown Spot lesions"
            des5 = "Leaf blast lesions are usually elongated and pointed at each end, while brown spot lesions tend " \
                   "to be more round, brown in color, and have a yellow halo surrounding the lesion. "
        elif text_position == 6:
            topic = ""
            des1 = "Sheath blight is a fungal disease caused by Rhizoctonia solani. Infected leaves senesce or dry " \
                   "out and die more rapidly, young tillers can also be destroyed. "
            des2 = "As a result, the leaf area of the canopy can significantly be reduced by the disease. This " \
                   "reduction in leaf area, along with the diseased-induced senescence of leaves and young infected " \
                   "tillers are the primary causes of yield reduction. "
            des3 = "Sheath blight occurs in areas with high temperatures (28−32°C),  high levels of nitrogen " \
                   "fertilizer, and relative humidity of crop canopy from 85−100%. "
            des4 = "High seeding rate or close plant spacing, dense canopy, disease in the soil, sclerotia or " \
                   "infection bodies floating on the water, and growing of high yielding improved varieties also " \
                   "favor disease development. "
            des5 = "oval or ellipsoidal greenish-gray lesions, usually, 1-3 cm long, on the leaf sheath, initially " \
                   "just above the soil or water level in the case of conventionally flooded rice. "
        elif text_position == 7:
            topic = ""
            des1 = "Rice tungro disease is caused by the combination of two viruses, which are transmitted by " \
                   "leafhoppers. It causes leaf discoloration, stunted growth, reduced tiller numbers, and sterile or " \
                   "partly filled grains. "
            des2 = "Leafhoppers can acquire the viruses from any part of the infected plant by feeding on it, " \
                   "even for a short time. It can, then, immediately transmit the viruses to other plants within 5−7 " \
                   "days. The viruses do not remain in the leafhopper's body unless it feeds again on an infected " \
                   "plant and re-acquire the viruses. "
            des3 = "Tungro infection can occur during all growth stages of the rice plant. It is most frequently seen " \
                   "during the vegetative phase. Plants are most vulnerable at the tillering stage. "
            des4 = "Tungro incidence depends on the availability of the virus sources and vector population. Other " \
                   "than infected rice plants in the farmer's field, other primary sources for tungro, include "
            des5 = "Once tungro is present in the field, it increases rapidly in young rice plants. Leafhopper " \
                   "vectors prefer to feed on young rice plants. They also acquire tungro viruses more efficiently " \
                   "from younger infected plants. "

        # return send_from_directory("images", filename, as_attachment=True)
    return render_template("template.html", image_name = filename, text = prediction, desc1 = des1, desc2 = des2,
                           desc3 = des3, desc4 = des4, desc5 = des5)


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


@app.route('/aboutUs')
def go_about_us():  # put application's code here
    return render_template('aboutUs.html')


@app.route('/index')
def go_index():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
