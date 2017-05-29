# See Food
## Shazam for Food, an idea shamelessly copied from [Silicon Valley S4Ep3](http://www.slantmagazine.com/house/article/silicon-valley-recap-season-4-episode-3-intellectual-property)

### data creation
The biggest quest in such application is data creation. I have used [Fatun Chrome Extension](https://chrome.google.com/webstore/detail/fatkun-batch-download-ima/nnjjahlikiabnchcpehcpkdeckfgnohf?hl=en) which downloads images from google image search page for various food items.

### training
Place food images in /data dir with food name folder as name and train with below command
```$ python src/train.py```

the weights get stored in 'weights' dir.

### prediction
Run
```$ python src/predict.py <img_path>``` and
it will print food class name
