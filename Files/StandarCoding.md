# Coding standarization

<a name="Item1"></a>

## File naming

1. All file names must begin with a lowercase letter, except by the imported components, and no-code files.

    XX ~~Index.py~~ XX

    ✓✓  index.py  ✓✓
    
2. Do not use the following characters in the name:  ¿ / \ : * ” < > [ ] & $ , . #

    XX ~~Plus#!.c~~ XX

    ✓✓ plus.py ✓✓
    
3. Be as short as possible.
    
    XX ~~MainClassForProgram.py~~ XX

    ✓✓  main.py  ✓✓
    
4. It should not have blank spaces, if necessary use "_" or differentiate the following word by capitalizing it.

     XX ~~Names of Company.md~~ XX  
    
     ✓✓  namesOfCompany.md  ✓✓___OR___✓✓  names_Of_Company.md  ✓✓
    
5. Always naming the extension of the type of code that the file uses.

    XX ~~ReadMe~~ XX

    ✓✓  ReadMe.md  ✓✓

<a name="Item2"></a>

## Inicial Documentation

Every code file/document should start with an initial content covering the following points:

1. "Description": Writing of the purpose of the complete code.

2. "Developers": Name of those involved in the code.

3. "State": State is definide for In progress/funcional/Bug/Complete.
    * In progress: Is worked in code at that momment.
    * Funcional: the code is worked, but no finished.
    * Bug: Have a error, don´t work the code.
    * Complete: The code is Finished and work whit any problem.

4. "Previous bugs": Known bugs that need to be fixed.
```python

#Description: Print the words "hello word"

#Developments: Luis Inzunza, David erez

#State: Bug

#Previous bugs: don´t print correctly


 print("Hello Word")
```

<a name="Item3"></a>

## Variable naming

1. They should not have spacing, in case of word differences in the 2nd word of the variable start it with a capital letter.
2. Start with a lowercase letter.
3. Have exact names of what they consider themselves to be.
4. For counters use i,j,k,l,m...y,z as variables, change the letter every time you start another counter in the same order. Giving the undestanding that "k" its the 3rd counter in the program.
5. Declaring in one line the same types of data. 
6. Spacing between '=' and next of ','
```c
int i = 0, j = 0;
char stundentName[5] = "Angel", gender[5] = "Male";

```

<a name="Item4"></a>

## Functions Documentation

Every function must have a short description of what happens inside them.

Every name must be understandable to what the function does, not exceding too much with the characters.

The keys will be the following way: The one that opens its going to be in the same line as the function and the one that closes will be in the same height as the funcion. 

The arguments must be separated by a space after a ',' and between the parentheses brackets

```c
// this job the bubble metod
void Bubble( array[][], chain1, chain2 ){

}
//Search in the va
void SearchNumbers( chain1 ){

}

```
<a name="Item5"></a>

## Spacing
The spacing will be 4 spaces per line.