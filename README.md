# Introduction
Hello, welcome to my `dsa` branch. This branch mainly focuses my Data Structures and Algorithms (DSA) tutorials from [w3schools](https://www.w3schools.com/dsa/dsa_intro.php) — a website company that provides freemium (a business strategy that offers basic features for free and charges for advanced features.) coding tutorials. Each of the DSA tutorial has its own summarizations.

# Summarizations

# 1. DSA Intro
## What Are Data Structures?
In simplest term, a data structure is a way to store data in our computer's RAM (Random Access Memory) in distinct strutures. We structure data in distinct ways depending on what data we have, and what we want to do it; for instance, suppose I want to store my full name in the computer's RAM, then the correct data structure to store my full name is an array of characters. Below are the examples of storing my full name in C, C++, and Python:

```C
// C code
#include <stdio.h>

int main(void)
{
    char full_name[] = "Ali Masyhuri Asghor";
    
    printf("My full name: %s\n", full_name);

    return 0;
}
```

```C++
// C++ code
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string full_name = "Ali Masyhuri Asghor";
    
    cout << "My full name: " << full_name << endl;

    return 0;
}
```

```Python
# Python code
full_name = "Ali Masyhuri Asghor"
print(f"My full name: {full_name}")
```

Or maybe I want to store student grades, then the correct data type to store student grades are using integer of arrays:

```C
// C code
#include <stdio.h>

int main(void)
{
    int student_grades[] = {80, 100, 75, 60, 85};
    
    for (int i = 0; i < sizeof(student_grades) / sizeof(student_grades[0]); i++)
        printf("student_grades[%d] = %d\n", i, student_grades[i]);

    return 0;
}
```

```C++
// C++ code
#include <iostream>

using namespace std;

int main(void)
{
    int student_grades[] = {80, 100, 75, 60, 85};
    
    for (int i = 0; i < sizeof(student_grades) / sizeof(student_grades[0]); i++)
        cout << "student_grades[" << i << "]" << " = " << student_grades[i] << endl;

    return 0;
}
```

```Python
# Python code
student_grades = [80, 100, 75, 60, 85]

for index, value in enumerate(student_grades):
    print(f"student_grades[{index}] = {value}")
```



> **Note📖**: Please do note that in Computer Science, there are two distinct kinds of data structures: primitive data structures and abstract data structures. Primitive data structures are basic data structures that are provided by the programming languages to represent single values, such as integers, floating-point values, booleans, characters, etc. Abstract data structure is higher-level data structures that are built using primitive data types and provide more comples and specialized operations. Some common examples of abstract data structures are arrays, stacks, linked lists, queues, trees, and graphs.

