import imageio.v3 as iio
filenames = ['img1.png', 'img2.png', 'img3.png', 'img4.png']
images = [ ]
for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('gru.gif', images, duration=2000, loop = 0)