#!/usr/bin/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

a=challenge[2][1]
b=challenge[2][0]
c=challenge[3]

d=trial[2]
#print(type(d))
#print(d)
#print(d.get("eyes"))
e=d.get("goggles")
f=d.get("eyes")
g=trial[3]

h=nightmare[0]
i=h.get("kumquat")
#print(i)
j=h.get("user")
k=j.get("name")
l=k.get("first")
#print(l)
m=h.get("d")
#print(m)

print("My " + l + "! The " + i + " do " + m + "!")

print("My " + e + "! The " + f + " do " + g + "!")

print("My " + a + "! The " + b + " do " + c + "!")


