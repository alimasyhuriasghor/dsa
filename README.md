# Introduction
Hello, welcome to my `dsa` branch. This branch mainly focuses my Data Structures and Algorithms (DSA) tutorials from [w3schools](https://www.w3schools.com/dsa/dsa_intro.php) — a website company that provides freemium (a business strategy that offers basic features for free and charges for advanced features.) coding tutorials. Each of the DSA tutorial has its own summarizations.

# Summarizations

# 1. DSA Intro
## What Are Data Structures?
A data structure is a way to store data in our computer's RAM (Random Access Memory) in distinct structures. We structure data in distinct ways depending on what data we have, and what we want to do it; for instance, suppose I want to store my full name in the computer's RAM, then the correct data structure to store my full name is by using the string data type (a group of characters that are used to represent text). Below are the examples of storing my full name in C, C++, and Python:

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

Or maybe I want to store student grades:

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

int main()
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

In essence, Data Structures are a way to store efficiently in different kind of structures.

# 2. What Are Algorithms?
An algorithm is a step-by-step instructions to solve a given problem or to achieve a specific goal. It is often used with data structures manipulate them, and if possible, it is often used to make our much faster.

