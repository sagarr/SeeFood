# See Food
## Shazam for Food, an idea shamelessly copied from [Silicon Valley S4Ep3](http://www.slantmagazine.com/house/article/silicon-valley-recap-season-4-episode-3-intellectual-property)

### training
Place food images in /data dir with food name folder as name and train with below command
```$ python src/train.py```

the weights get stored in 'weights' dir.

### prediction
Run
```$ python src/predict.py <img_path>``` and
it will print food class name
