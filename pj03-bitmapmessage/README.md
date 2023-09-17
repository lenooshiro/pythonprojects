## The Bitmap Message 

This program uses a multiline string as a bitmap, a 2D image with only two possible colors for each pixel, to determine how it should display a message from the user. In this bitmap, space characters represent an empty space, and all other characters are replaced by characters in the user’s message.

The provided bitmap resembles a world map, but you can change this to any image you’d like. The binary simplicity of the space-or-message-characters system makes it good for beginners. Try experimenting with different messages to see what the results look like!

***

The output will look like this:


```
Bitmap Message, by Al Sweigart al@inventwithpython.com
Enter the message to display with the bitmap.
> Hello!

Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!He
   lo!Hello!Hello   l  !He lo  e      llo!Hello!Hello!Hello!Hello!He
  llo!Hello!Hello!Hello He lo H  l !Hello!Hello!Hello!Hello!Hello H
 el      lo!Hello!Hello!He       lo!Hello!Hello!Hello!Hello!Hel
          o!Hello!Hello          lo  e lo!H ll !Hello!Hello!H l
           !Hello!He            llo!Hel   Hello!Hello!Hell ! e
            Hello!He           ello!Hello!Hello!Hello!Hell  H
   l        H llo! ell         ello!Hello!Hell !Hello  el o
               lo!H  l         ello!Hello!Hell   ell !He  o
                 !Hello         llo!Hello!Hel    el   He  o
                 !Hello!H        lo!Hello!Hell    l  !H llo
                   ello!Hel         Hello!He          H llo Hell
                   ello!Hell         ello!H  l        Hell !H l o!
                   ello!Hell         ello!H l o           o!H l   H
                     lo!Hel          ello! el             o!Hel   H
                     lo!He            llo! e            llo!Hell
                    llo!H             llo!              llo!Hello
                    llo!              ll                 lo!Hell   e
                    llo                                       l    e
                    ll     l                    H
Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!He
```