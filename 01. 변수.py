Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

print('Hello, world!')
Hello, world!
print('Hello, python')
Hello, python
print('Hello, python')
Hello, python

========================= RESTART: C:/project/hello.py =========================
Hello, world!
1+!
SyntaxError: invalid syntax
1+1
2
1-2
-1
2*2
4
5/2
2.5
2.5
2.5
5/3
1.6666666666666667
5//2
2
4//2
2
5.5//2
2.0
5%2
1
2**10
1024
int(3.3)
3
int(5/2)
2
int('10')
10
10
10
type(10)
<class 'int'>
type(a)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    type(a)
NameError: name 'a' is not defined
type(3.3)
<class 'float'>
divmod(5,2)
(2, 1)
0b110
6
0ㅐ7
SyntaxError: invalid decimal literal
0o7
7
0xF
15
3.5+2.1
5.6

4.3 - 2.7
1.5999999999999996
float(5)
5.0

float(1+2)
3.0
float('5.3')
5.3
type(3.5)
<class 'float'>

1.2+1.3ㅓ
SyntaxError: invalid decimal literal
1.2+1.3j
(1.2+1.3j)
complex(1.2,1.3)
(1.2+1.3j)
(1.2+1.3j)
(1.2+1.3j)

35+1 *2
37
(35+1)*2
72
104
104
10/4
2.5
float 10/3
SyntaxError: invalid syntax
float(10//3)
3.0
float 10 / 3
SyntaxError: invalid syntax
7+(10-5)*2
17
int(0.2467 * 12 +4.159)
7
102*0.6 +225
286.2
x=10
x
10
y='Hello, world'
y
'Hello, world'
type(x)
<class 'int'>
type(y)
<class 'str'>
x,y,z = 10,20,30
x
10
y
20
z
30
x=y=z=10
x
10
y
10
z
10
x,y=10,20
x,y = y,x
x
20
y
10
del x
x
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    x
NameError: name 'x' is not defined
x= none
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    x= none
NameError: name 'none' is not defined. Did you mean: 'None'?
x = None
print(x)
None
a=10
a=a+10
a
20
a=10
a +=20
a
30
x = -10
-x
10
input()
Hello, world
'Hello, world'
x = input()
안녕하세요
x
'안녕하세요'
x = input('문자열을 입력하세요 : ')
문자열을 입력하세요 : 안녕하십니까?
ㅌ
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    ㅌ
NameError: name 'ᄐ' is not defined
x
'안녕하십니까?'
a= input('첫번째 숫자를 입력하세요 : ')
첫번째 숫자를 입력하세요 : 10
b = input('두번째 숫자를 입력하세요 :')
두번째 숫자를 입력하세요 :20
a+b
'1020'
a= input()
10
type(a)
<class 'str'>
a = int(input())
a= int(input('첫번째 숫자를 입력하세요: '))
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    a = int(input())
ValueError: invalid literal for int() with base 10: "a= int(input('첫번째 숫자를 입력하세요: '))"
a = int(input('첫번째 숫자를 입력하세요: '))
첫번째 숫자를 입력하세요: 10
b = int(input('두번쨰 숫자를 입력하세요 : '))
두번쨰 숫자를 입력하세요 : 20
a+b
30
a,b =input('문자열 두개를 입력하세요 :').split()
문자열 두개를 입력하세요 :Hello python
Hello
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    Hello
NameError: name 'Hello' is not defined
python
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    python
NameError: name 'python' is not defined
a,b =input('문자열 두개를 입력하세요 :').split()
문자열 두개를 입력하세요 :Hello Python

print(a)
Hello
print(b)
Python
print a+b
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print a+b
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print(a+b)
HelloPython
a,b = inprint('숫자 두 개를 입력하세요: ').split()
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    a,b = inprint('숫자 두 개를 입력하세요: ').split()
NameError: name 'inprint' is not defined. Did you mean: 'print'?
a,b = input('숫자 두 개를 입력하세요: ').split()
숫자 두 개를 입력하세요: 10 20
print (a+b)
1020
print (int(a) + int(b))
30
a,b = map(int, input('숫자 두개를 입력하세요: ').split())
숫자 두개를 입력하세요: 10,20
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    a,b = map(int, input('숫자 두개를 입력하세요: ').split())
ValueError: invalid literal for int() with base 10: '10,20'
a,b = map(int, input('숫자 두개를 입력하세요: ').split())
숫자 두개를 입력하세요: 10 20
print(a+b)
30
a,b = map(int, input('숫자 두개를 입력하세요: ').split(','))
숫자 두개를 입력하세요: 10,20
print(a+b)
30
print(1,2,3,sep=',')
1,2,3
print(1,2,3,sep='*')
1*2*3
print(1,2,3,sep=' ')
1 2 3
print(1,2,3,sep '/n')
SyntaxError: invalid syntax
print(1,2,3,sep='/n')
1/n2/n3
print(1,2,3,sep='\n')
1
2
3
print('1\n2\n3')
1
2
3
print(1, end='')
1
print(2, end="")
2
print(3)
3
print(1, end='')    # end에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됨
print(2, end='')
print(3)
SyntaxError: multiple statements found while compiling a single statement
print(1, end='')   
print(2, end='')
print(3)
SyntaxError: multiple statements found while compiling a single statement
print(1, end='')
print(2, end='')
print(3)
SyntaxError: multiple statements found while compiling a single statement
