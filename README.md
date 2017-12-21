DICT: Set Dict Item Normally  43.45 usec/pass  0.04 usec/item

DICT: Set Dict Item using setdefault 111.08 usec/pass  0.11 usec/item

DICT: Set only if key doesnt exist. Use KeyError exception to determine existence  50.73 usec/pass  0.05 usec/item

DICT: Set only if key doesnt exist. Use get() to determine existence 104.98 usec/pass  0.10 usec/item

DICT: Set only if key doesnt exist. Use in to determine existence  41.75 usec/pass  0.04 usec/item

OBJ CLEAR: [x.clear()] 557.15 usec/pass  0.56 usec/item

OBJ CLEAR: setattr(x,x,None) 513.60 usec/pass  0.51 usec/item

OBJ CLEAR: x.clear() 539.62 usec/pass  0.54 usec/item

OBJ CLEAR: x.x = None 437.54 usec/pass  0.44 usec/item

OBJ: Set attr by calling getattr on method to set variable. 228.96 usec/pass  0.23 usec/item

OBJ: Set attr by calling method to set variable. 168.58 usec/pass  0.17 usec/item

1000 items

1000 iterations

