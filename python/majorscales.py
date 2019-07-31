## author Matt Blaul
## 12/5/2017

## Script to find a specific note in a major scale based on the scale and solege sound.

scale = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
majscale = {"Do":0,
            "Re":2,
            "Me":4,
            "Fa":5,
            "So":7,
            "La":9,
            "Ti":11}

usernote = "B"
usersound = "Re"

if (majscale[usersound]+scale.index(usernote) > 12):
    wrap = majscale[usersound]+scale.index(usernote) - 12
    outnote = scale[wrap]
else:
    outnote = scale[majscale[usersound]+scale.index(usernote)]

print(outnote)
