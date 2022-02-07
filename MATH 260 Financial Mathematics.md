# MATH 260 Financial Mathematics

## Part Ⅰ

### 1. Time Value of Money

**Principle:** Money invested today can be invested to earn interest/profit. 

1. **PV** = present value / initial investment
2. **r** = rate of return (%) per annum
3. **n** = no. of years
4. $FV_n = PV(1 + r)^n$ --- compounding formula 
5. $CF_n$ = future cash flow at the end of year n
6. $PV = \frac{CF_n}{(1+r)^n}$ ---discount formula

### 2. Interest Rates

* Nominal rate: $r_{nom}$  --- Yearly rate quoted by bank.
* Periodic rate $r_{PER}$  --- Rate per period. Assume m periods per year. 
* $r_{PER}=\frac{r_{nm}}{m}$ 
* $FV_n = PV(1 + \frac{r_{nm}}{m})^{nm}$
* Effective rates: $r_{EAR}$ --- Annual rate that produces the same result as $m$ compounding periods.  $r_{EAR}+1=(1+\frac{r_{nom}}{m})^m$ 
* Real rate of return $R$: Takes into account rising costs. 
  * Fischer's Equation: $1+R=\frac{1+r}{1+i}$ whose denominator is discounting cost and numerator is compounding income. 
  * $i$ = rate of inflation in the period
  * $r$ = rate of interest in the period
  * $R = \frac{r-i}{1+i}$
* Continuous Rates $r_C$ 
  * $\lim\limits_{m\rightarrow\infty}(FV_n) = \lim(PV(1+\frac{r_{nom}}{m})^{mn})$ 	
  * using $(1+\frac{x}{n})^n \rightarrow e^x$, $FV_n = PV*e^{r_Cn}$
