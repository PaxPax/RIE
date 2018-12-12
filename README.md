# RIE(Resize Images Easily)

RIE in essence is a simple gui over the python package Pillow. While not the prettiest looking application on the block, it does the job it needs to do. It maintains a simple user interface, that should be easy to become accustomed to.

![](C:\Users\Emmett\Documents\Projects\PythonProjects\RIE\images\mainScreen.PNG)

When you choose a folder all of the images inside that folder will be converted according to the width and height you specified. While you may pick where the newly resized images are stored, the default is a folder called `resized` located inside the programs directory. 

The `Zip Folder` option is handy when you want to move the newly resized pictures somewhere else or to simply conserve storage space. What the folder will be called when zipped and where the zipped file will be store is entirely up to you.  RIE does have default options for this as well though.

![](C:\Users\Emmett\Documents\Projects\PythonProjects\RIE\images\settings.PNG)

As you may or may not be familiar with toml files, it's rather easy to edit the changes of your settings. **Important Note:** EzBatch does spawn processes dependent on your batch size. Example you have a 100 images in your folder and you set your batch size to 10. That would mean EzBatch would spawn 10 processes to complete the job. To further that example if you have 1000 images and you set your batch size to 10 then you would spawn a 100 processes. Hopefully, you can see how quickly this can get out of hand. **You** are responsible for how many processes EzBatch should spawn by adjusting batch size accordingly. While their are pros and cons to each approach, I think this is acceptable for now and may change in the future.

While your batch size may end up being a nice even number, more often than not it won't be. RIE has a final process in place to complete the last of the images that didn't quite fit in so no worries!