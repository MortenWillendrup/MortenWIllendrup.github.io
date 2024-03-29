---
layout: post
title:  Asset Swap Spread - A clear explanation
date: 2024-03-22 21:01:00
description: This posts tells 
tags: formatting images
categories: Fixed Income
thumbnail: assets/img/Asset_Swap_front.jpg
giscus_comments: true
related_posts: false
toc:
  sidebar: left
---

# Asset Swap introduction

Today's post is going to focus on Asset Swap or more specific about the asset swap spread.

Asset swaps are commonly used instrument in the finance society, which used by institutional investors in order to reduce the risk arising from holding a certain asset (usually a bond).

It happens frequently that an investor, who has just bought a certain bond (for example by participating to a issue of a new bond or to an auction on the primary market), wants to hedge the risk coming from the bond itself. It is well known, indeed, that if you are long of a bond you are indeed short interest rates, in the sense that if they go up the price of your security decreases giving you a negative P&L. 

First thing, what the investor could do is to sell another fixed income security trying to remove the sensitivity to interest rates from its portfolio; however this solution is not a perfect hedge because it often implies some sort of basis risk/curve risk between the hedged security and the hedging security.

To get an idea of what I am saying you can just try to hedge a BTP 2.8 01/03/2067 (=46 years to maturity) with the only securities you have in the proximity of the curve, that are the BTP 1.7 01/09/2051 (30y to maturity) and the BTP 2.15 01/03/2072 (51y to maturity). 

In the best case you have a 5-year curve exposure which may not seem a lot but it’s enough to make you lose several basis points, especially in the long end of the curve.

Therefore a good alternative, for the investor who has just bought the BTP 2.8 01/03/2067, may be to (asset)swap it!

Notice that this is not the only reason you may want to enter an asset swap, of course. 

You may simply want to swap your position from a fixed periodic coupon, to a floating periodic coupon. In any case, whatever are your motivations, you may find this instrument quite interesting.

# How does the asset swap work?

An asset swap is similar in structure to a plain vanilla swap with the key difference being the underlying of the swap contract. Rather than regular fixed and floating loan interest rates being swapped, fixed and floating assets are being exchanged.

Let’s try to analyze it sentence by sentence. It is similar to a plain vanilla swap, thus let’s look how this one looks like

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/Asset_Swap_2.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>

where the fixed payment is given by the Notional of the contract (N) and the Plain-vanilla Swap rate (R) relative for the time period

$$
  \text{Fixed leg}_t\;=\; R \; \times \; N
$$

