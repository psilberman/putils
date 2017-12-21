DICT: Set Dict Item Normally  48.13 usec/pass  0.05 usec/item
DICT: Set Dict Item using setdefault 115.22 usec/pass  0.12 usec/item
DICT: Set only if key doesnt exist. Use KeyError exception to determine existence  50.72 usec/pass  0.05 usec/item
DICT: Set only if key doesnt exist. Use get() to determine existence 105.42 usec/pass  0.11 usec/item
DICT: Set only if key doesnt exist. Use in to determine existence  40.48 usec/pass  0.04 usec/item
OBJ CLEAR: [x.clear()] 549.22 usec/pass  0.55 usec/item
OBJ CLEAR: setattr(x,x,None) 515.78 usec/pass  0.52 usec/item
OBJ CLEAR: x.clear() 535.72 usec/pass  0.54 usec/item
OBJ CLEAR: x.x = None 444.11 usec/pass  0.44 usec/item
OBJ: Set attr by calling getattr on method to set variable. 229.15 usec/pass  0.23 usec/item
OBJ: Set attr by calling method to set variable. 185.04 usec/pass  0.19 usec/item
1000 items
1000 iterations
