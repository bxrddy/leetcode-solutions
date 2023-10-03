# 1757.Recyclable and Low Fat Products

## Intuition
Hey there! So, you've got two bits of code that aim to tackle the same problem – finding products that are both low-fat and recyclable. At a first glance, one takes the path of an old-school loop, while the other leverages the power of `pandas` to do things more succinctly.

## Approach

### Code 01:
This code is like that friend who likes to go through things one by one, meticulously. It manually steps through each row of the `products` DataFrame, checking if the product is both low-fat and recyclable. If it is, it takes note of the product ID. It's like going through a checklist and ticking off items one by one.

### Code 02:
This code, on the other hand, is that efficient buddy who just "gets" things done. Instead of checking each product individually, it asks `pandas` to filter out all the products that meet the criteria in one fell swoop.

### About Vectorization:
Ever heard of the term "vectorization"? It's a fancy term that stems from the world of vectors in math. In the land of coding, especially with tools like `pandas`, it's all about doing operations on a whole bunch of data at once, rather than one piece at a time. It's kind of like eating popcorn. You could eat one piece at a time, or you could grab a handful (vectorized!) and munch away. The second code uses this "grab a handful" approach, making it pretty snappy.

## Code
Check out the ```#1_recyclable_lowfat.py``` and ```#2_recyclable_lowfat.py``` file.
