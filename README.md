Author: Matthew Holder

Version: 0.1.0

[PR]()

[Whiteboard](Assets/white-board.jpg)

## Problem Domain:
    I would like to be able to create a garage band with a bassist, guitarist and drummer.
    They should all be able to play a solo and fetch their instrument.
    I would also like to keep track of each band I create.

## Challenge Description:
    A Band class should have a name attribute that takes a string, a members attribute that takes a list of band members, a method to ask a given member to play a solo, and a method that returns a list of all previously created bands.
    A member should have a type (string attribute), a method for fetching their instrument (returning a string) and a method for playing a solo (returning a string).
    To minimize repeated code there will be a master class 'musician' which is inherited by all types of musician (bassist, guitarist, drummer).

## Solution:
    Purpose:
        This module allows a person to create a band with the name of their choosing. A user can also createmembers for the band such as a Bassist, Guitarist and/or Drummer. Each member is listed in the members attribute of the Band class. Each member is capable of fetching their instrument and/or playing a solo. Finally, the Band class keeps a list of previous instances referencable with `Band.instances`.
    Use:
        To use Band assign `Band()` to a variable of your choosing and pass in the name of the band and a list containing all band members in no particular order. The members can also be created by simply assigning Bassist(), Guitarist(), or Drummer() to a variable and passing in the name of the member as an argument to the proper set of parenthesis. The full creation of a band would appear as follows:
        ```
        Mike = Bassist("Mike")
        Jess = Guitarist("Jess")
        John = Drummer("John")
        The_MJs = Band("The_MJs", [Mike, Jess, John])
        ```
