HoldingPeriodRisk
=================

Monte-Carlo simulation of a risky asset held for 1, 5, or 20 years.

The purpose of this program is to evaluate how the holding period of a risky
asset, such as a stock mutual fund, with reinvestment of dividends affects
the risk as defined by the standard deviation of the [annualized cumulative return](http://en.wikipedia.org/wiki/Rate_of_return#Geometric_average_rate_of_return),
and risk as defined by negative total returns.
Monte-Carlo simulation is used to demonstrate that extended holding periods
increase the annualized cumulative rate of return (geometric average rate),
but lead to a higher probability of large negative returns!
In this comparison, when the risky asset it held for only one year, the final
balance is invested in a risk-free asset for the remaining 19.
