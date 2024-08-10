import matplotlib.pyplot as plt
plt.switch_backend('agg')
import json
from PIL import Image
import os

results = json.load(open("results.json"))
image_names = ['2017_70401921', '2017_94183115', '2017_10688111', '2017_10895938', '2017_73344050', '2017_13031777']
vis_images = []

for image_name in image_names:
    ori_image = Image.open(os.path.join("images", image_name, image_name + ".png"))
    ano_images = []
    for img in results.keys():
        if image_name not in img or "cMAP" not in img:
            continue

        ano_images.append((Image.open(img), results[img]))
        
    ano_images = sorted(ano_images, key=lambda x:x[1], reverse=True)
    ano_images.append(ori_image)
    vis_images.append(ano_images)

n_image = len(vis_images)
plt.figure(figsize=(15,21),dpi=300)
for i in range(n_image):
    plt.subplot(n_image,4,1+i*4), plt.title('original image', fontsize=15)
    plt.imshow(vis_images[i][-1]), plt.axis('off')
    plt.subplot(n_image,4,2+i*4), plt.title('cMAP = {:.1f}'.format(vis_images[i][0][1]), fontsize=15)
    plt.imshow(vis_images[i][0][0]), plt.axis('off')
    plt.subplot(n_image,4,3+i*4), plt.title('cMAP = {:.1f}'.format(vis_images[i][1][1]), fontsize=15)
    plt.imshow(vis_images[i][1][0]), plt.axis('off')
    plt.subplot(n_image,4,4+i*4), plt.title('cMAP = {:.1f}'.format(vis_images[i][2][1]), fontsize=15)
    plt.imshow(vis_images[i][2][0]), plt.axis('off')

plt.suptitle("Visualization of the same images with changing cMAP.\n(the lower cMAP the better privacy preservation)", fontsize=20)
plt.subplots_adjust(wspace=0.1, hspace=0.3)

plt.savefig("visualization_cMAP.png",dpi=300)
# plt.show()

