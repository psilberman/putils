DICT: Set Dict Item Normally  48.86 usec/pass  0.05 usec/item
DICT: Set Dict Item using setdefault 120.00 usec/pass  0.12 usec/item

DICT: Set only if key doesnt exist. Use KeyError exception to determine existence  49.54 usec/pass  0.05 usec/item
DICT: Set only if key doesnt exist. Use get() to determine existence 107.38 usec/pass  0.11 usec/item
DICT: Set only if key doesnt exist. Use in to determine existence  43.98 usec/pass  0.04 usec/item
OBJ CLEAR: [x.clear()] 562.47 usec/pass  0.56 usec/item
OBJ CLEAR: setattr(x,x,None) 515.67 usec/pass  0.52 usec/item
OBJ CLEAR: x.clear() 545.35 usec/pass  0.55 usec/item
OBJ CLEAR: x.x = None 446.62 usec/pass  0.45 usec/item
OBJ: Set attr by calling getattr on method to set variable. 227.94 usec/pass  0.23 usec/item
OBJ: Set attr by calling method to set variable. 190.65 usec/pass  0.19 usec/item
1000 items
1000 iterations
