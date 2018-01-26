from deva_mesh import Deva_Mesh
from deva_const import MeshType

# put the quotes in single lines
_role = [
"""
 o 
-+-
 ^ 
""",
"""
 o 
-+-
 " 
"""]

role = Deva_Mesh(_role, MeshType.ANIMATE_ON_TOUCH)

_npc = [
"""
 o 
+++
 ^ 
"""
]

npc = Deva_Mesh(_npc)

#4x9
_rock = [
"""
    .-.  
`/-+` `/ 
/  :    /
.  `    .
""",
"""
 -.-     
 / `:    
|   ::--`
     `  -
""",
"""
-+//+ 
s   `s/--
:    `s. 
+      / 
"""
]

rock = Deva_Mesh(_rock, MeshType.RANDOM)

_house = [
"""
        `-///:   
    -///:    `+/ 
 oy+.  xxxx.///o+
o- :++------   -+
d///::h        -+
y     y   |    -+
y     y   |    -+
--------###------
"""
]

house = Deva_Mesh(_house, MeshType.STATIC)


_river = [
"""
                                                   ````..        
                              `````       :::-.````      ..`     
 /+/:--...``````````````````         ````-                       
           `:::::       ---...````````````     ````````````````` 
                                 `````````````                 `.
 ::.     ````````````````````                   ```````````      
  `--...`                                                  `:    
""",
"""
                                                   ````..        
                              `````       :::-.````      ..`     
 /+/:--...``````````````````         ````-                       
``````````            `:::::       ---...````````````     ```````
             `.                                 `````````````    
    ```````````       ::.     ````````````````````               
  `--...`                                                  `:    
""",
"""
                                                   ````..        
                              `````       :::-.````      ..`     
 /+/:--...``````````````````         ````-                       
````     `````````````````            `:::::       ---...````````
     `````````````                 `.                            
``                   ```````````       ::.     ``````````````````
  `--...`                                                  `:    
""",

]

river = Deva_Mesh(_river, MeshType.ANIMATE_AUTO)

_grass = [
"""
...................................................................................
...................................................................................
...................................................................................
...................................................................................
...................................................................................
...................................................................................
...................................................................................
...................................................................................
...................................................................................
...................................................................................
"""
]

grass = Deva_Mesh(_grass)

_temple = [
"""
         /-          
       .+-+::-``     
   ``-/:`.d-``-::::::
-::--. `-+h-::-.`  /.
:/-.:++//.y...://:/- 
  `.o             +  
    y     -----:  s  
    s     y.```y  y  
    +-    m`   s  y  
    ::    y    s  s  
    :+::::+####+::/  
"""
]

temple = Deva_Mesh(_temple)

_box = [
"""
x
""",
"""
o
"""
]

box = Deva_Mesh(_box, MeshType.ANIMATE_AUTO)

MeshMap = {
        'rock': rock,
        'role': role,
        'house': house,
        'npc': npc,
        'river': river,
        'grass': grass,
        'temple': temple,
        'box': box,
        }