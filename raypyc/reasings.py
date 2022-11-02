"""**********************************************************************************************

   reasings - raylib easings library, based on Robert Penner library

   Useful easing functions for values animation

   This header uses:
       #define REASINGS_STATIC_INLINE      // Inlines all functions code, so it runs faster.
                                           // This requires lots of memory on system.
   How to use:
   The four inputs t,b,c,d are defined as follows:
   t = current time (in any unit measure, but same unit as duration)
   b = starting value to interpolate
   c = the total change in value of b that needs to occur
   d = total time it should take to complete (duration)

   Example:

   currentTime = 0
   duration = 100
   startPositionX = 0.0f
   finalPositionX = 30.0f
   currentPositionX = startPositionX

   while currentPositionX < finalPositionX:
       currentPositionX = ease_sine_in(currentTime, startPositionX, finalPositionX - startPositionX, duration)
       currentTime += 1

   A port of Robert Penner's easing equations to C (http://robertpenner.com/easing/)

   Robert Penner License
   ---------------------------------------------------------------------------------
   Open source under the BSD License.

   Copyright (c) 2001 Robert Penner. All rights reserved.

   Redistribution and use in source and binary forms, with or without modification,
   are permitted provided that the following conditions are met:

       - Redistributions of source code must retain the above copyright notice,
         this list of conditions and the following disclaimer.
       - Redistributions in binary form must reproduce the above copyright notice,
         this list of conditions and the following disclaimer in the documentation
         and/or other materials provided with the distribution.
       - Neither the name of the author nor the names of contributors may be used
         to endorse or promote products derived from this software without specific
         prior written permission.

   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
   ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
   WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
   IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
   INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
   BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
   LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
   OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
   OF THE POSSIBILITY OF SUCH DAMAGE.
   ---------------------------------------------------------------------------------

   Copyright (c) 2015-2022 Ramon Santamaria (@raysan5)

   This software is provided "as-is", without any express or implied warranty. In no event
   will the authors be held liable for any damages arising from the use of this software.

   Permission is granted to anyone to use this software for any purpose, including commercial
   applications, and to alter it and redistribute it freely, subject to the following restrictions:

     1. The origin of this software must not be misrepresented; you must not claim that you
     wrote the original software. If you use this software in a product, an acknowledgment
     in the product documentation would be appreciated but is not required.

     2. Altered source versions must be plainly marked as such, and must not be misrepresented
     as being the original software.

     3. This notice may not be removed or altered from any source distribution.

**********************************************************************************************"""

import math  # Required for: sin(), cos(), sqrt(), pow(), pi


# Linear Easing functions

def ease_linear_none(t: float, b: float, c: float, d: float) -> float:
    """Ease: Linear"""
    return c * t / d + b


def ease_linear_in(t: float, b: float, c: float, d: float) -> float:
    """Ease: Linear In"""
    return c * t / d + b


def ease_linear_out(t: float, b: float, c: float, d: float) -> float:
    """Ease: Linear Out"""
    return c * t / d + b


def ease_linear_in_out(t: float, b: float, c: float, d: float) -> float:
    """Ease: Linear In Out"""
    return c * t / d + b


# Sine Easing functions

def ease_sine_in(t: float, b: float, c: float, d: float) -> float:
    """Ease: Sine In"""
    return -c * math.cos(t / d * (math.pi / 2.0)) + c + b


def ease_sine_out(t: float, b: float, c: float, d: float) -> float:
    """Ease: Sine Out"""
    return c * math.sin(t / d * (math.pi / 2.0)) + b


def ease_sine_in_out(t: float, b: float, c: float, d: float) -> float:
    """Ease: Sine In Out"""
    return -c / 2.0 * (math.cos(math.pi * t / d) - 1.0) + b


# Circular Easing functions

def ease_circ_in(t: float, b: float, c: float, d: float) -> float:
    """Ease: Circular In"""
    t /= d
    return -c * (math.sqrt(1.0 - t * t) - 1.0) + b


def ease_circ_out(t: float, b: float, c: float, d: float) -> float:
    """Ease: Circular Out"""
    t = t / d - 1.0
    return c * math.sqrt(1.0 - t * t) + b


def ease_circ_in_out(t: float, b: float, c: float, d: float) -> float:
    """Ease: Circular In Out"""
    t /= d / 2.0
    if t < 1.0:
        return -c / 2.0 * (math.sqrt(1.0 - t * t) - 1.0) + b
    t -= 2.0
    return c / 2.0 * (math.sqrt(1.0 - t * t) + 1.0) + b


# Cubic Easing functions

def ease_cubic_in(t: float, b: float, c: float, d: float) -> float:
    """Ease: Cubic In"""
    t /= d
    return c * t * t * t + b


def ease_cubic_out(t: float, b: float, c: float, d: float) -> float:
    """Ease: Cubic Out"""
    t = t / d - 1.0
    return c * (t * t * t + 1.0) + b


def ease_cubic_in_out(t: float, b: float, c: float, d: float) -> float:
    """Ease: Cubic In Out"""
    t /= d / 2.0
    if t < 1.0:
        return c / 2.0 * t * t * t + b
    t -= 2.0
    return c / 2.0 * (t * t * t + 2.0) + b


# Quadratic Easing functions

def ease_quad_in(t: float, b: float, c: float, d: float) -> float:
    """Ease: Quadratic In"""
    t /= d
    return c * t * t + b


