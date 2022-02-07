# MATH 260 Financial Mathematics

## Part Ⅰ

### 1. Time Value of Money

**Principle:** Money invested today can be invested to earn interest/profit. 

* **PV** = present value / initial investment
* **r** = rate of return (%) per annum
* **n** = no. of years
* $FV_n = PV(1 + r)^n$ --- compounding formula 
* $CF_n$ = future cash flow at the end of year n
* $PV = \frac{CF_n}{(1+r)^n}$ ---discount formula

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

### 3. Relationship between Continuous and compounded rates 

* $FV_n=PV(1+ \frac{r_{rom}}{m})^{nm} = PV*e^{r_C*n}$
* $r_C = m*ln(1+ \frac{r_{nom}}{m})$ & $r_{nom} = m*(e^{\frac{r_C}{m}} - 1)$

### 4. Risk and Return

Measuring risk and return: use influencing events and associated probs. 

**Investment** 
|Events:| 1 | 2 | 3 |
|---|---|---|----|
|Probabilities| $P_1$ | $P_2$ | $P_3$ |
|Returns: | $r_1$ | $r_2$ | $r_3$ |

* $\hat{r} = E(r) = \sum_{i=1}^{n}P_ir_i$

* $\sigma^2 = Var(r):= \sum_{i=1}^{n}P_i(r_i - \hat{r})^2 = E(r^2) - E[(r)]^2$  --- $\sigma=$ measure of risk

* Decision making 

  Coefficient of variation $CV=\frac{\sigma}{\hat{r}}$   PS: $\sigma $ lower the better 

  
