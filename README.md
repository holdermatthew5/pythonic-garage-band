Author: Matthew Holder

Version: 0.1.0

[PR]()

## Problem Domain:
    I would like to be able to create a garage band with a bassist, guitarist and drummer.
    They should all be able to play a solo and fetch their instrument.
    I would also like to keep track of each band I create.

## Challenge Description:
    A Band class should have a name attribute that takes a string, a members attribute that takes a list of band members, a method to ask a given member to play a solo, and a method that returns a list of all previously created bands.
    A member should have a type (string attribute), a method for fetching their instrument (returning a string) and a method for playing a solo (returning a string).
    To minimize repeated code there will be a master class 'musician' which is inherited by all types of musician (bassist, guitarist, drummer).

## 