def ease_quad_out(t: float, b: float, c: float, d: float) -> float:
    """Ease: Quadratic Out"""
    t /= d
    return -c * t * (t - 2.0) + b


def ease_quad_in_out(t: float, b: float, c: float, d: float) -> float:
    """Ease: Quadratic In Out"""
    t /= d / 2
    if t < 1:
        return ((c / 2) * (t * t)) + b

    return -c / 2.0 * (((t - 1.0) * (t - 3.0)) - 1.0) + b


# Exponential Easing functions

def ease_expo_in(t: float, b: float, c: float, d: float) -> float:
    """Ease: Exponential In"""
    return b if t == 0.0 else c * math.pow(2.0, 10.0 * (t / d - 1.0)) + b


def ease_expo_out(t: float, b: float, c: float, d: float) -> float:
    """Ease: Exponential Out"""
    return b + c if t == d else c * (-math.pow(2.0, -10.0 * t / d) + 1.0) + b


def ease_expo_in_out(t: float, b: float, c: float, d: float) -> float:
    """Ease: Exponential In Out"""
    if t == 0.0: return b
    if t == d: return b + c
    t /= d / 2.0
    if t < 1.0: return c / 2.0 * math.pow(2.0, 10.0 * (t - 1.0)) + b

    return c / 2.0 * (-math.pow(2.0, -10.0 * (t - 1.0)) + 2.0) + b


# Back Easing functions

def ease_back_in(t: float, b: float, c: float, d: float) -> float:
    """Ease: Back In"""
    s: float = 1.70158
    t /= d
    post_fix: float = t
    return c * post_fix * t * ((s + 1.0) * t - s) + b


def ease_back_out(t: float, b: float, c: float, d: float) -> float:
    """Ease: Back Out"""
    s: float = 1.70158
    t = t / d - 1.0
    return c * (t * t * ((s + 1.0) * t + s) + 1.0) + b


def ease_back_in_out(t: float, b: float, c: float, d: float) -> float:
    """Ease: Back In Out"""
    s: float = 1.70158
    t /= d / 2.0

    if t < 1.0:
        s *= 1.525
        return c / 2.0 * (t * t * ((s + 1.0) * t - s)) + b

    t -= 2.0
    post_fix: float = t
    s *= 1.525
    return c / 2.0 * (post_fix * t * ((s + 1.0) * t + s) + 2.0) + b


# Bounce Easing functions

def ease_bounce_out(t: float, b: float, c: float, d: float) -> float:
    """Ease: Bounce Out"""
    t /= d
    if t < 1.0 / 2.75:
        return c * (7.5625 * t * t) + b
    elif t < 2.0 / 2.75:
        t -= 1.5 / 2.75
        post_fix: float = t
        return c * (7.5625 * post_fix * t + 0.75) + b
    elif t < 2.5 / 2.75:
        t -= 2.25 / 2.75
        post_fix: float = t
        return c * (7.5625 * post_fix * t + 0.9375) + b
    else:
        t -= 2.625 / 2.75
        post_fix: float = t
        return c * (7.5625 * post_fix * t + 0.984375) + b


def ease_bounce_in(t: float, b: float, c: float, d: float) -> float:
    """Ease: Bounce In"""
    return c - ease_bounce_out(d - t, 0.0, c, d) + b


def ease_bounce_in_out(t: float, b: float, c: float, d: float) -> float:
    """Ease: Bounce In Out"""
    if t < d / 2.0:
        return ease_bounce_in(t * 2.0, 0.0, c, d) * 0.5 + b
    else:
        return ease_bounce_out(t * 2.0 - d, 0.0, c, d) * 0.5 + c * 0.5 + b


# Elastic Easing functions

def ease_elastic_in(t: float, b: float, c: float, d: float) -> float:
    """Ease: Elastic In"""
    if t == 0.0: return b
    t /= d
    if t == 1.0: return b + c

    p: float = d * 0.3
    a: float = c
    s: float = p / 4.0
    t -= 1.0
    post_fix: float = a * math.pow(2.0, 10.0 * t)

    return -(post_fix * math.sin((t * d - s) * (2.0 * math.pi) / p)) + b


def ease_elastic_out(t: float, b: float, c: float, d: float) -> float:
    """Ease: Elastic Out"""
    if t == 0.0: return b
    t /= d
    if t == 1.0: return b + c

    p: float = d * 0.3
    a: float = c
    s: float = p / 4.0

    return a * math.pow(2.0, -10.0 * t) * math.sin((t * d - s) * (2.0 * math.pi) / p) + c + b


def ease_elastic_in_out(t: float, b: float, c: float, d: float) -> float:
    """Ease: Elastic In Out"""
    if t == 0.0: return b
    t /= d / 2.0
    if t == 2.0: return b + c

    p: float = d * (0.3 * 1.5)
    a: float = c
    s: float = p / 4.0

    if t < 1.0:
        t -= 1.0
        post_fix: float = a * math.pow(2.0, 10.0 * t)
        return -0.5 * (post_fix * math.sin((t * d - s) * (2.0 * math.pi) / p)) + b

    t -= 1.0
    post_fix: float = a * math.pow(2.0, -10.0 * t)

    return post_fix * math.sin((t * d - s) * (2.0 * math.pi) / p) * 0.5 + c + b
