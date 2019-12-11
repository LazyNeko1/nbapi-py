**Random**
---------

**Random Nekos:**
``nbapi.random.neko()``

  -By default WILL only show images with a source.
  
  -Options:
    `source=True/False` - Shows image source and ID (for reporting)
    
    `check=True/False` - Check if image has a source or not.
    
    `min,max(default:false)=int()` - Input minimum or maximum ID values (eg ID 1 through 20) 
    
      -By default `max` is False (get total amount of images on API) and `min` is 1
      
      -NOTE: if this value is below a certian amount, the API will return a infinite `while True` loop. 
      

**Random Anime:**
``nbapi.random.anime()``

  -Options:
  
    `source=True/False` - Shows image source and ID (for reporting)
    
    `check=True/False` - Check if image has a source or not.
    
    `min,max(default:false)=int()` - Input minimum or maximum ID values (eg ID 1 through 20)
    
      -By default `max` is False (get total amount of images on API) and `min` is 1
      
      -NOTE: if this value is below a certian amount, the API will return a infinite `while True` loop. 






**Search**
--------
**Nekos:**
``nbapi.search.neko(*int)``
  -Options:
    `source=True/False` - Shows image source and ID (for reporting)

**Anime:**
``nbapi.search.anime(*int)``
  -Options:
    `source=True/False` - Shows image source and ID (for reporting)


