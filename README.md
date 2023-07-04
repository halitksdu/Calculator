#### This is my first project that I have uploaded to Github. I feel excited.
# Calculator
![](https://github.com/halitksdu/Calculator/blob/main/read/calculator.png)




## Description
In this project, the advanced calculator was created in the python environment. I did not use any libraries, my own module was created using mathematical formulas.

When we run the code, it asks us to enter the number of the operation we want to do. The numbers are printed on the screen as follows:
1. Addition
2. Extraction
3. Multiplication
4. Division
5. Percentage
6. Exponentian
7. Rooting
8. Logarithm
9. Ln
10. Factorial
11. Sinus
12. Cosinus
13. Tangent
14. Cotangent


Then it asks the appropriate question for the selected operation.(Some operations require two numbers, while others may require degrees or base.) I added the code below:
<br/> ![](https://github.com/halitksdu/Calculator/blob/main/read/write.png)

Finally, there are the transaction lines. I will talk about the module code as I am using it from the module.

## Module:
### 1. ln:
I approached the result by giving n=9999 in the formula. 
<br/> ![](https://github.com/halitksdu/Calculator/blob/main/read/ln.png)
#### Code:
![](https://github.com/halitksdu/Calculator/blob/main/read/ln%20code.png)

### 2. log:
I got the logarithm using the ln line.
<br/> ![](https://github.com/halitksdu/Calculator/blob/main/read/log.png)
#### Code:
![](https://github.com/halitksdu/Calculator/blob/main/read/log%20code.png)

### 3. con (converting degrees to radians):
I converted degrees to radials using the formula.
<br/> <img src="https://github.com/halitksdu/Calculator/blob/main/read/conv.png" alt="alt text" width="262,5" height="75">
#### Code:
![](https://github.com/halitksdu/Calculator/blob/main/read/conv%20code.png)

### 4. sin:
I obtained the sine using the Taylor series(got some help from the internet):
<br/> *sin(x) = x - x^3/3! + x^5/5! ...*
#### Code:
![](https://github.com/halitksdu/Calculator/blob/main/read/sin%20code.png)

### 5. cos, cot, tan:
I created the values using the sine line.

**Cosine:**
<br/><img src="https://github.com/halitksdu/Calculator/blob/main/read/cosine.png" alt="alt text" width="160" height="33">
<br/>**Tangent and Cotangent:**
<br/><img src="https://github.com/halitksdu/Calculator/blob/main/read/tan%20cot.png" alt="alt text" width="160" height="123">

#### Code:
![](https://github.com/halitksdu/Calculator/blob/main/read/tri%20code.png)


