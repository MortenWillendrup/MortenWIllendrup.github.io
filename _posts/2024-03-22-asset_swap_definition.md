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

It happens frequently that an investor, who has just bought a certain bond (for example by participating in an issuance of a new bond or to an auction on the primary market), wants to hedge the risk coming from the bond itself. It is well known, indeed, that if you are long of a bond you are indeed short interest rates, in the sense that if they go up the price of your security decreases giving you a negative P&L. 

First thing, what the investor could do is to sell another fixed income security trying to remove the sensitivity to interest rates from its portfolio; however this solution is not a perfect hedge because it often implies some sort of basis risk/curve risk between the hedged security and the hedging security.

To get an idea of what I am saying you can just try to hedge a BTP 2.8 01/03/2067 (=46 years to maturity) with the only securities you have in the proximity of the curve, that are the BTP 1.7 01/09/2051 (30y to maturity) and the BTP 2.15 01/03/2072 (51y to maturity). 

In the best case you have a 5-year curve exposure which may not seem a lot but it’s enough to make you lose several basis points, especially in the long end of the curve.

Therefore a good alternative, for the investor who has just bought the BTP 2.8 01/03/2067, may be to (asset)swap it!

Notice that this is not the only reason you may want to enter an asset swap, of course. 

You may simply want to swap your position from a fixed periodic coupon, to a floating periodic coupon. In any case, whatever are your motivations, you may find this instrument quite interesting.

# How does the asset swap work?

An asset swap is similar in structure to a plain vanilla swap with the key difference being the underlying of the swap contract. Rather than regular fixed and floating loan interest rates being swapped, fixed and floating assets are being exchanged.

Let’s try to analyze it sentence by sentence. It is similar to a plain vanilla swap, thus let’s look how this one looks like

where the fixed payment is given by the Notional of the contract $N$ and the Plain-vanilla Swap rate $R$ relative for the time period

