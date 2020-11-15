# Convolutional Autoencoder

![cover](https://github.com/priyavrat-misra/convolutional-autoencoder/blob/master/images/cover.png?raw=true "CAE in action!")


## How it works
> Usually, Autoencoders have two parts, an encoder and a decoder. When some input image is passed through the encoder, it encodes the image to a compressed representation. Then that representation can be passed through the decoder to reconstruct the image.
>
> Although autoencoders aren't much widely used for image compression and decompression, they are known for their ability to extract key information from an image which are often the most essential features required for image reconstruction techniques.
> Few such techniques include image denoising, and making grayscale images colorful!

<br>

## About this project
> This project uses the [MNIST Dataset](http://yann.lecun.com/exdb/mnist/) for [training the autoencoder](https://github.com/priyavrat-misra/convolutional-autoencoder/blob/master/train.ipynb "train.ipynb"). Then few images from the test set are fed into the [model](https://github.com/priyavrat-misra/convolutional-autoencoder/blob/master/network.py "network.py"), which then compresses them and tries to reconstruct the original images!

<br>


## Results
> Here check this plot, can you distinguish between the two rows?
>
> ![original+reconstructed](https://github.com/priyavrat-misra/convolutional-autoencoder/blob/master/images/original_decoded.png?raw=true "pretty indifferentiable, right?")
>
> _<sup>(first row contains the original images, and the second, you guessed it right!, the reconstructed ones)</sup>_