<div class="col-sm mt-3 mt-md-0">
    {% include figure.html path="assets/img/Asset_Swap_2.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}
</div>

$$
  \text{Fixed leg}_t\;=\; R \; \times \; N
$$

and the floating payment is given by the Notional of the contract (N) and the floating rate ( $$r_t$$ ), that usually is Euribor or OIS in Europe, relative for the time period

$$
  \text{Float leg}_t\;=\; r_t \; \times \; N
$$

and from the non-arbitrage assumption we know that we can find exactly the value of $R$.

Now, usually institutional investors are those who buy the swap, in the sense that they pay the fixed leg and receive the floating leg (they are said to be buyer because they profit if rates goes up since they receive the floating leg).
In an asset swap the investor keeps receiving the floating leg and paying the fixed leg (= he gives away the interest rate risk), which…guess…is now exactly the coupon he receives from the asset he owns.

Indeed, in an asset swap the structure is


<div class="col-sm mt-3 mt-md-0">
    {% include figure.html path="assets/img/Asset_Swap_3.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}
</div>

where the fixed payment is given by the Notional of the contract ($N$) and the **Coupon** rate ($$c$$) of the asset the investor wants to asset-swap

$$
  \text{Fixed leg}_t\;=\; c \; \times \; N
$$

and the floating payment is given by the Notional of the contract ($N$) and the floating rate ($$r_t$$) plus the asset swap spread ($A$)

$$
  \text{Float leg}_t\;=\; \left(r_t+A\right) \; \times \; N
$$

and from the non-arbitrage assumption we will see that we can find exactly the value that $$A$$ must take.

## bit of intuition

Try to take the point of view of a market making bank which is everyday running its business of selling plain-vanilla swap, where it pays the periodic floating rate and receive the Swap spread ($R$) from its clients. Assume the swap rate is $R= 0.5$ semi-annual. 

### The investor's interaction with the bank


**INVESTOR**: “Hey look, I just bought this BTP 2.15 01/3/2067 that is paying me this 1.075 (2.15/2) each semester and I don’t really know what to do with it, especially beacuse I fear interest rates are going up”

**BANK**: “so what? Would you like to receive Euribor then? So that if rates go up your cash flow increases”

**INVESTOR**: “Yes. i’d love to!”

**BANK**: “ok dude, I’ll pay you Euribor 6-month at every date your BTP pays its coupons and you give the coupons to me. Sounds like a great deal…I take the fixed coupons and so the risk of rates going up and you’ll have your floating rate.”


**INVESTOR**: “well not really…my BTP pays a 6-month coupon of 1.075, which I must give to you, and in return you give me back only the Euribor? To your clients on plain-vanilla swaps you are paying the Euribor rate every 6 months and they’re paying you only a fixed swap rate of 0.5. Why should I pay you 1.075 if they pay 0.5, if we receive the same?”

**BANK**: “ok, fine..fine…I’ll add up to that a fixed asset swap spread”

And that is basically how we arrived to $$\text{FLoat Leg}_t = \left(r_t + A\right) \times N$$

#### Two cases

##### Coupon greater than the current swap rate

We can therefore imagine two different cases. In the first one, where the investor wants to asset-swap a bond which has a coupon greater than the current swap rate ($c > R$), the bank must add-up a positive asset swap spread to the floating leg, in order to compensate the fact that the investor is paying an higher fixed coupon (with respective to the investor on the plain vanilla swap).

<div class="col-sm mt-3 mt-md-0">
    {% include figure.html path="assets/img/Asset_Swap_4.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}
</div>

In the “mezzanine” case where the bond’s coupon is exactly equal to the swap rate ($$R$$) the bank must not add anything since the structure is exactly equal to the plain-vanilla case.

##### Coupon lower than the current swap rate

In the case in which the bond has a very small coupon, below the swap rate ($$c < R$$) the bank should charge a negative asset swap spread to the investor, meaning decrease the Euribor rate which pays to the client. Notice however that this is mostly an academic situation since bond’s coupons are floored at zero, even in a negative rates environment

<div class="col-sm mt-3 mt-md-0">
    {% include figure.html path="assets/img/Asset_Swap_5.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}
</div>

he main takeaway from this paragraph should be that the asset swap spread is a flexible amount which depends on the bond the investor wants to swap and that its first driver is the difference between the coupon rate ($$c$$) of the bond and the prevalent swap rate ($$R$$).

Is that all? Unfortunately no, there is another component which influence the asset swap spread, but for the moment we can write

$$
  A\;=\; \left(c-R\right)+\text{Something} 
$$

### The Present Value of a zero-one

To give you a bit of time to digest what we have said in the paragraphs above, I am going to review the concept of PV01.

We all know the definition of DV01 (if not you can have a look at here), which is the monetary change in the price of a bond given by a shift of 1 basis point in yield. 

PV01 is a very similar concept which relates to coupons instead. Indeed it is the monetary change in the price of a bond given by a shift of 1 basis point in coupon.

Starting from the formula to price (i.e. to discount) fixed known cash flows we can write

\begin{equation}
\label{eq:risk-free_discounting}
 P_{rf}\;=\; \frac{\sum{c \times N}}{(1+r_t)^t} + \frac{c\times N+N}{(1+r_T)^T}
\end{equation}


that is the theoretical price we should have if we discount all the cash flows using the risk free rate ($$r$$). However we are well aware of the fact that this is not the price we observe on the market because of credit and liquidity issues. Therefore we may use the yield to maturity (y)

$$
  P_{ytm}\;=\; \frac{\sum{c \times N}}{(1+y_t)^t} + \frac{c\times N+N}{(1+y_T)^T}
$$

or the zeta spread, that is an additional curve which accounts for the riskiness of the bond

$$
  P_{zs}\;=\; \frac{\sum{c \times N}}{(1+r_t+z_t)^t} + \frac{c\times N+N}{(1+r_T+z_T)^T}
$$


in any case it is obvious that $$P_{ytm}\;=\;P_{zs}\;=\;P_{Observed}$$

Starting from these formulas we can increase the value of the coupon rate by one basis point, setting a new $$c_1 = c+0.01$$ and see how the price changes. The PV01 is this change in price.

Using formula \eqref{eq:risk-free_discounting} which then becomes 


\begin{equation}
\label{eq:risk-free_discounting_pv01}
P^{1}_{rf}\;=\; \frac{\sum{c_1 \times N}}{(1+r_t)^t} + \frac{c_1\times N+N}{(1+r_T)^T}
\end{equation}

using \eqref{eq:risk-free_discounting} and \eqref{eq:risk-free_discounting_pv01}, we can define $$PV01=P^{1}_{rf}-P_{rf)$$ and with some algebraic adjustments we get

\begin{equation}
\label{eq:pv01_rf}
PV01_{rf}\;=\; \sum{0.1}\frac{1}{(1+r_t)^t}
\end{equation}

## The Last Step

In Asset Swap, like in every other swap, the value at inception for the two parties must be null (if one side of the trade was more convenient than the other it wouldn’t be possible to close the trade, since everybody would want to sit on that side, on average). Therefore the value of the two legs must be equal.

To determine the exact value of both legs, let’s analyse more in deep the flows behind the asset swap.

<div class="col-sm mt-3 mt-md-0">
    {% include figure.html path="assets/img/Asset_Swap_7.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}
</div>

The investor has bought a bond at the dirty price ($$P_{ytm}$$), receives the coupons which forwards to the Bank but must also give to the bank the amount $$N-P_{ytm}$$ (usually N=100).

The latter is an upfront payment which the investor must give to the bank because normal Swap contracts are paid on a notional of $$N$$ and so are the legs of the asset swap. Therefore, if the investor wants the bank to treat him as a classic swap buyer, must give to the bank the difference between the classic notional amount ($$N$$) and the capital he has invested ($$P_{ytm}$$). And it must give it upfront, because of course the Bank will want to make interest on this capital.

The Bank receives the coupons and pays the Euribor (or Libor) + Asw spread. We already know that the Asw spread must include the difference between the coupon and the swap rate ($$c-R$$) but now we know that we must also include the fact that the bank has received an upfront capital $$ N-P_{ytm} $$.


Indeed the bank must reimburse this capital which otherwise will represent a transfer of value from one side of the contract to the other. The Asw spread is therefore increased by

$$
ASW =(c-R)+\text{Something}
$$

\begin{equation}
\label{eq:ASW_Spread_increase}
ASW\;=\; (c-R)+ (N- P_{ytm})\times\frac{1}{100\times N \times PV01_{Rf}}
\end{equation}


where the second term is 1 over the present value of an annuity of value N and it is needed to convert a monetary amount ($$ N-P_{ytm} $$) into a rate.

Another way of seeing it…

We have just seen that the asset swap spread is defined as in \eqref{eq:ASW_Spread_increase}, but if we expand the definition, where the swap rate we know is defined as

\begin{equation}
\label{eq:Swap_rate}
R\;=\; \frac{1-d_T}{\sum d_t}
\end{equation}

where $$d = \frac{1}{(1+r_t)^{t}} is the risk free discount rate. Also we know that $$ PV01 = 0.01\sum{d_t} $$ when $$N = 100$$, and as such we can write the asset swap as


\begin{equation}
\label{eq:ASW_1}
ASW\;=\; c-[(1-d_t)\times N \times (N-P_{ytm})]+ \times\frac{1}{100\times N \times PV01_{Rf}}
\end{equation}

and

\begin{equation}
\label{eq:ASW_2}
ASW\;=\; [c\times PV01 \times 100 \times N-(1-d_t) \times N + (N-P_{ytm})]+ \times\frac{1}{100\times N \times PV01_{Rf}}
\end{equation}


which simplifies to

\begin{equation}
\label{eq:ASW_3}
ASW\;=\; [c\times N \times \sum{d_t}+d_T \times N-P_{ytm})]+ \times\frac{1}{100\times N \times PV01_{Rf}}
\end{equation}

Here we remember that $$ P_{rf} = c \times N \times \times \sum{d_t}+d_T \times N $$ and then we get

\begin{equation}
\label{eq:ASW_4}
ASW\;=\; [P_{rf}-P_{ytm}]+ \times\frac{1}{N \times \sum{d_t}}
\end{equation}


which gives another definition of the Asw spread as the rate that must compensate the present value difference between the “fair” price of the bond (meaning priced as a pure risk free) and the price of the bond observed in the market via the yield to maturity.

This definition consider the asset swap spread as a measure of riskiness of the bond, and therefore we expect results that are very close to the z-spread as written in the paragraph (“The present value of a zero one”). This explain why sometimes the asset swap spread is used as a measure of bonds pricing over the risk free rate.

Let’s see a simple scenario: a bond that is very cheap compared to its peers (i.e. nobody wants it) will show a (relatively) high yield to maturity. Under another pricing formula this can also be seen as an higher z-spread ($$ z_t $$), because $$ P_{ytm}=P_{z_t} $$.

 This means that the difference $$ P_{rf}-P_{ytm} $$ must be quite relevant, which implies an higher Asset swap spread.

This is because the investor, is giving upfront to the bank the amount $$N-P_{ytm}$$ that in this case is relevant since the bond is cheap and $$P_{ytm}$$ is low; therefore the bank must compensate with an higher Asw spread.










